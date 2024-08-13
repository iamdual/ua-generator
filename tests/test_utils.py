"""
Random User-Agent
Copyright: 2022 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import unittest

from src.ua_generator import utils


class TestUtils(unittest.TestCase):
    def test_choice(self):
        self.assertEqual(utils.choice('mobile'), 'mobile')
        self.assertEqual(utils.choice(('mobile', 'mobile')), 'mobile')
        self.assertEqual(utils.choice(['mobile', 'mobile']), 'mobile')
        self.assertEqual(utils.choice(None), None)
        self.assertEqual(utils.choice(111), None)


if __name__ == '__main__':
    unittest.main()
