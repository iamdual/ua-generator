"""
Random User-Agent
Copyright: 2025 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import unittest

from src.ua_generator.data.browsers.chrome import VERSIONS as CHROME_VERSIONS
from src.ua_generator.data.filterer import Filterer
from src.ua_generator.data.version import VersionRange


class TestFilterer(unittest.TestCase):
    def test_unfiltered(self):
        filterer = Filterer(CHROME_VERSIONS)
        self.assertEqual(len(filterer.versions), len(CHROME_VERSIONS))

    def test_version_range(self):
        CHROME_MIN = 131
        CHROME_MAX = 135

        filterer = Filterer(CHROME_VERSIONS)
        filterer.version_range(VersionRange(CHROME_MIN, CHROME_MAX))
        self.assertEqual(len(filterer.versions), (CHROME_MAX - CHROME_MIN) + 1)

    def test_weighted_versions(self):
        filterer = Filterer(CHROME_VERSIONS)
        filterer.weighted_versions()
        self.assertEqual(len(filterer.versions), 1)


if __name__ == '__main__':
    unittest.main()
