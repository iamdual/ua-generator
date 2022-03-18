"""
Random User-Agent
Copyright: 2022 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import unittest

from src.ua_generator import utils


class TestUtils(unittest.TestCase):
    def test_contains(self):
        self.assertTrue(utils.contains(('mobile', 'desktop'), 'mobile'))

    def test_contains_2(self):
        self.assertTrue(utils.contains(('mobile', 'desktop'), 'desktop'))

    def test_contains_3(self):
        self.assertTrue(utils.contains('desktop', 'desktop'))

    def test_contains_4(self):
        self.assertFalse(utils.contains(('mobile', 'desktop'), 'ebook'))

    def test_contains_5(self):
        self.assertFalse(utils.contains('desktop', 'ebook'))

    def test_contains_multiple(self):
        self.assertTrue(utils.contains_multiple(('mobile', 'desktop'), ['mobile', 'desktop']))

    def test_contains_multiple_2(self):
        self.assertTrue(utils.contains_multiple(('mobile', 'desktop'), ['ebook', 'desktop']))

    def test_contains_multiple_3(self):
        self.assertTrue(utils.contains_multiple(['mobile', 'desktop'], ['ebook', 'mobile']))

    def test_contains_multiple_4(self):
        self.assertTrue(utils.contains_multiple('desktop', ('ebook', 'desktop')))

    def test_contains_multiple_5(self):
        self.assertTrue(utils.contains_multiple('desktop', ('ebook', 'desktop')))

    def test_contains_multiple_6(self):
        self.assertFalse(utils.contains_multiple(['mobile', 'desktop'], ['ebook', 'gameboy']))

    def test_contains_multiple_7(self):
        self.assertFalse(utils.contains_multiple('mobile', ['ebook', 'gameboy']))


if __name__ == '__main__':
    unittest.main()
