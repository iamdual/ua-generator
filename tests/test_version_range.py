"""
Random User-Agent
Copyright: 2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import unittest

import src.ua_generator as ua_generator
from src.ua_generator.data.version import Version, VersionRange
from src.ua_generator.options import Options


class TestVersionRange(unittest.TestCase):
    def test_version_range(self):
        version_range = VersionRange(1, 2)
        self.assertIsNotNone(version_range)
        self.assertIsNotNone(version_range.min_version)
        self.assertIsNotNone(version_range.max_version)
        self.assertIsInstance(version_range.min_version, Version)
        self.assertIsInstance(version_range.max_version, Version)
        self.assertEqual(version_range.min_version.format(), Version(1).format())
        self.assertEqual(version_range.max_version.format(), Version(2).format())
        self.assertEqual(version_range.min_version.to_tuple(), Version(1).to_tuple())
        self.assertEqual(version_range.max_version.to_tuple(), Version(2).to_tuple())
        self.assertEqual(version_range.min_version.format(partitions=4), '1.0.0.0')
        self.assertEqual(version_range.max_version.format(partitions=4), '2.0.0.0')
        self.assertTrue(version_range.max_version.to_tuple() > version_range.min_version.to_tuple())
        self.assertTrue(version_range.max_version > version_range.min_version)

    def test_version_range_2(self):
        version_range = VersionRange(Version(major=100, minor=0, build=2), 101)
        self.assertIsNotNone(version_range)
        self.assertIsNotNone(version_range.min_version)
        self.assertIsNotNone(version_range.max_version)
        self.assertIsInstance(version_range.min_version, Version)
        self.assertIsInstance(version_range.max_version, Version)
        self.assertEqual(version_range.min_version.format(), Version(major=100, minor=0, build=2).format())
        self.assertEqual(version_range.max_version.format(), Version(101).format())
        self.assertEqual(version_range.min_version.to_tuple(), Version(major=100, minor=0, build=2).to_tuple())
        self.assertEqual(version_range.max_version.to_tuple(), Version(101).to_tuple())
        self.assertEqual(version_range.min_version.format(partitions=4), '100.0.2.0')
        self.assertEqual(version_range.max_version.format(partitions=4), '101.0.0.0')
        self.assertTrue(version_range.max_version.to_tuple() > version_range.min_version.to_tuple())
        self.assertTrue(version_range.max_version > version_range.min_version)

    def test_version_range_3(self):
        # MUST be valid version range
        chrome_min = 124
        chrome_max = 127

        for i in range(0, 100):
            options = Options(
                version_ranges={
                    'chrome': VersionRange(min_version=chrome_min, max_version=chrome_max),
                })
            ua = ua_generator.generate(browser='chrome', options=options)
            self.assertTrue(ua.browser == 'chrome')
            self.assertIsNotNone(ua.generator.browser_version)
            self.assertTrue(chrome_min <= ua.generator.browser_version.major <= chrome_max)

    def test_version_range_4(self):
        # MUST be valid version range
        firefox_min = 125
        firefox_max = 129

        for i in range(0, 100):
            options = Options(version_ranges={
                'firefox': VersionRange(min_version=firefox_min, max_version=firefox_max),
            })
            ua = ua_generator.generate(browser='firefox', options=options)
            self.assertTrue(ua.browser == 'firefox')
            self.assertIsNotNone(ua.generator.browser_version)
            self.assertTrue(firefox_min <= ua.generator.browser_version.major <= firefox_max)

    def test_version_range_multiple(self):
        # MUST be valid version range
        chrome_min = 124
        chrome_max = 127
        firefox_min = 125
        firefox_max = 129

        for i in range(0, 100):
            options = Options(version_ranges={
                'chrome': VersionRange(min_version=chrome_min, max_version=chrome_max),
                'firefox': VersionRange(min_version=firefox_min, max_version=firefox_max),
            })
            ua = ua_generator.generate(browser=('chrome', 'firefox'), options=options)
            self.assertIn(ua.browser, ('chrome', 'firefox'))
            self.assertIsNotNone(ua.generator.browser_version)
            if ua.browser == 'chrome':
                self.assertTrue(chrome_min <= ua.generator.browser_version.major <= chrome_max)
            if ua.browser == 'firefox':
                self.assertTrue(firefox_min <= ua.generator.browser_version.major <= firefox_max)

    def test_version_range_5(self):
        # MUST be valid version range
        macos_min = 12
        macos_max = 14

        for i in range(0, 100):
            options = Options(version_ranges={
                'macos': VersionRange(min_version=macos_min, max_version=macos_max),
            })
            ua = ua_generator.generate(platform='macos', options=options)
            self.assertTrue(ua.platform == 'macos')
            self.assertIsNotNone(ua.generator.platform_version)
            self.assertTrue(macos_min <= ua.generator.platform_version.major <= macos_max)

    def test_version_range_min_only(self):
        # MUST be valid version range
        chrome_min = 124

        for i in range(0, 100):
            options = Options(
                version_ranges={
                    'chrome': VersionRange(min_version=chrome_min),
                })
            ua = ua_generator.generate(browser='chrome', options=options)
            self.assertTrue(ua.browser == 'chrome')
            self.assertIsNotNone(ua.generator.browser_version)
            self.assertTrue(chrome_min <= ua.generator.browser_version.major)

    def test_version_range_max_only(self):
        # MUST be valid version range
        chrome_max = 125

        for i in range(0, 100):
            options = Options(
                version_ranges={
                    'chrome': VersionRange(max_version=chrome_max),
                })
            ua = ua_generator.generate(browser='chrome', options=options)
            self.assertTrue(ua.browser == 'chrome')
            self.assertIsNotNone(ua.generator.browser_version)
            self.assertTrue(ua.generator.browser_version.major <= chrome_max)

    def test_version_range_invalid(self):
        # MUST be INVALID version range
        edge_min = 1
        edge_max = 2

        for i in range(0, 100):
            options = Options(version_ranges={
                'edge': VersionRange(min_version=edge_min, max_version=edge_max),
            })
            ua = ua_generator.generate(browser='edge', options=options)
            self.assertTrue(ua.browser == 'edge')
            self.assertIsNotNone(ua.generator.browser_version)
            self.assertFalse(edge_min <= ua.generator.browser_version.major <= edge_max)


if __name__ == '__main__':
    unittest.main()
