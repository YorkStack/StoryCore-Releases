#!/usr/bin/env python3
"""Update only the marked README table using GitHub release asset counters."""
import json
import os
from pathlib import Path
import re
from datetime import datetime, timezone
from urllib.request import Request, urlopen

REPOSITORY = 'YorkStack/StoryCore-Releases'
START = '<!-- download-stats:start -->'
END = '<!-- download-stats:end -->'


def fetch_releases():
    releases = []
    for page in range(1, 1001):
        headers = {'Accept': 'application/vnd.github+json', 'User-Agent': 'StoryCore-download-statistics'}
        if os.environ.get('GH_TOKEN'):
            headers['Authorization'] = 'Bearer ' + os.environ['GH_TOKEN']
        request = Request(f'https://api.github.com/repos/{REPOSITORY}/releases?per_page=100&page={page}', headers=headers)
        with urlopen(request, timeout=30) as response:
            batch = json.load(response)
        if not isinstance(batch, list):
            raise ValueError('Unexpected GitHub response; keeping existing statistics')
        releases.extend(batch)
        if len(batch) < 100:
            return releases
    raise ValueError('Pagination limit reached; keeping existing statistics')


def render_table(releases):
    rows = []
    for release in releases:
        if release.get('draft'):
            continue
        tag = release['tag_name']
        version = re.fullmatch(r'v?(\d+)\.(\d+)\.(\d+)', tag)
        if not version:
            continue
        key = tuple(map(int, version.groups()))
        if key < (2, 0, 2):
            continue
        counts = [0, 0, 0]
        for asset in release['assets']:
            name = asset['name']
            category = (0 if re.fullmatch(r'StoryCore_[^/]+_Mac-Installer\.zip', name)
                        else 1 if re.fullmatch(r'StoryCore_[^/]+\.dmg', name)
                        else 2 if name == 'StoryCore.app.tar.gz' else None)
            if category is not None:
                count = asset['download_count']
                if type(count) is not int or count < 0:
                    raise ValueError('Invalid download count; keeping existing statistics')
                counts[category] += count
        label = '.'.join(version.groups())
        status = 'Beta' if release['prerelease'] else 'Stabil'
        rows.append((key, f'| [{label}](https://github.com/{REPOSITORY}/releases/tag/{tag}) | {status} | ' + ' | '.join(map(str, [*counts, sum(counts)])) + ' |'))
    if not rows:
        raise ValueError('No public releases found; keeping existing statistics')
    return '\n'.join([
        '| Version | Status | Installer-ZIP | DMG | Update-Paket | Gesamt |',
        '| --- | --- | ---: | ---: | ---: | ---: |',
        *(row for _, row in sorted(rows, reverse=True)),
    ])


def update_readme(readme, table, now):
    if readme.count(START) != 1 or readme.count(END) != 1:
        raise ValueError('README statistics markers must occur exactly once')
    before, remaining = readme.split(START)
    current, after = remaining.split(END)
    if '\n'.join(line for line in current.splitlines() if line.startswith('|')) == table:
        return readme
    return f'{before}{START}\n\n{table}\n\nDatenstand (zuletzt geändert): {now:%d.%m.%Y %H:%M} UTC.\n\n{END}{after}'


if __name__ == '__main__':
    path = Path(__file__).resolve().parents[1] / 'README.md'
    old = path.read_text()
    new = update_readme(old, render_table(fetch_releases()), datetime.now(timezone.utc))
    if new != old:
        path.write_text(new)
        print('Download statistics updated.')
    else:
        print('Download statistics unchanged; no commit needed.')
