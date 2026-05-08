"""
Random User-Agent
Copyright: 2024-2026 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import unittest

import src.ua_generator as ua_generator
from src.ua_generator.data.browsers.chrome import VERSIONS as CHROME_VERSIONS
from src.ua_generator.data.platforms.ios import VERSIONS as IOS_VERSIONS
from src.ua_generator.data.version import VersionRange
from src.ua_generator.options import Options


class TestOptions(unittest.TestCase):
    def test_weighted_versions(self):
        ua = ua_generator.generate()
        self.assertFalse(ua.options.weighted_versions)
        self.assertFalse(ua.options.latest_versions)
        ua = ua_generator.generate(options=Options(weighted_versions=True))
        self.assertTrue(ua.options.weighted_versions)
        ua = ua_generator.generate(options=Options(weighted_versions=False))
        self.assertFalse(ua.options.weighted_versions)

    def test_version_ranges(self):
        ua = ua_generator.generate()
        self.assertIsNone(ua.options.version_ranges)

        options = Options()
        options.version_ranges = {'chrome': VersionRange(125, 127)}

        for i in range(0, 100):
            ua = ua_generator.generate(browser='chrome', options=options)
            self.assertIn(ua.generator.browser_version.major, (125, 126, 127))

    def test_latest_versions_true(self):
        options = Options()
        options.latest_versions = True

        for i in range(0, 100):
            ua = ua_generator.generate(platform='ios', browser='chrome', options=options)
            self.assertEqual(ua.generator.browser_version.to_tuple(), CHROME_VERSIONS[-1].to_tuple())
            self.assertEqual(ua.generator.platform_version.to_tuple(), IOS_VERSIONS[-1].to_tuple())

    def test_latest_versions_dict(self):
        options = Options()
        options.latest_versions = {
            'chrome': 3,
            'ios': 3,
        }

        latest_chrome_versions = [version.to_tuple() for version in CHROME_VERSIONS[-3:]]
        latest_ios_versions = [version.to_tuple() for version in IOS_VERSIONS[-3:]]

        for i in range(0, 100):
            ua = ua_generator.generate(platform='ios', browser='chrome', options=options)
            self.assertIn(ua.generator.browser_version.to_tuple(), latest_chrome_versions)
            self.assertIn(ua.generator.platform_version.to_tuple(), latest_ios_versions)

    def test_tied_safari_version(self):
        for i in range(0, 100):
            options = Options()
            options.tied_safari_version = True
            ua = ua_generator.generate(platform=('macos', 'ios'), browser='safari', options=options)
            self.assertEqual(ua.generator.browser_version.format(), ua.generator.platform_version.format())


if __name__ == '__main__':
    unittest.main()
