"""
Random User-Agent
Copyright: 2022 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import unittest

import src.ua_generator as ua_generator
from src.ua_generator import exceptions


def raised_call():
    ua_generator.generate(device='desktop', platform='invalid111')


def raised_call_2():
    ua_generator.generate(browser=('invalid111', 'invalid112'))


def raised_call_3():
    ua_generator.generate(device='invalid111', platform='android', browser='chrome')


def raised_call_4():
    for i in range(0, 100):
        ua_generator.generate(device=('desktop', 'invalid111'))


def raised_call_5():
    for i in range(0, 100):
        ua_generator.generate(platform=('invalid111', 'macos'))


def raised_call_6():
    for i in range(0, 100):
        ua_generator.generate(browser=('invalid111', 'chrome'))


def raised_call_7():
    ua = ua_generator.generate()
    return ua.ch.invalid111


class TestExceptions(unittest.TestCase):
    def test_value_error(self):
        self.assertRaises(exceptions.InvalidArgumentError, raised_call)

    def test_value_error_2(self):
        self.assertRaises(exceptions.InvalidArgumentError, raised_call_2)

    def test_value_error_3(self):
        self.assertRaises(exceptions.InvalidArgumentError, raised_call_3)

    def test_value_error_4(self):
        self.assertRaises(exceptions.InvalidArgumentError, raised_call_4)

    def test_value_error_5(self):
        self.assertRaises(exceptions.InvalidArgumentError, raised_call_5)

    def test_value_error_6(self):
        self.assertRaises(exceptions.InvalidArgumentError, raised_call_6)

    def test_value_error_7(self):
        self.assertRaises(exceptions.InvalidArgumentError, raised_call_7)


if __name__ == '__main__':
    unittest.main()
