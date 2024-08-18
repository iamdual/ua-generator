"""
Random User-Agent
Copyright: 2022 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import unittest

import src.ua_generator as ua_generator
from src.ua_generator.data import BROWSERS_SUPPORT_CH


class TestHeaders(unittest.TestCase):
    def test_default(self):
        for i in range(0, 100):
            ua = ua_generator.generate()
            self.assertIsNotNone(ua.headers)
            self.assertTrue('user-agent' in ua.headers.get())

    def test_client_hints(self):
        for i in range(0, 100):
            ua = ua_generator.generate(browser=BROWSERS_SUPPORT_CH)
            self.assertIsNotNone(ua.headers)
            self.assertTrue('sec-ch-ua' in ua.headers.get())
            self.assertTrue('sec-ch-ua-mobile' in ua.headers.get())
            self.assertTrue('sec-ch-ua-platform' in ua.headers.get())

    def test_client_hints_not_exists(self):
        for i in range(0, 100):
            ua = ua_generator.generate(browser='firefox')
            self.assertIsNotNone(ua.headers)
            self.assertFalse('sec-ch-ua' in ua.headers.get())
            self.assertFalse('sec-ch-ua-mobile' in ua.headers.get())
            self.assertFalse('sec-ch-ua-platform' in ua.headers.get())

    def test_accept_ch(self):
        for i in range(0, 100):
            ua = ua_generator.generate(browser=BROWSERS_SUPPORT_CH)

            ua.headers.accept_ch('Sec-CH-UA-Platform-Version, Sec-CH-UA-Full-Version-List')
            self.assertTrue('sec-ch-ua-platform-version' in ua.headers.get())
            self.assertTrue('sec-ch-ua-full-version-list' in ua.headers.get())

            ua.headers.accept_ch('Sec-CH-UA-Bitness, Sec-CH-UA-Arch')
            self.assertTrue('sec-ch-ua-bitness' in ua.headers.get())
            self.assertTrue('sec-ch-ua-arch' in ua.headers.get())
            self.assertFalse('sec-ch-ua-platform-version' in ua.headers.get())
            self.assertFalse('sec-ch-ua-full-version-list' in ua.headers.get())

            ua.headers.accept_ch('Sec-CH-UA-Model, Sec-CH-UA-WoW64')
            self.assertTrue('sec-ch-ua-model' in ua.headers.get())
            self.assertTrue('sec-ch-ua-wow64' in ua.headers.get())

    def test_reset(self):
        for i in range(0, 100):
            ua = ua_generator.generate(browser=BROWSERS_SUPPORT_CH)

            ua.headers.add('sec-ch-ua-bitness')
            self.assertTrue('user-agent' in ua.headers.get())
            self.assertTrue('sec-ch-ua' in ua.headers.get())
            self.assertTrue('sec-ch-ua-bitness' in ua.headers.get())

            ua.headers.reset()
            self.assertTrue('user-agent' in ua.headers.get())
            self.assertTrue('sec-ch-ua' in ua.headers.get())
            self.assertFalse('sec-ch-ua-bitness' in ua.headers.get())

    def test_accept_ch_not_exists(self):
        for i in range(0, 100):
            ua = ua_generator.generate(browser=BROWSERS_SUPPORT_CH)
            ua.headers.accept_ch('Sec-CH-Example')
            self.assertFalse('sec-ch-ua-platform-version' in ua.headers.get())
            self.assertFalse('sec-ch-ua-full-version-list' in ua.headers.get())


if __name__ == '__main__':
    unittest.main()
