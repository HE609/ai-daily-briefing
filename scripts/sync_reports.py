#!/usr/bin/env python3
"""Import completed local reports; preserve original research prose and source links."""
import argparse
import datetime as dt
import json
import re
from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SITE_URL = json.loads((ROOT / 'site.json').read_text(encoding='utf-8'))['url'].rstrip('/')
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
R = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'


def publishable(text):
    # Desktop attachment links cannot work on the public site. Keep their labels.
    def local_link(match):
        label, target = match.groups()
        target = target.strip('<> ')
        if re.match(r'(?:https?://|mailto:|#)', target):
            return match.group()
        date = re.search(r'\d{4}-\d{2}-\d{2}', target)
        if target.endswith('.md') and date:
            return f'[{label}]({SITE_URL}/reports/{date.group()}/)'
        if target.endswith(('.docx', '.pdf')) or target.startswith(('/Users/', '/mnt/', '/nfs', 'file:', 'sandbox:')):
            return label + '（本地附件）'
        return match.group()
    text = re.sub(r'\[([^\]]+)\]\(([^\n)]+)\)', local_link, text)
    if re.search(r'(?<![A-Za-z0-9_-])(?:gh[pousr]_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9_-]{25,})|-----BEGIN .*PRIVATE KEY', text):
        raise ValueError('Credential-like text found in report; review before publishing')
    if re.search(r'/Users/|/nfs-shared|file://', text):
        raise ValueError('Unresolved local path; review before publishing')
    text = re.sub(r'(?<! ) $', '', text, flags=re.M)
    return text.rstrip() + '\n'


def docx_markdown(path):
    with ZipFile(path) as archive:
        rels = ET.fromstring(archive.read('word/_rels/document.xml.rels'))
        links = {r.get('Id'): r.get('Target') for r in rels}
        body = ET.fromstring(archive.read('word/document.xml')).find(W + 'body')

    def inline(el):
        out = []
        for child in el:
            if child.tag == W + 'hyperlink':
                label = ''.join(n.text or '' for n in child.iter(W + 't'))
                href = links.get(child.get(R + 'id'), '')
                out.append(f'[{label}]({href})' if href.startswith(('https://', 'http://')) else label)
            elif child.tag == W + 'r':
                out.append(''.join(n.text or '' for n in child.iter(W + 't')))
        return ''.join(out).strip()

    blocks = []
    for el in body:
        if el.tag == W + 'p':
            value = inline(el)
            if not value:
                continue
            style = el.find('./' + W + 'pPr/' + W + 'pStyle')
            name = style.get(W + 'val') if style is not None else ''
            prefix = {'Title': '# ', 'Heading1': '## ', 'Heading2': '### ', 'ListNumber': '1. '}.get(name, '')
            blocks.append(prefix + value)
        elif el.tag == W + 'tbl':
            rows = []
            for row in el.findall(W + 'tr'):
                cells = ['<br>'.join(inline(p) for p in c.findall(W + 'p')).replace('|', '\\|') for c in row.findall(W + 'tc')]
                rows.append(cells)
            if rows:
                width = max(map(len, rows))
                rows = [r + [''] * (width - len(r)) for r in rows]
                lines = ['| ' + ' | '.join(r) + ' |' for r in rows]
                lines.insert(1, '| ' + ' | '.join(['---'] * width) + ' |')
                blocks.append('\n'.join(lines))
    return '\n\n'.join(blocks) + '\n'


def sync(source):
    target = ROOT / 'content' / 'reports'
    target.mkdir(parents=True, exist_ok=True)
    by_date = {}
    for path in sorted(source.glob('*.md')):
        if '晨报' not in path.name:
            continue
        match = re.search(r'\d{4}-\d{2}-\d{2}', path.name)
        if match:
            date = match.group()
            dt.date.fromisoformat(date)
            if date in by_date:
                raise ValueError(f'Multiple report sources for {date}; choose the final version')
            by_date[date] = path
    changes = []
    for date, path in by_date.items():
        text = publishable(path.read_text(encoding='utf-8'))
        destination = target / f'{date}.md'
        if not destination.exists() or destination.read_text(encoding='utf-8') != text:
            destination.write_text(text, encoding='utf-8')
            changes.append(date)
    # Earliest local report only has a Word source; this is a faithful text import.
    for path in sorted(source.glob('*晨报*.docx')):
        match = re.search(r'\d{4}-\d{2}-\d{2}', path.name)
        if not match or match.group() in by_date:
            continue
        date = match.group()
        destination = target / f'{date}.md'
        if destination.exists():
            continue
        text = publishable(docx_markdown(path))
        destination.write_text(text, encoding='utf-8')
        changes.append(date)
    map_source = source / '研究地图-持续更新.md'
    if map_source.exists():
        text = publishable(map_source.read_text(encoding='utf-8'))
        destination = ROOT / 'content' / 'research-map.md'
        if not destination.exists() or destination.read_text(encoding='utf-8') != text:
            destination.write_text(text, encoding='utf-8')
            changes.append('research-map')
    return changes


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=ROOT.parent)
    args = parser.parse_args()
    print('Imported:', ', '.join(sync(args.source.resolve())) or 'already up to date')
