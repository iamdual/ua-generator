"""
Random User-Agent
Copyright: 2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import unittest

import src.ua_generator as ua_generator
from src.ua_generator.data.version import VersionRange
from src.ua_generator.options import Options


class TestOptions(unittest.TestCase):
    def test_weighted_versions(self):
        ua = ua_generator.generate()
        self.assertFalse(ua.options.weighted_versions)
        ua = ua_generator.generate(options=Options(weighted_versions=True))
        self.assertTrue(ua.options.weighted_versions)
        ua = ua_generator.generate(options=Options(weighted_versions=False))
        self.assertFalse(ua.options.weighted_versions)

    def test_version_ranges(self):
        ua = ua_generator.generate()
        self.assertIsNone(ua.options.version_ranges)

        options = Options()
        options.version_ranges={'chrome': VersionRange(125, 127)}

        for i in range(0, 100):
            ua = ua_generator.generate(browser='chrome', options=options)
            self.assertIn(ua.generator.browser_version.major, (125, 126, 127))


if __name__ == '__main__':
    unittest.main()
