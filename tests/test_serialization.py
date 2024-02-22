"""
Random User-Agent
Copyright: 2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import unittest

from src.ua_generator import serialization


class TestSerialization(unittest.TestCase):
    def test_ch_brand_list(self):
        brand_list = [
            {'brand': 'Not A(Brand', 'version': '99'},
            {'brand': 'UA-Generator', 'version': '0'},
        ]
        self.assertEqual(serialization.ch_brand_list(brand_list), '"Not A(Brand";v="99", "UA-Generator";v="0"')

    def test_ch_bool(self):
        self.assertEqual(serialization.ch_bool(True), '?1')
        self.assertEqual(serialization.ch_bool(False), '?0')

    def test_ch_string(self):
        self.assertEqual(serialization.ch_string('foo'), '"foo"')


if __name__ == '__main__':
    unittest.main()
