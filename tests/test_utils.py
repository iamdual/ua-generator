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
        self.assertTrue(utils.contains(('mobile', 'desktop'), 'desktop'))
        self.assertTrue(utils.contains('desktop', 'desktop'))
        self.assertFalse(utils.contains(('mobile', 'desktop'), 'ebook'))
        self.assertFalse(utils.contains('desktop', 'ebook'))

    def test_contains_multiple(self):
        self.assertTrue(utils.contains_multiple(('mobile', 'desktop'), ['mobile', 'desktop']))
        self.assertTrue(utils.contains_multiple(('mobile', 'desktop'), ['ebook', 'desktop']))
        self.assertTrue(utils.contains_multiple(['mobile', 'desktop'], ['ebook', 'mobile']))
        self.assertTrue(utils.contains_multiple('desktop', ('ebook', 'desktop')))
        self.assertTrue(utils.contains_multiple('desktop', ('ebook', 'desktop')))
        self.assertFalse(utils.contains_multiple(['mobile', 'desktop'], ['ebook', 'gameboy']))
        self.assertFalse(utils.contains_multiple('mobile', ['ebook', 'gameboy']))


if __name__ == '__main__':
    unittest.main()
