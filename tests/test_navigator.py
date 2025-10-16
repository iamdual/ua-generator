"""
Random User-Agent
Copyright: 2022-2025 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import unittest

import src.ua_generator as ua_generator


class TestNavigator(unittest.TestCase):
    def test_navigator(self):
        ua = ua_generator.generate()
        self.assertIsNotNone(ua.navigator)
        navigator = ua.navigator.get()

        self.assertTrue('brands' in navigator)
        self.assertEqual(navigator['brands'], ua.navigator.brands)
        self.assertTrue(isinstance(ua.navigator.brands, list))

        self.assertTrue('mobile' in navigator)
        self.assertEqual(navigator['mobile'], ua.navigator.mobile)
        self.assertTrue(isinstance(ua.navigator.mobile, bool))

        self.assertTrue('platform' in navigator)
        self.assertEqual(navigator['platform'], ua.navigator.platform)
        self.assertTrue(isinstance(ua.navigator.platform, str))


if __name__ == '__main__':
    unittest.main()
