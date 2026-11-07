#!/usr/bin/env python3
"""Sync completed reports, validate, commit content only and push to the existing site."""
import argparse
import fcntl
import subprocess
from pathlib import Path

from build import build
from check import check
from sync_reports import sync
from deploy_pages import deploy

ROOT = Path(__file__).resolve().parents[1]


def git(*args, capture=True):
    result = subprocess.run(['git', *args], cwd=ROOT, text=True, check=True, capture_output=capture)
    return result.stdout.strip() if capture else ''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=ROOT.parent)
    parser.add_argument('--dry-run', action='store_true', help='Import/build/check without committing or pushing')
    args = parser.parse_args()
    with (ROOT / '.publish.lock').open('w') as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise SystemExit('Another publisher is running; leave it to finish')
        remote = git('remote', 'get-url', 'origin')
        if remote not in ['https://github.com/HE609/ai-daily-briefing.git', 'git@github.com:HE609/ai-daily-briefing.git']:
            raise SystemExit('Unexpected remote; refusing to push')
        if git('branch', '--show-current') != 'main':
            raise SystemExit('Publisher requires main; never force-push or switch another working branch')
        if not args.dry_run:
            if git('status', '--porcelain'):
                raise SystemExit('Repository has uncommitted changes; review them before publishing')
            git('fetch', 'origin', 'main', capture=False)
            git('merge', '--ff-only', 'origin/main', capture=False)
        changes = sync(args.source.resolve())
        items = build()
        check()
        print('Imported:', ', '.join(changes) or 'no changes')
        if args.dry_run:
            print('Dry run complete; no commit or push performed')
            return
        git('add', '--', 'content/reports', 'content/research-map.md')
        if git('diff', '--cached', '--name-only'):
            git('commit', '-m', f'daily: publish {items[0]["date"]} research briefing', capture=False)
        git('push', 'origin', 'HEAD:main', capture=False)
        print('Pushed commit:', git('rev-parse', 'HEAD'))
        pages_commit = deploy()
        print('Pages output commit:', pages_commit)
        print('Website: https://he609.github.io/ai-daily-briefing/')
        print('Verify the gh-pages commit has a successful Pages build/deployment before reporting the issue as live.')


if __name__ == '__main__':
    main()
