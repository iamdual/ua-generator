"""
Random User-Agent
Copyright: 2022 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import unittest

import src.ua_generator as ua_generator
from src.ua_generator import serialization
from src.ua_generator.data import BROWSERS_SUPPORT_CH


class TestClientHints(unittest.TestCase):
    def test_ch_platform(self):
        for i in range(0, 100):
            ua = ua_generator.generate(browser=BROWSERS_SUPPORT_CH, platform='macos')
            self.assertIsNotNone(ua.ch)
            self.assertTrue(type(ua.ch.platform) is str)
            self.assertEqual(ua.ch.platform, '"macOS"')
            self.assertEqual(ua.ch.get_platform(), 'macOS')

    def test_ch_platform_2(self):
        for i in range(0, 100):
            ua = ua_generator.generate(browser=BROWSERS_SUPPORT_CH, platform='linux')
            self.assertIsNotNone(ua.ch)
            self.assertTrue(type(ua.ch.platform) is str)
            self.assertEqual(ua.ch.platform, '"Linux"')
            self.assertEqual(ua.ch.get_platform(), 'Linux')

    def test_ch_platform_version(self):
        for i in range(0, 100):
            ua = ua_generator.generate(browser=BROWSERS_SUPPORT_CH)
            self.assertIsNotNone(ua.ch)
            self.assertTrue(type(ua.ch.platform_version) is str)
            self.assertEqual(ua.ch.platform_version, serialization.ch_string(ua.ch.get_platform_version()))

    def test_ch_platform_version_windows(self):
        for i in range(0, 100):
            ua = ua_generator.generate(platform='windows')
            self.assertIsNotNone(ua.ch)
            self.assertTrue(type(ua.ch.platform_version) is str)
            self.assertEqual(ua.ch.platform_version, serialization.ch_string(ua.ch.get_platform_version()))

    def test_ch_mobile(self):
        for i in range(0, 100):
            ua = ua_generator.generate(browser=BROWSERS_SUPPORT_CH, platform='android')
            self.assertIsNotNone(ua.ch)
            self.assertTrue(type(ua.ch.mobile) is str)
            self.assertEqual(ua.ch.mobile, '?1')
            self.assertTrue(type(ua.ch.get_mobile()) is bool)
            self.assertEqual(ua.ch.get_mobile(), True)
            self.assertTrue(ua.ch.model is not None and ua.ch.model != "")
            self.assertTrue(ua.ch.get_model() is not None and ua.ch.get_model() != "")

    def test_ch_non_mobile(self):
        for i in range(0, 100):
            ua = ua_generator.generate(browser=BROWSERS_SUPPORT_CH, platform='windows')
            self.assertIsNotNone(ua.ch)
            self.assertTrue(type(ua.ch.mobile) is str)
            self.assertEqual(ua.ch.mobile, '?0')
            self.assertTrue(type(ua.ch.get_mobile()) is bool)
            self.assertEqual(ua.ch.get_mobile(), False)

    def test_ch_brands(self):
        for i in range(0, 100):
            ua = ua_generator.generate(browser='chrome', platform='windows')
            self.assertIsNotNone(ua.ch)
            self.assertTrue(type(ua.ch.brands) is str)
            self.assertTrue(ua.ch.brands.startswith('"Not A(Brand";v="99"'))
            self.assertTrue('Chromium' in ua.ch.brands)
            self.assertTrue('Google Chrome' in ua.ch.brands)
            self.assertTrue(type(ua.ch.get_brands()) is list)
            self.assertEqual(ua.ch.brands, serialization.ch_brand_list(ua.ch.get_brands()))

    def test_ch_brands_full_version_list(self):
        for i in range(0, 100):
            ua = ua_generator.generate(browser='edge', platform='windows')
            self.assertIsNotNone(ua.ch)
            self.assertTrue(type(ua.ch.brands_full_version_list) is str)
            self.assertTrue(ua.ch.brands_full_version_list.startswith('"Not A(Brand";v="99.0.0.0"'))
            self.assertTrue('Chromium' in ua.ch.brands_full_version_list)
            self.assertTrue('Microsoft Edge' in ua.ch.brands_full_version_list)
            self.assertTrue(type(ua.ch.get_brands(full_version_list=True)) is list)
            self.assertEqual(ua.ch.brands_full_version_list, serialization.ch_brand_list(ua.ch.get_brands(full_version_list=True)))

    def test_ch_bitness(self):
        for i in range(0, 100):
            ua = ua_generator.generate(browser=BROWSERS_SUPPORT_CH)
            self.assertIsNotNone(ua.ch)
            self.assertTrue(type(ua.ch.bitness) is str)
            self.assertIn(ua.ch.bitness, ('"32"', '"64"'))
            self.assertIn(ua.ch.get_bitness(), ('32', '64'))

    def test_ch_architecture(self):
        for i in range(0, 100):
            ua = ua_generator.generate(browser=BROWSERS_SUPPORT_CH)
            self.assertIsNotNone(ua.ch)
            self.assertTrue(type(ua.ch.architecture) is str)
            self.assertIn(ua.ch.architecture, ('"arm"', '"x86"'))
            self.assertIn(ua.ch.get_architecture(), ('arm', 'x86'))

    def test_ch_model(self):
        for i in range(0, 100):
            ua = ua_generator.generate(platform='android', browser='chrome')
            self.assertIsNotNone(ua.ch)
            self.assertTrue(type(ua.ch.model) is str)
            self.assertTrue(ua.ch.model != '""')
            self.assertTrue(len(ua.ch.model) > 2)
            self.assertEqual(ua.ch.model, serialization.ch_string(ua.ch.get_model()))

    def test_ch_model_2(self):
        for i in range(0, 100):
            ua = ua_generator.generate(platform='linux', browser='firefox')
            self.assertIsNotNone(ua.ch)
            self.assertTrue(type(ua.ch.model) is str)
            self.assertTrue(ua.ch.model == '""')
            self.assertEqual(ua.ch.model, serialization.ch_string(ua.ch.get_model()))

    def test_ch_wow64(self):
        for i in range(0, 100):
            ua = ua_generator.generate(platform='windows')
            self.assertIsNotNone(ua.ch)
            self.assertTrue(type(ua.ch.wow64) is str)
            self.assertEqual(ua.ch.wow64, '?1')
            self.assertTrue(type(ua.ch.get_wow64()) is bool)
            self.assertEqual(ua.ch.get_wow64(), True)

    def test_ch_wow64_2(self):
        for i in range(0, 100):
            ua = ua_generator.generate(platform='linux')
            self.assertIsNotNone(ua.ch)
            self.assertTrue(type(ua.ch.wow64) is str)
            self.assertEqual(ua.ch.wow64, '?0')
            self.assertTrue(type(ua.ch.get_wow64()) is bool)
            self.assertEqual(ua.ch.get_wow64(), False)


if __name__ == '__main__':
    unittest.main()
