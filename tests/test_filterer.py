"""
Random User-Agent
Copyright: 2025-2026 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import unittest

from src.ua_generator.data.browsers.chrome import VERSIONS as CHROME_VERSIONS
from src.ua_generator.data.filterer import Filterer
from src.ua_generator.data.version import VersionRange
from src.ua_generator.options import Options


class TestFilterer(unittest.TestCase):
    def test_unfiltered(self):
        filterer = Filterer(CHROME_VERSIONS, 'chrome', Options())
        self.assertEqual(len(filterer.versions), len(CHROME_VERSIONS))

    def test_version_range(self):
        CHROME_MIN = 131
        CHROME_MAX = 135

        options = Options(version_ranges={'chrome': VersionRange(CHROME_MIN, CHROME_MAX)})
        filterer = Filterer(CHROME_VERSIONS, 'chrome', options)
        self.assertEqual(len(filterer.versions), (CHROME_MAX - CHROME_MIN) + 1)

    def test_weighted_versions(self):
        filterer = Filterer(CHROME_VERSIONS, 'chrome', Options(weighted_versions=True))
        self.assertEqual(len(filterer.versions), 1)

    def test_latest_versions(self):
        filterer = Filterer(CHROME_VERSIONS, 'chrome', Options(latest_versions={'chrome': 3}))
        self.assertEqual(filterer.versions, CHROME_VERSIONS[-3:])

    def test_options_filters_versions_on_init(self):
        options = Options(latest_versions={'chrome': 3})
        filterer = Filterer(CHROME_VERSIONS, 'chrome', options)
        self.assertEqual(filterer.versions, CHROME_VERSIONS[-3:])

    def test_options_weighted_versions_is_optional(self):
        filterer = Filterer(CHROME_VERSIONS, 'chrome', Options(weighted_versions=False))
        self.assertEqual(len(filterer.versions), len(CHROME_VERSIONS))

        filterer = Filterer(CHROME_VERSIONS, 'chrome', Options(weighted_versions=True), max_weighted_version=3)
        self.assertEqual(len(filterer.versions), 1)


if __name__ == '__main__':
    unittest.main()
