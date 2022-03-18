"""
Random User-Agent
Copyright: 2022 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import unittest

import src.ua_generator as ua_generator


class TestDevice(unittest.TestCase):
    def test_device(self):
        for i in range(0, 100):
            ua = ua_generator.generate(device=('desktop'))
            self.assertTrue(ua.device == 'desktop')

    def test_device_2(self):
        for i in range(0, 100):
            ua = ua_generator.generate(device=('desktop', 'mobile'))
            self.assertTrue(ua.device == 'desktop' or ua.device == 'mobile')

    def test_device_3(self):
        for i in range(0, 100):
            ua = ua_generator.generate(device='desktop')
            self.assertTrue(ua.device == 'desktop')

    def test_device_4(self):
        for i in range(0, 100):
            ua = ua_generator.generate(device='mobile')
            self.assertTrue(ua.device == 'mobile')

    def test_device_5(self):
        for i in range(0, 100):
            ua = ua_generator.generate(device='desktop')
            self.assertFalse(ua.device == 'mobile')

    def test_device_6(self):
        for i in range(0, 100):
            ua = ua_generator.generate(platform=('ios'))
            self.assertTrue(ua.device == 'mobile')

    def test_device_7(self):
        for i in range(0, 100):
            ua = ua_generator.generate(platform=('windows', 'macos'))
            self.assertTrue(ua.device == 'desktop')


if __name__ == '__main__':
    unittest.main()
