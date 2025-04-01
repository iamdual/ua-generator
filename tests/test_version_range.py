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
        CHROME_MIN = 124
        CHROME_MAX = 127

        for i in range(0, 100):
            options = Options(
                version_ranges={
                    'chrome': VersionRange(min_version=CHROME_MIN, max_version=CHROME_MAX),
                })
            ua = ua_generator.generate(browser='chrome', options=options)
            self.assertTrue(ua.browser == 'chrome')
            self.assertIsNotNone(ua.generator.browser_version)
            self.assertTrue(CHROME_MIN <= ua.generator.browser_version.major <= CHROME_MAX)

    def test_version_range_4(self):
        # MUST be valid version range
        FIREFOX_MIN = 125
        FIREFOX_MAX = 129

        for i in range(0, 100):
            options = Options(version_ranges={
                'firefox': VersionRange(min_version=FIREFOX_MIN, max_version=FIREFOX_MAX),
            })
            ua = ua_generator.generate(browser='firefox', options=options)
            self.assertTrue(ua.browser == 'firefox')
            self.assertIsNotNone(ua.generator.browser_version)
            self.assertTrue(FIREFOX_MIN <= ua.generator.browser_version.major <= FIREFOX_MAX)

    def test_version_range_multiple(self):
        # MUST be valid version range
        CHROME_MIN = 124
        CHROME_MAX = 127
        FIREFOX_MIN = 125
        FIREFOX_MAX = 129

        for i in range(0, 100):
            options = Options(version_ranges={
                'chrome': VersionRange(min_version=CHROME_MIN, max_version=CHROME_MAX),
                'firefox': VersionRange(min_version=FIREFOX_MIN, max_version=FIREFOX_MAX),
            })
            ua = ua_generator.generate(browser=('chrome', 'firefox'), options=options)
            self.assertIn(ua.browser, ('chrome', 'firefox'))
            self.assertIsNotNone(ua.generator.browser_version)
            if ua.browser == 'chrome':
                self.assertTrue(CHROME_MIN <= ua.generator.browser_version.major <= CHROME_MAX)
            if ua.browser == 'firefox':
                self.assertTrue(FIREFOX_MIN <= ua.generator.browser_version.major <= FIREFOX_MAX)

    def test_version_range_5(self):
        # MUST be valid version range
        MACOS_MIN = 12
        MACOS_MAX = 14

        for i in range(0, 100):
            options = Options(version_ranges={
                'macos': VersionRange(min_version=MACOS_MIN, max_version=MACOS_MAX),
            })
            ua = ua_generator.generate(platform='macos', options=options)
            self.assertTrue(ua.platform == 'macos')
            self.assertIsNotNone(ua.generator.platform_version)
            self.assertTrue(MACOS_MIN <= ua.generator.platform_version.major <= MACOS_MAX)

    def test_version_range_min_only(self):
        # MUST be valid version range
        CHROME_MIN = 124

        for i in range(0, 100):
            options = Options(
                version_ranges={
                    'chrome': VersionRange(min_version=CHROME_MIN),
                })
            ua = ua_generator.generate(browser='chrome', options=options)
            self.assertTrue(ua.browser == 'chrome')
            self.assertIsNotNone(ua.generator.browser_version)
            self.assertTrue(CHROME_MIN <= ua.generator.browser_version.major)

    def test_version_range_max_only(self):
        # MUST be valid version range
        CHROME_MAX = 125

        for i in range(0, 100):
            options = Options(
                version_ranges={
                    'chrome': VersionRange(max_version=CHROME_MAX),
                })
            ua = ua_generator.generate(browser='chrome', options=options)
            self.assertTrue(ua.browser == 'chrome')
            self.assertIsNotNone(ua.generator.browser_version)
            self.assertTrue(ua.generator.browser_version.major <= CHROME_MAX)

    def test_version_range_invalid(self):
        # MUST be INVALID version range
        EDGE_MIN_INVALID = 1
        EDGE_MAX_INVALID = 2

        for i in range(0, 100):
            options = Options(version_ranges={
                'edge': VersionRange(min_version=EDGE_MIN_INVALID, max_version=EDGE_MAX_INVALID),
            })
            ua = ua_generator.generate(browser='edge', options=options)
            self.assertTrue(ua.browser == 'edge')
            self.assertIsNotNone(ua.generator.browser_version)
            self.assertFalse(EDGE_MIN_INVALID <= ua.generator.browser_version.major <= EDGE_MAX_INVALID)


if __name__ == '__main__':
    unittest.main()
