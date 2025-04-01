"""
Random User-Agent
Copyright: 2022 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import unittest

import src.ua_generator as ua_generator
from src.ua_generator.data.browsers.chrome import versions as chrome_versions
from src.ua_generator.data.filterer import Filterer


class TestExceptions(unittest.TestCase):
    def test_value_error(self):
        def raised_call():
            ua_generator.generate(device='desktop', platform='invalid111')

        self.assertRaises(ValueError, raised_call)

    def test_value_error_2(self):
        def raised_call():
            ua_generator.generate(browser=('invalid111', 'invalid112'))

        self.assertRaises(ValueError, raised_call)

    def test_value_error_3(self):
        def raised_call():
            ua_generator.generate(device='invalid111', platform='android', browser='chrome')

        self.assertRaises(ValueError, raised_call)

    def test_value_error_4(self):
        def raised_call():
            for i in range(0, 100):
                ua_generator.generate(device=('desktop', 'invalid111'))

        self.assertRaises(ValueError, raised_call)

    def test_value_error_5(self):
        def raised_call():
            for i in range(0, 100):
                ua_generator.generate(platform=('invalid111', 'macos'))

        self.assertRaises(ValueError, raised_call)

    def test_value_error_6(self):
        def raised_call():
            for i in range(0, 100):
                ua_generator.generate(browser=('invalid111', 'chrome'))

        self.assertRaises(ValueError, raised_call)

    def test_value_error_7(self):
        def raised_call():
            ua = ua_generator.generate()
            return ua.ch.invalid111

        self.assertRaises(AttributeError, raised_call)

    def test_type_error(self):
        def raised_call():
            filterer = Filterer(chrome_versions)
            filterer.version_range(range(0, 2))

        self.assertRaises(TypeError, raised_call)

if __name__ == '__main__':
    unittest.main()
