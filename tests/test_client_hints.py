"""
Random User-Agent
Copyright: 2022 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import unittest

import src.ua_generator as ua_generator


class TestClientHints(unittest.TestCase):
    def test_ch_platform(self):
        for i in range(0, 100):
            ua = ua_generator.generate(browser='chrome', platform='macos')
            self.assertIsNotNone(ua.ch)
            self.assertEqual(ua.ch.platform, '"macOS"')

    def test_ch_platform_2(self):
        for i in range(0, 100):
            ua = ua_generator.generate(browser='chrome', platform='linux')
            self.assertIsNotNone(ua.ch)
            self.assertEqual(ua.ch.platform, '"Linux"')

    def test_ch_platform_version(self):
        for i in range(0, 100):
            ua = ua_generator.generate(browser='chrome')
            self.assertIsNotNone(ua.ch)
            self.assertTrue(type(ua.ch.platform_version) is str)
            self.assertTrue(len(ua.ch.platform_version) > 0)

    def test_ch_mobile(self):
        for i in range(0, 100):
            ua = ua_generator.generate(browser='chrome', platform='android')
            self.assertIsNotNone(ua.ch)
            self.assertEqual(ua.ch.mobile, '?1')

    def test_ch_non_mobile(self):
        for i in range(0, 100):
            ua = ua_generator.generate(browser='chrome', platform='windows')
            self.assertIsNotNone(ua.ch)
            self.assertEqual(ua.ch.mobile, '?0')

    def test_ch_brands(self):
        for i in range(0, 100):
            ua = ua_generator.generate(browser='chrome', platform='windows')
            self.assertIsNotNone(ua.ch)
            self.assertTrue(ua.ch.brands.startswith('" Not A;Brand";v="99"'))
            self.assertTrue('Chromium' in ua.ch.brands)
            self.assertTrue('Google Chrome' in ua.ch.brands)

    def test_ch_brands_full_version_list(self):
        for i in range(0, 100):
            ua = ua_generator.generate(browser='edge', platform='windows')
            self.assertIsNotNone(ua.ch)
            self.assertTrue(ua.ch.brands_full_version_list.startswith('" Not A;Brand";v="99"'))
            self.assertTrue('Chromium' in ua.ch.brands_full_version_list)
            self.assertTrue('Microsoft Edge' in ua.ch.brands_full_version_list)


if __name__ == '__main__':
    unittest.main()