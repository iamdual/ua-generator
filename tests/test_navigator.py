"""
Random User-Agent
Copyright: 2022-2025 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import unittest

import src.ua_generator as ua_generator


class TestNavigator(unittest.TestCase):
    def test_get(self):
        ua = ua_generator.generate()
        self.assertIsNotNone(ua.navigator)

        navigator = ua.navigator.get()

        self.assertTrue('brands' in navigator)
        self.assertEqual(navigator['brands'], ua.navigator.brands)
        self.assertTrue('mobile' in navigator)
        self.assertEqual(navigator['mobile'], ua.navigator.mobile)
        self.assertTrue('platform' in navigator)
        self.assertEqual(navigator['platform'], ua.navigator.platform)

    def test_return_types(self):
        ua = ua_generator.generate()
        self.assertTrue(isinstance(ua.navigator.brands, list))
        self.assertTrue(isinstance(ua.navigator.mobile, bool))
        self.assertTrue(isinstance(ua.navigator.platform, str))
        self.assertTrue(isinstance(ua.navigator.architecture, str))
        self.assertTrue(isinstance(ua.navigator.bitness, str))
        self.assertTrue(isinstance(ua.navigator.formFactors, list))
        self.assertTrue(isinstance(ua.navigator.fullVersionList, list))
        self.assertTrue(isinstance(ua.navigator.model, str))
        self.assertTrue(isinstance(ua.navigator.platformVersion, str))
        self.assertTrue(isinstance(ua.navigator.wow64, bool))

if __name__ == '__main__':
    unittest.main()
