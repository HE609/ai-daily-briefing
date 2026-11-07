#!/usr/bin/env python3
"""Publish verified static output to gh-pages without changing the source checkout."""
import os
import json
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / 'public'


def git(*args, **kwargs):
    return subprocess.run(['git', *args], text=True, check=True, capture_output=True, cwd=ROOT, **kwargs).stdout.strip()


def deploy():
    if not (PUBLIC / 'index.html').exists() or not (PUBLIC / '.nojekyll').exists():
        raise SystemExit('Build and validate public/ before publishing')
    if git('remote', 'get-url', 'origin') not in ['https://github.com/HE609/ai-daily-briefing.git', 'git@github.com:HE609/ai-daily-briefing.git']:
        raise SystemExit('Unexpected remote; refusing to publish')
    reports = json.loads((PUBLIC / 'data/reports.json').read_text(encoding='utf-8'))
    receipt = {'source_commit': git('rev-parse', 'HEAD'), 'latest_report': reports[0]['date'], 'report_count': len(reports)}
    (PUBLIC / 'deployment.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
    parent = None
    remote_branch = git('ls-remote', '--heads', 'origin', 'gh-pages')
    if remote_branch:
        git('fetch', 'origin', 'gh-pages')
        parent = git('rev-parse', 'FETCH_HEAD')
    with tempfile.TemporaryDirectory(prefix='research-daily-pages-') as scratch:
        env = dict(os.environ, GIT_INDEX_FILE=str(Path(scratch) / 'index'))
        common = ['git', '--git-dir=' + str(ROOT / '.git'), '--work-tree=' + str(PUBLIC)]
        def stage(*args):
            return subprocess.run(common + list(args), env=env, cwd=PUBLIC, text=True, check=True, capture_output=True).stdout.strip()
        stage('read-tree', '--empty')
        stage('add', '--all')
        tree = stage('write-tree')
    if parent and git('rev-parse', parent + '^{tree}') == tree:
        print('Pages output already matches the published branch:', parent)
        return parent
    args = ['commit-tree', tree, '-m', 'Publish research daily for source ' + git('rev-parse', '--short', 'HEAD')]
    if parent:
        args.extend(['-p', parent])
    commit = git(*args)
    # Push only a fast-forward commit on the output branch; never check it out.
    subprocess.run(['git', 'push', 'origin', commit + ':refs/heads/gh-pages'], cwd=ROOT, check=True)
    print('Published static Pages branch:', commit)
    return commit


if __name__ == '__main__':
    deploy()
