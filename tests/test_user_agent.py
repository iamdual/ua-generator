"""
Random User-Agent
Copyright: 2022 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import re
import unittest

import src.ua_generator as ua_generator


class TestUserAgent(unittest.TestCase):
    def test_user_agent(self):
        for i in range(0, 100):
            ua = ua_generator.generate()
            self.assertIsNotNone(ua.device)
            self.assertIsNotNone(ua.platform)
            self.assertIsNotNone(ua.browser)
            self.assertIsNotNone(ua.text)

    def test_user_agent_2(self):
        for i in range(0, 100):
            ua = ua_generator.generate(platform=('ios', 'macos'), browser='safari')
            self.assertIsNotNone(ua.device)
            self.assertIsNotNone(ua.platform)
            self.assertIsNotNone(ua.browser)
            self.assertIsNotNone(ua.text)

    def test_user_agent_3(self):
        for i in range(0, 100):
            ua = ua_generator.generate(device='mobile', browser=('safari', 'chrome'))
            self.assertIsNotNone(ua.device)
            self.assertIsNotNone(ua.platform)
            self.assertIsNotNone(ua.browser)
            self.assertIsNotNone(ua.text)

    def test_user_agent_4(self):
        for i in range(0, 100):
            ua = ua_generator.generate(device='desktop', browser='firefox')
            self.assertIsNotNone(ua.device)
            self.assertIsNotNone(ua.platform)
            self.assertIsNotNone(ua.browser)
            self.assertIsNotNone(ua.text)

    def test_user_agent_5(self):
        for i in range(0, 1000):
            device = ('desktop', 'mobile')
            platform = ('windows', 'macos', 'ios', 'linux', 'android')
            browser = ('chrome', 'edge', 'firefox', 'safari')
            ua = ua_generator.generate(device=device, browser=browser, platform=platform)
            self.assertIsNotNone(ua.device)
            self.assertIsNotNone(ua.platform)
            self.assertIsNotNone(ua.browser)
            self.assertIsNotNone(ua.text)

    def test_user_agent_not_contains_brackets(self):
        brackets = re.compile('{(d|s|v|build|chrome|firefox|safari|webkit|windows|android|ios|macos|linux)}')
        for i in range(0, 200):
            ua = ua_generator.generate()
            self.assertNotRegex(ua.text, brackets)


if __name__ == '__main__':
    unittest.main()
