#!/usr/bin/env python3
"""Validate report coverage, internal links, anchors, feeds and publication boundaries."""
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'public'


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.ids = set()
        self.links = []
        self.title = False
        self.main = False
        self.errors = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            if attrs['id'] in self.ids:
                self.errors.append(f'{self.path}: duplicate id {attrs["id"]}')
            self.ids.add(attrs['id'])
        self.title |= tag == 'title'
        self.main |= tag == 'main'
        for key in ['href', 'src']:
            if key in attrs:
                self.links.append(attrs[key])


def check():
    errors = []
    manifest = json.loads((OUT / 'data/reports.json').read_text(encoding='utf-8'))
    search = json.loads((OUT / 'data/search.json').read_text(encoding='utf-8'))
    expected = {p.name[:10] for p in ROOT.glob('????-??-??-ai-daily.md')}
    expected |= {p.stem for p in (ROOT / 'content/reports').glob('????-??-??.md')}
    dates = [x['date'] for x in manifest]
    if set(dates) != expected or len(dates) != len(set(dates)):
        errors.append('Report manifest does not exactly match archived source dates')
    if dates != sorted(dates, reverse=True):
        errors.append('Reports must be sorted newest first')
    if set(search) != set(dates):
        errors.append('Full-text index coverage mismatch')
    pages = {}
    for path in OUT.rglob('*.html'):
        text = path.read_text(encoding='utf-8')
        page = Page(path.relative_to(OUT))
        page.feed(text)
        pages[path.resolve()] = page
        errors.extend(page.errors)
        if not page.title:
            errors.append(f'{path}: missing page title')
        if re.search(r'/Users/|/nfs-shared|(?<![A-Za-z0-9_-])(?:gh[pousr]_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9_-]{25,})', text):
            errors.append(f'{path}: local path or credential-like string')
    for path, page in pages.items():
        for link in page.links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                continue
            dest = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if dest.is_dir():
                dest /= 'index.html'
            if not dest.exists():
                errors.append(f'{page.path}: missing local target {link}')
            elif parsed.fragment and dest in pages and unquote(parsed.fragment) not in pages[dest].ids:
                errors.append(f'{page.path}: missing anchor {link}')
    for item in manifest:
        if re.fullmatch(r'[A-E]|今日精读顺序', item['headline']):
            errors.append(f'{item["date"]}: a reading-order label was mistaken for the report headline')
        path = (OUT / item['url'] / 'index.html').resolve()
        if path not in pages or not pages[path].main:
            errors.append(f'{item["date"]}: report page missing semantic main')
        if len(search[item['date']]) < 200:
            errors.append(f'{item["date"]}: report appears empty or incomplete')
        if not (OUT / 'raw' / (item['date'] + '.md')).exists():
            errors.append(f'{item["date"]}: Markdown download missing')
    css = (OUT / 'assets/katex/katex.min.css').read_text(encoding='utf-8')
    for font in re.findall(r'url\(([^)]+)\)', css):
        if not (OUT / 'assets/katex' / font.strip('\"\'')).exists():
            errors.append('Missing bundled math font: ' + font)
    for name in ['feed.xml', 'sitemap.xml']:
        ET.parse(OUT / name)
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        raise SystemExit(1)
    print(f'Checked {len(dates)} complete reports, {len(pages)} HTML pages, all local links/anchors, full-text index, math fonts and feeds.')


if __name__ == '__main__':
    check()
