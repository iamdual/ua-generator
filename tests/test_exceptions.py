"""
Random User-Agent
Copyright: 2022 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import unittest

import src.ua_generator as ua_generator
from src.ua_generator import exceptions


def raised_call():
    ua_generator.generate(device='desktop', platform='commodore_64')


def raised_call_2():
    ua_generator.generate(browser=('netscape', 'ie'))


class TestExceptions(unittest.TestCase):
    def test_value_error(self):
        self.assertRaises(exceptions.InvalidArgumentError, raised_call)

    def test_value_error_2(self):
        self.assertRaises(exceptions.InvalidArgumentError, raised_call_2)


if __name__ == '__main__':
    unittest.main()
