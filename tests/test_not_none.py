"""
Random User-Agent
Copyright: 2022 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import unittest

import src.ua_generator as ua_generator


class TestNotNone(unittest.TestCase):
    def test_text(self):
        for i in range(0, 100):
            ua = ua_generator.generate()
            self.assertTrue(ua.text is not None)

    def test_device(self):
        for i in range(0, 100):
            ua = ua_generator.generate(device=('desktop', 'mobile'))
            self.assertTrue(ua.device is not None)

    def test_device_2(self):
        for i in range(0, 100):
            ua = ua_generator.generate()
            self.assertTrue(ua.device is not None)

    def test_platform(self):
        for i in range(0, 100):
            ua = ua_generator.generate(device='desktop', platform=('windows', 'macos'))
            self.assertTrue(ua.platform is not None)
            self.assertTrue(ua.platform_version is not None)

    def test_platform_2(self):
        for i in range(0, 100):
            ua = ua_generator.generate(browser=('chrome', 'firefox'))
            self.assertTrue(ua.platform is not None)
            self.assertTrue(ua.platform_version is not None)

    def test_browser(self):
        for i in range(0, 100):
            ua = ua_generator.generate(device='desktop', platform=('windows', 'macos'))
            self.assertTrue(ua.browser is not None)
            self.assertTrue(ua.browser_version is not None)

    def test_browser_2(self):
        for i in range(0, 100):
            ua = ua_generator.generate(device='mobile', platform=('windows', 'linux'))
            self.assertTrue(ua.browser is not None)
            self.assertTrue(ua.browser_version is not None)

    def test_platform_6(self):
        for i in range(0, 100):
            ua = ua_generator.generate(platform='android', browser='chrome')
            self.assertTrue(ua.browser is not None)
            self.assertTrue(ua.browser_version is not None)

if __name__ == '__main__':
    unittest.main()
