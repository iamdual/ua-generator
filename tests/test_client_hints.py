"""
Random User-Agent
Copyright: 2022 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import unittest

import src.ua_generator as ua_generator
from src.ua_generator.data import browsers_support_ch


class TestClientHints(unittest.TestCase):
    def test_ch_platform(self):
        for i in range(0, 100):
            ua = ua_generator.generate(browser=browsers_support_ch, platform='macos')
            self.assertIsNotNone(ua.ch)
            self.assertEqual(ua.ch.platform, '"macOS"')

    def test_ch_platform_2(self):
        for i in range(0, 100):
            ua = ua_generator.generate(browser=browsers_support_ch, platform='linux')
            self.assertIsNotNone(ua.ch)
            self.assertEqual(ua.ch.platform, '"Linux"')

    def test_ch_platform_version(self):
        for i in range(0, 100):
            ua = ua_generator.generate(browser=browsers_support_ch)
            self.assertIsNotNone(ua.ch)
            self.assertTrue(type(ua.ch.platform_version) is str)
            self.assertTrue(len(ua.ch.platform_version) > 0)

    def test_ch_platform_version_windows(self):
        for i in range(0, 100):
            ua = ua_generator.generate(platform='windows')
            self.assertIsNotNone(ua.ch)
            self.assertTrue(type(ua.ch.platform_version) is str)
            self.assertEqual(len(ua.ch.platform_version.split('.')), 3)

    def test_ch_mobile(self):
        for i in range(0, 100):
            ua = ua_generator.generate(browser=browsers_support_ch, platform='android')
            self.assertIsNotNone(ua.ch)
            self.assertEqual(ua.ch.mobile, '?1')

    def test_ch_non_mobile(self):
        for i in range(0, 100):
            ua = ua_generator.generate(browser=browsers_support_ch, platform='windows')
            self.assertIsNotNone(ua.ch)
            self.assertEqual(ua.ch.mobile, '?0')

    def test_ch_brands(self):
        for i in range(0, 100):
            ua = ua_generator.generate(browser='chrome', platform='windows')
            self.assertIsNotNone(ua.ch)
            self.assertTrue(ua.ch.brands.startswith('"Not A(Brand";v="99"'))
            self.assertTrue('Chromium' in ua.ch.brands)
            self.assertTrue('Google Chrome' in ua.ch.brands)

    def test_ch_brands_full_version_list(self):
        for i in range(0, 100):
            ua = ua_generator.generate(browser='edge', platform='windows')
            self.assertIsNotNone(ua.ch)
            self.assertTrue(ua.ch.brands_full_version_list.startswith('"Not A(Brand";v="99"'))
            self.assertTrue('Chromium' in ua.ch.brands_full_version_list)
            self.assertTrue('Microsoft Edge' in ua.ch.brands_full_version_list)

    def test_ch_bitness(self):
        for i in range(0, 100):
            ua = ua_generator.generate(browser=browsers_support_ch)
            self.assertIsNotNone(ua.ch)
            self.assertIn(ua.ch.bitness, ('"32"', '"64"'))

    def test_ch_architecture(self):
        for i in range(0, 100):
            ua = ua_generator.generate(browser=browsers_support_ch)
            self.assertIsNotNone(ua.ch)
            self.assertIn(ua.ch.architecture, ('"arm"', '"x86"'))

    def test_ch_model(self):
        for i in range(0, 100):
            ua = ua_generator.generate(platform='android', browser='chrome')
            self.assertIsNotNone(ua.ch)
            self.assertTrue(ua.ch.model != '')


if __name__ == '__main__':
    unittest.main()
