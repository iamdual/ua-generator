"""
Random User-Agent
Copyright: 2022 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import unittest

import src.ua_generator as ua_generator


class TestUserAgent(unittest.TestCase):
    def test_user_agent(self):
        for i in range(0, 100):
            ua = ua_generator.generate()
            self.assertIsNotNone(ua.text)
            self.assertIsNotNone(ua.device)
            self.assertIsNotNone(ua.platform)
            self.assertIsNotNone(ua.platform_version)
            self.assertIsNotNone(ua.browser)
            self.assertIsNotNone(ua.browser_version)

    def test_user_agent_2(self):
        for i in range(0, 100):
            ua = ua_generator.generate(platform=('ios', 'macos'), browser='safari')
            self.assertIsNotNone(ua.text)
            self.assertIsNotNone(ua.device)
            self.assertIsNotNone(ua.platform)
            self.assertIsNotNone(ua.platform_version)
            self.assertIsNotNone(ua.browser)
            self.assertIsNotNone(ua.browser_version)

    def test_user_agent_3(self):
        for i in range(0, 100):
            ua = ua_generator.generate(device='mobile', browser=('safari', 'chrome'))
            self.assertIsNotNone(ua.text)
            self.assertIsNotNone(ua.device)
            self.assertIsNotNone(ua.platform)
            self.assertIsNotNone(ua.platform_version)
            self.assertIsNotNone(ua.browser)
            self.assertIsNotNone(ua.browser_version)

    def test_user_agent_4(self):
        for i in range(0, 100):
            ua = ua_generator.generate(device='desktop', browser='firefox')
            self.assertIsNotNone(ua.text)
            self.assertIsNotNone(ua.device)
            self.assertIsNotNone(ua.platform)
            self.assertIsNotNone(ua.platform_version)
            self.assertIsNotNone(ua.browser)
            self.assertIsNotNone(ua.browser_version)


if __name__ == '__main__':
    unittest.main()
