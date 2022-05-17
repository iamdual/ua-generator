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
            self.assertTrue(ua.ch.platform, 'macOS')

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

    def test_ch_versions(self):
        for i in range(0, 100):
            ua = ua_generator.generate(browser='chrome', platform='windows')
            self.assertIsNotNone(ua.ch)
            self.assertTrue(ua.ch.versions.startswith('" Not A;Brand";v="99", "Chromium";v="'))

    def test_ch_full_versions(self):
        for i in range(0, 100):
            ua = ua_generator.generate(browser='chrome', platform='windows')
            self.assertIsNotNone(ua.ch)
            self.assertTrue(ua.ch.full_versions.startswith('" Not A;Brand";v="99", "Chromium";v="'))


if __name__ == '__main__':
    unittest.main()
