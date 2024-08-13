"""
Random User-Agent
Copyright: 2022 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import unittest

import src.ua_generator as ua_generator


class TestPlatform(unittest.TestCase):
    def test_platform(self):
        for i in range(0, 100):
            ua = ua_generator.generate(platform=('linux',))
            self.assertTrue(ua.platform == 'linux')

    def test_platform_2(self):
        for i in range(0, 100):
            ua = ua_generator.generate(platform=('windows', 'macos'))
            self.assertTrue(ua.platform == 'windows' or ua.platform == 'macos')

    def test_platform_3(self):
        for i in range(0, 100):
            ua = ua_generator.generate(platform='macos')
            self.assertTrue(ua.platform == 'macos')

    def test_platform_4(self):
        for i in range(0, 100):
            ua = ua_generator.generate(device='mobile')
            self.assertTrue(ua.platform == 'ios' or ua.platform == 'android')

    def test_platform_5(self):
        for i in range(0, 100):
            ua = ua_generator.generate(device='desktop')
            self.assertTrue(ua.platform == 'windows' or ua.platform == 'macos' or ua.platform == 'linux')

    def test_platform_6(self):
        for i in range(0, 100):
            ua = ua_generator.generate(device='desktop', platform='ios')
            self.assertNotEqual(ua.device, 'desktop')
            self.assertEqual(ua.platform, 'ios')

    def test_platform_7(self):
        for i in range(0, 100):
            ua = ua_generator.generate(device='desktop', platform='android')
            self.assertNotEqual(ua.device, 'desktop')
            self.assertEqual(ua.platform, 'android')

    def test_platform_8(self):
        for i in range(0, 100):
            ua = ua_generator.generate(device='mobile', platform='windows')
            self.assertNotEqual(ua.device, 'mobile')
            self.assertEqual(ua.platform, 'windows')

    def test_platform_9(self):
        for i in range(0, 100):
            ua = ua_generator.generate(device='mobile', platform='macos')
            self.assertNotEqual(ua.device, 'mobile')
            self.assertEqual(ua.platform, 'macos')


if __name__ == '__main__':
    unittest.main()
