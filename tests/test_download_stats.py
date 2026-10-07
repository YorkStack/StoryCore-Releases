import importlib.util
from pathlib import Path
from datetime import datetime, timezone
import unittest

spec = importlib.util.spec_from_file_location('stats', Path(__file__).resolve().parents[1] / 'scripts/update-download-stats.py')
stats = importlib.util.module_from_spec(spec)
spec.loader.exec_module(stats)


def release(tag='v2.0.8', draft=False, beta=False):
    return dict(tag_name=tag, draft=draft, prerelease=beta, assets=[
        dict(name='StoryCore_2.0.8_Mac-Installer.zip', download_count=2),
        dict(name='StoryCore_2.0.8_aarch64.dmg', download_count=3),
        dict(name='StoryCore.app.tar.gz', download_count=4),
        dict(name='storycore-update.json', download_count=100),
        dict(name='StoryCore-Erste-Schritte.pdf', download_count=50),
        dict(name='third-party-sources.zip', download_count=10),
    ])


class StatisticsTests(unittest.TestCase):
    def test_packages_only_and_total(self):
        table = stats.render_table([release()])
        self.assertIn('| Stabil | 2 | 3 | 4 | 9 |', table)

    def test_drafts_old_versions_excluded_and_numeric_sort(self):
        table = stats.render_table([release('v1.7.1'), release('v2.0.9'), release('v2.0.10', beta=True), release('v2.0.11', draft=True)])
        self.assertNotIn('1.7.1', table)
        self.assertNotIn('2.0.11', table)
        self.assertLess(table.index('2.0.10'), table.index('2.0.9'))
        self.assertIn('| Beta |', table)

    def test_unchanged_table_keeps_timestamp_and_surroundings(self):
        now = datetime(2026, 10, 7, tzinfo=timezone.utc)
        old = f'Introduction\n{stats.START}\n{stats.END}\nFooter'
        new = stats.update_readme(old, stats.render_table([release()]), now)
        self.assertTrue(new.startswith('Introduction\n'))
        self.assertTrue(new.endswith('\nFooter'))
        self.assertEqual(new, stats.update_readme(new, stats.render_table([release()]), now.replace(day=8)))

    def test_empty_response_and_bad_markers_do_not_overwrite(self):
        with self.assertRaises(ValueError): stats.render_table([])
        with self.assertRaises(ValueError): stats.update_readme('no markers', '', datetime.now())

    def test_invalid_count_fails(self):
        data = release()
        data['assets'][0]['download_count'] = -1
        with self.assertRaises(ValueError): stats.render_table([data])


if __name__ == '__main__': unittest.main()
