"""
Random User-Agent
Copyright: 2022 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import unittest

import src.ua_generator as ua_generator


class TestBrowser(unittest.TestCase):
    def test_browser(self):
        for i in range(0, 100):
            ua = ua_generator.generate(browser=('chrome',))
            self.assertTrue(ua.browser == 'chrome')

    def test_browser_2(self):
        for i in range(0, 100):
            ua = ua_generator.generate(browser=('chrome', 'firefox'))
            self.assertTrue(ua.browser == 'chrome' or ua.browser == 'firefox')

    def test_browser_3(self):
        for i in range(0, 100):
            ua = ua_generator.generate(platform=('macos', 'ios'), browser='safari')
            self.assertTrue(ua.browser == 'safari')

    def test_browser_4(self):
        for i in range(0, 100):
            ua = ua_generator.generate(platform=('windows', 'linux'), browser='safari')
            self.assertTrue(ua.browser == 'chrome')

    def test_browser_5(self):
        for i in range(0, 100):
            ua = ua_generator.generate(platform=('macos', 'linux'), browser='safari')
            self.assertTrue((ua.platform == 'macos' and ua.browser == 'safari') or
                            (ua.platform == 'linux' and ua.browser == 'chrome'))


if __name__ == '__main__':
    unittest.main()
