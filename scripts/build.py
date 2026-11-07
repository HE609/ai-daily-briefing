#!/usr/bin/env python3
"""Build the entire reading site. No browser-side Markdown or remote runtime assets."""
import datetime as dt
import hashlib
import html
import json
import math
import re
import shutil
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import quote
import xml.etree.ElementTree as ET

import markdown
import yaml
from markdown.extensions.toc import slugify_unicode

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'public'
CONFIG = json.loads((ROOT / 'site.json').read_text(encoding='utf-8'))
BASE = CONFIG['url'].rstrip('/')
H = html.escape


class TextOnly(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def plain(value):
    value = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', value)
    parser = TextOnly()
    parser.feed(value)
    return re.sub(r'\s+', ' ', ' '.join(parser.parts).replace('**', '').replace('`', '')).strip(' *#\n')


def md_render(text):
    if re.search(r'<\s*(?:script|iframe|object|embed)\b|\bon\w+\s*=|javascript\s*:', text, re.I):
        raise ValueError('Executable HTML is not permitted in report content')
    engine = markdown.Markdown(
        extensions=['extra', 'sane_lists', 'toc', 'pymdownx.arithmatex', 'pymdownx.magiclink'],
        extension_configs={'toc': {'slugify': slugify_unicode}, 'pymdownx.arithmatex': {'generic': True}},
        output_format='html5',
    )
    body = engine.convert(text)
    body = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" target="_blank" rel="noopener noreferrer"', body)
    body = body.replace('<table>', '<div class="table-scroll" role="region" aria-label="数据表格" tabindex="0"><table>').replace('</table>', '</table></div>')
    return body, engine.toc_tokens


def flatten(tokens):
    values = []
    for token in tokens:
        values.append({'title': plain(token['name']), 'id': token['id'], 'level': token['level']})
        values.extend(flatten(token.get('children', [])))
    return values


def write(path, value):
    dest = OUT / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(value, encoding='utf-8')


def tags(values):
    return ''.join(f'<span class="tag">{H(t)}</span>' for t in values)


def short_title(title):
    title = re.sub(r'^\d+[.、]\s*', '', plain(title))
    title = re.sub(r'[｜|]\s*P\d.*$', '', title).strip()
    if len(title) > 58:
        title = re.split(r'[:：—]', title)[0].strip()
    return title


def read_report(path, date, legacy=False):
    raw = path.read_text(encoding='utf-8')
    meta = {}
    body = raw
    if body.startswith('---\n'):
        _, fm, body = body.split('---', 2)
        meta = yaml.safe_load(fm) or {}
    body = re.sub(r'^\s*# [^\n]+\n', '', body, count=1)
    body = re.sub(r'^\s*正文开始[：:]\s*', '', body)
    rendered, toc = md_render(body.strip())
    headings = flatten(toc)
    numbered = [x for x in headings if re.match(r'^\d+[.、]\s*', x['title'])]
    highlights = [{'title': short_title(x['title']), 'id': x['id']} for x in numbered[:5]]
    reading_section = re.search(r'^## 今日精读顺序\s*\n(.*?)(?=^## |\Z)', body, re.M | re.S)
    section = reading_section.group(1) if reading_section else ''
    ranked_names = re.findall(r'\*\*[A-E]\s*→\s*(.+?)\*\*', section)
    order = re.search(r'今天我建议的精读顺序是[：:][ \t]*([^\n]+)', section)
    names = ranked_names or ([plain(x).strip('。* ') for x in order.group(1).split('→')] if order else [])
    names = [n for n in names if len(n) >= 3 and not re.match(r'^[A-E][.、：:]?$', n)]
    if names:
        def normalized(value):
            return re.sub(r'[^\w]', '', value.casefold())
        ranked = []
        for name in names[:5]:
            key = normalized(name)
            candidates = numbered or headings
            candidate = next((x for x in candidates if key in normalized(x['title'])), None)
            if candidate is None and len(key) >= 18:
                candidate = next((x for x in candidates if key[:18] in normalized(x['title'])), None)
            if candidate:
                ranked.append({'title': name, 'id': candidate['id']})
        if len(ranked) >= min(3, len(highlights)):
            highlights = ranked
    if not highlights:
        highlights = [{'title': short_title(x['title']), 'id': x['id']} for x in headings[:5]]
    paragraphs = [plain(p) for p in body.split('\n\n') if not p.lstrip().startswith(('#', '|', '-', '1.', '>'))]
    intro = next((p for p in paragraphs if re.search(r'今天最重要|今日判断|今天最值得|最重要的产业新增', p)), '')
    if not intro:
        intro = next((p for p in paragraphs if len(p) > 60 and not p.startswith(('来源覆盖', '生成时间', '检索窗口', '检索主窗口'))), '')
    judgment = re.search(r'(?:今天最重要的(?:新增)?判断是|今天最值得关注的(?:变化|判断)是|今日判断)[：:]\s*(.*)', intro)
    if judgment:
        intro = judgment.group(1)
    elif '最重要的产业新增' in intro:
        intro = intro[intro.index('最重要的产业新增'):]
    if intro:
        # Use a complete sentence instead of fabricating punctuation mid-word.
        first_sentence = re.split(r'(?<=[。！？])', intro)[0].strip()
        if len(first_sentence) > 170:
            fragment = first_sentence[:160]
            boundary = max(fragment.rfind('，'), fragment.rfind('；'))
            summary = fragment[:boundary] + '…' if boundary > 70 else fragment + '…'
        else:
            summary = first_sentence if first_sentence.endswith(('。', '！', '？')) else first_sentence + '。'
    else:
        summary = '阅读本期完整研究观察、论文解读与来源记录。'
    headline_parts = [short_title(x['title']).rstrip('。') for x in highlights[:3]]
    if len(' · '.join(headline_parts)) > 110:
        headline_parts = [re.split(r'[:：]|[（(]', x)[0].strip() for x in headline_parts]
    headline = ' · '.join(headline_parts) or f'AI 研究观察 · {date}'
    override = CONFIG.get('issues', {}).get(date, {})
    headline = str(meta.get('headline') or override.get('headline') or headline)
    summary = str(meta.get('summary') or override.get('summary') or summary)
    field = ' '.join(h['title'] for h in headings) + ' ' + intro
    topic_patterns = {
        '世界模型': r'world.?model|world.?action|世界模型|WAM|世界生成',
        '空间智能': r'spatial|空间智能|3D|4D|场景|几何',
        '具身智能': r'robot|VLA|具身|机器人|跨本体',
        'Agent': r'agent|自改进|自进化|智能体|强化学习',
        '通用 AI': r'LLM|VLM|多模态|大模型|AI for Science',
    }
    scores = [(k, len(re.findall(v, field, re.I))) for k, v in topic_patterns.items()]
    topics = meta.get('topics') or [k for k, s in sorted(scores, key=lambda kv: -kv[1])[:3] if s > 0] or ['通用 AI']
    text = plain(rendered)
    return {
        'date': date, 'headline': headline, 'summary': summary, 'topics': topics,
        'series': 'AI 前沿情报' if legacy else '空间智能与通用 AI',
        'minutes': max(1, math.ceil(len(text) / 600)),
        'highlights': highlights, 'headings': headings, 'body': rendered,
        'raw': raw, 'text': text, 'legacy': path.name if legacy else None,
        'url': f'reports/{date}/',
    }


def shell(title, description, content, prefix='./', page='', math_enabled=False):
    canonical = BASE + '/' + page
    browser_title = title if 'Yunhe' in title else title + ' · Yunhe'
    asset_hash = hashlib.sha256((ROOT / 'assets' / 'site.css').read_bytes() + (ROOT / 'assets' / 'site.js').read_bytes()).hexdigest()[:10]
    maths = ''
    if math_enabled:
        maths = f'<link rel="stylesheet" href="{prefix}assets/katex/katex.min.css"><script defer src="{prefix}assets/katex/katex.min.js"></script>'
    return f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light"><meta name="theme-color" content="#f7f8f3">
<title>{H(browser_title)}</title><meta name="description" content="{H(description, quote=True)}">
<link rel="canonical" href="{H(canonical)}"><meta property="og:type" content="article"><meta property="og:title" content="{H(title, quote=True)}"><meta property="og:description" content="{H(description, quote=True)}"><meta property="og:url" content="{H(canonical)}">
<link rel="icon" type="image/svg+xml" href="{prefix}assets/favicon.svg"><link rel="alternate" type="application/atom+xml" title="Yunhe 科研日报" href="{prefix}feed.xml">
<link rel="stylesheet" href="{prefix}assets/site.css?v={asset_hash}">{maths}<script defer src="{prefix}assets/site.js?v={asset_hash}"></script></head>
<body data-root="{prefix}"><a class="skip-link" href="#main">跳到正文</a><div class="reading-progress" aria-hidden="true"></div>
<header class="site-header"><div class="wrap header-inner"><a class="brand" href="{prefix}" aria-label="Yunhe 科研日报首页"><svg viewBox="0 0 32 32" aria-hidden="true"><path d="M5 6h10v20H5zM17 6h10v20H17z"/><path d="M9 11h2m-2 5h2m10-5h2m-2 5h2"/></svg><span>Yunhe <span class="brand-divider">/</span> 科研日报<small>RESEARCH, DAY BY DAY</small></span></a>
<nav aria-label="主导航"><a href="{prefix}latest/">最新一期</a><a href="{prefix}#archive">历史归档</a><a href="{prefix}map/">研究地图</a><a class="github-nav" href="{CONFIG['repository']}" target="_blank" rel="noopener noreferrer">GitHub <span aria-hidden="true">↗</span></a></nav></div></header>
{content}
<footer class="site-footer wrap"><div><strong>Yunhe / 科研日报</strong><p>把每天的发现，留给下一次思考。</p></div><div class="footer-right"><span>以原始来源为依据 · 证据状态见各期正文</span><a href="{prefix}feed.xml">RSS 订阅 ↗</a></div></footer><button class="back-top" type="button" aria-label="返回顶部" title="返回顶部">↑</button>
</body></html>'''


def card(item):
    return f'''<a class="report-card" href="{item['url']}"><div class="card-meta"><time datetime="{item['date']}">{item['date'].replace('-', '.')}</time><span>{item['minutes']} 分钟阅读</span></div><h3>{H(item['headline'])}</h3><p>{H(item['summary'])}</p><div class="card-bottom"><div class="tags">{tags(item['topics'][:2])}</div><span class="card-arrow" aria-hidden="true">↗</span></div></a>'''


def home(items):
    item = items[0]
    date = dt.date.fromisoformat(item['date'])
    months = sorted({x['date'][:7] for x in items}, reverse=True)
    options = ''.join(f'<option value="{m}">{int(m[:4])} 年 {int(m[5:])} 月</option>' for m in months)
    picks = ''.join(f'<li><a href="{item["url"]}#{quote(p["id"])}"><span class="pick-number">{i:02d}</span><span>{H(p["title"])}</span><span class="pick-arrow" aria-hidden="true">↗</span></a></li>' for i, p in enumerate(item['highlights'][:5], 1))
    content = f'''<main id="main" class="wrap home">
<section class="hero"><div><p class="eyebrow"><span class="status-dot"></span> A DAILY PRACTICE OF CURIOSITY</p><h1>读懂今天的进展，<br>看见明天的问题。</h1><p class="hero-description">空间智能、世界模型与具身智能。<br>有来源的研究观察，持续生长的知识脉络。</p></div><div class="hero-date"><span>LATEST EDITION / {date.year}</span><strong>{date:%m.%d}<i>↗</i></strong><span>{date.strftime('%A').upper()} <b>·</b> 已收录 {len(items)} 期</span></div></section>
<section class="latest-section" aria-label="最新一期"><div class="latest-feature"><div class="feature-meta"><span><span class="status-dot"></span> 最新一期</span><time datetime="{item['date']}">{item['date'].replace('-', ' / ')}</time></div><a class="feature-link" href="{item['url']}"><h2>{H(item['headline'])}</h2><p>{H(item['summary'])}</p><span class="feature-cta">阅读完整日报 <span aria-hidden="true">↗</span></span></a><div class="feature-footer"><span>{item['series']}</span><span>{item['minutes']} 分钟阅读</span></div><svg class="feature-art" viewBox="0 0 320 320" aria-hidden="true"><g fill="none" stroke="currentColor"><circle cx="160" cy="160" r="120"/><ellipse cx="160" cy="160" rx="56" ry="120" transform="rotate(40 160 160)"/><ellipse cx="160" cy="160" rx="56" ry="120" transform="rotate(-40 160 160)"/><path d="M15 160h290M160 15v290"/><circle cx="160" cy="160" r="87"/></g></svg></div><aside class="reading-picks"><div class="section-kicker"><span>本期精读</span><span>THE READING LIST</span></div><ol>{picks}</ol></aside></section>
<section id="archive" class="archive" aria-labelledby="archive-heading"><div class="archive-title"><div><p class="eyebrow">THE ARCHIVE</p><h2 id="archive-heading">每一天，都有迹可循<span>{len(items):03d}</span></h2></div><p>从最新发现，回到问题的来路。</p></div>
<form class="archive-tools" role="search" id="search-form"><label class="search-field"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5"/><path d="m16 16 5 5"/></svg><input id="search" name="q" type="search" autocomplete="off" placeholder="搜索论文、模型或关键词…" aria-label="搜索日报全文"><kbd>/</kbd></label><label class="month-field"><span class="sr-only">按月份筛选</span><select id="month" name="month" aria-label="按月份筛选"><option value="">全部月份</option>{options}</select></label></form>
<div class="topic-filters" role="group" aria-label="按研究主题筛选">{''.join(f'<button type="button" data-topic="{t if t != "全部" else ""}" aria-pressed="{str(t == "全部").lower()}">{t}</button>' for t in ['全部','世界模型','空间智能','具身智能','Agent','通用 AI'])}</div>
<div class="results-line"><span id="result-count" role="status" aria-live="polite">共 {len(items)} 期日报 · 按日期倒序</span><button type="button" id="reset-filters" hidden>清除筛选 ×</button></div>
<div class="report-grid" id="report-grid">{''.join(card(x) for x in items[:12])}</div><div class="empty-state" id="empty-state" hidden><span>⌕</span><h3>暂时没有匹配的日报</h3><p>试试更短的关键词，或清除月份与主题筛选。</p></div><button type="button" class="load-more" id="load-more">继续浏览历史日报 <span aria-hidden="true">↓</span></button><noscript><p class="no-script">可通过下面的日期索引阅读全部归档；全文搜索需要 JavaScript。</p><div class="all-dates">{''.join(f'<a href="{x["url"]}">{x["date"]}</a>' for x in items)}</div></noscript>
<div class="archive-note"><span>关于这份归档</span><p>收录已保存的完整成稿。日期之间的空档表示未收录，不代表当天没有研究发布；历史内容保留成稿时的证据与资源状态。</p><a href="map/">沿着研究地图继续探索 ↗</a></div></section></main>'''
    write('index.html', shell(CONFIG['title'], CONFIG['description'], content))


def report_page(item, older=None, newer=None):
    toc = ''.join(f'<a class="toc-level-{min(x["level"],3)}" href="#{quote(x["id"])}">{H(x["title"])}</a>' for x in item['headings'] if x['level'] <= 3)
    pagination = ''
    for label, other, direction in [('← 上一期', older, 'older'), ('下一期 →', newer, 'newer')]:
        if other:
            pagination += f'<a class="{direction}" href="../{other["date"]}/"><span>{label} · {other["date"]}</span><strong>{H(other["headline"])}</strong></a>'
        else:
            pagination += '<span></span>'
    content = f'''<main id="main" class="wrap reader"><a class="breadcrumb" href="../../#archive">← 返回日报归档</a><header class="article-header"><p class="eyebrow">{H(item['series'])} <span> / </span> RESEARCH DAILY</p><h1>{H(item['headline'])}</h1><p class="article-deck">{H(item['summary'])}</p><div class="article-meta"><time datetime="{item['date']}">{item['date'].replace('-', ' / ')}</time><span>约 {item['minutes']} 分钟阅读</span><div class="tags">{tags(item['topics'])}</div></div></header>
<div class="reader-layout"><aside class="toc"><details open><summary>本期目录 <span aria-hidden="true">⌄</span></summary><nav aria-label="本期目录">{toc}</nav></details><div class="reader-actions"><button type="button" id="copy-link">复制本期链接 ↗</button><a href="../../raw/{item['date']}.md" download>下载 Markdown ↓</a></div></aside><div class="article-column"><div class="original-title">空间智能与通用 AI 科研晨报 <span>｜</span> {item['date']}</div><article class="prose">{item['body']}</article><nav class="issue-pagination" aria-label="相邻日报">{pagination}</nav><p class="article-end">读到这里，留一个问题给明天。<a href="../../map/">查看持续研究地图 ↗</a></p></div></div></main>'''
    if item['legacy']:
        content = content.replace('空间智能与通用 AI 科研晨报 <span>', 'AI 前沿情报日报 <span>')
    write(f'reports/{item["date"]}/index.html', shell(f'{item["date"]}｜{item["headline"]}', item['summary'], content, '../../', item['url'], 'arithmatex' in item['body']))
    write(f'raw/{item["date"]}.md', item['raw'])
    if item['legacy']:
        alias = item['legacy'].replace('.md', '.html')
        write(alias, f'<!doctype html><html lang="zh-CN"><meta charset="utf-8"><title>{item["date"]} 日报</title><meta http-equiv="refresh" content="0;url=reports/{item["date"]}/"><link rel="canonical" href="{BASE}/{item["url"]}"><a href="reports/{item["date"]}/">阅读 {item["date"]} 完整日报</a></html>')
        write(item['legacy'], item['raw'])


def research_map(latest):
    path = ROOT / 'content' / 'research-map.md'
    if not path.exists():
        return
    raw = path.read_text(encoding='utf-8')
    text = re.sub(r'^# [^\n]+\n', '', raw, count=1)
    rendered, toc = md_render(text)
    links = ''.join(f'<a href="#{quote(x["id"])}">{H(x["title"])}</a>' for x in flatten(toc) if x['level'] <= 3)
    content = f'''<main id="main" class="wrap reader map-reader"><a class="breadcrumb" href="../">← 返回日报首页</a><header class="article-header"><p class="eyebrow">A LIVING RESEARCH MAP</p><h1>把进展连起来，<br>让问题浮现出来。</h1><p class="article-deck">感知与状态 → 转移预测 → 规划与执行 → 学习闭环 → 评测与基础设施</p><div class="article-meta"><span>随日报持续更新</span><span>最新一期 {latest['date']}</span></div></header><div class="reader-layout"><aside class="toc"><details open><summary>地图目录 <span aria-hidden="true">⌄</span></summary><nav aria-label="地图目录">{links}</nav></details></aside><article class="prose">{rendered}</article></div></main>'''
    write('map/index.html', shell('持续研究地图', '研究问题、近期趋势、未解决的 gap 与可验证的研究机会。', content, '../', 'map/', 'arithmatex' in rendered))


def feeds(items):
    ns = 'http://www.w3.org/2005/Atom'
    ET.register_namespace('', ns)
    feed = ET.Element(f'{{{ns}}}feed')
    def sub(parent, tag, text=None, **attrs):
        node = ET.SubElement(parent, f'{{{ns}}}{tag}', attrs)
        node.text = text
        return node
    sub(feed, 'title', CONFIG['title'])
    sub(feed, 'id', BASE + '/')
    sub(feed, 'link', href=BASE + '/feed.xml', rel='self')
    sub(feed, 'link', href=BASE + '/')
    sub(feed, 'updated', items[0]['date'] + 'T01:00:00Z')
    sub(sub(feed, 'author'), 'name', 'Yunhe Ni')
    for item in items[:30]:
        entry = sub(feed, 'entry')
        sub(entry, 'title', item['date'] + '｜' + item['headline'])
        sub(entry, 'id', BASE + '/' + item['url'])
        sub(entry, 'link', href=BASE + '/' + item['url'])
        sub(entry, 'updated', item['date'] + 'T01:00:00Z')
        sub(entry, 'summary', item['summary'])
    write('feed.xml', '<?xml version="1.0" encoding="utf-8"?>\n' + ET.tostring(feed, encoding='unicode'))
    urls = [BASE + '/', BASE + '/map/'] + [BASE + '/' + x['url'] for x in items]
    write('sitemap.xml', '<?xml version="1.0" encoding="utf-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join(f'<url><loc>{H(url)}</loc></url>' for url in urls) + '</urlset>')
    write('robots.txt', f'User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n')


def build():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(ROOT / 'assets', OUT / 'assets')
    items = {}
    for path in sorted(ROOT.glob('????-??-??-ai-daily.md')):
        date = path.name[:10]
        items[date] = read_report(path, date, legacy=True)
    for path in sorted((ROOT / 'content' / 'reports').glob('????-??-??.md')):
        dt.date.fromisoformat(path.stem)
        items[path.stem] = read_report(path, path.stem)
    ordered = sorted(items.values(), key=lambda x: x['date'], reverse=True)
    if not ordered:
        raise ValueError('No reports found')
    for i, item in enumerate(ordered):
        report_page(item, ordered[i+1] if i+1 < len(ordered) else None, ordered[i-1] if i else None)
    home(ordered)
    research_map(ordered[0])
    keys = ['date', 'headline', 'summary', 'topics', 'series', 'minutes', 'url']
    manifest = [{k: item[k] for k in keys} for item in ordered]
    write('data/reports.json', json.dumps(manifest, ensure_ascii=False, separators=(',', ':')))
    write('data/search.json', json.dumps({item['date']: item['text'] for item in ordered}, ensure_ascii=False, separators=(',', ':')))
    latest = ordered[0]
    # This stable address always opens the newest completed report.
    write('latest/index.html', f'<!doctype html><html lang="zh-CN"><meta charset="utf-8"><title>最新一期科研日报</title><meta http-equiv="refresh" content="0;url=../{latest["url"]}"><link rel="canonical" href="{BASE}/{latest["url"]}"><a href="../{latest["url"]}">阅读最新一期 {latest["date"]}</a></html>')
    error = '<main id="main" class="wrap error-page"><p class="eyebrow">404 / PAGE NOT FOUND</p><h1>这一页，还没有写下。</h1><p>回到归档，继续寻找你关心的问题。</p><a class="primary-link" href="' + BASE + '/">返回日报首页 ↗</a></main>'
    write('404.html', shell('页面未找到', '返回日报归档', error, BASE + '/'))
    write('.nojekyll', '')
    feeds(ordered)
    print(f'Built {len(ordered)} reports: {ordered[-1]["date"]} → {ordered[0]["date"]}; {OUT}')
    return ordered


if __name__ == '__main__':
    build()
