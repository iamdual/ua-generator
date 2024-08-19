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

    def test_selected_versions(self):
        ua = ua_generator.generate()
        self.assertIsNone(ua.options.selected_versions)

        for i in range(0, 100):
            ua = ua_generator.generate(browser="chrome", options=Options(
                selected_versions={"chrome": VersionRange(min_version=100, max_version=102)}))
            self.assertIn(ua.generator.browser_version.major, (100, 101, 102))


if __name__ == '__main__':
    unittest.main()
