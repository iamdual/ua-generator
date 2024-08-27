import unittest

import src.ua_generator as ua_generator
from src.ua_generator.options import Options
from src.ua_generator.data.version import VersionRange, Version
from src.ua_generator.exceptions import InvalidArgumentError
from src.ua_generator.data.browsers import chrome,safari,edge,firefox
from src.ua_generator.data.platforms import linux,ios,macos,windows
from src.ua_generator.data.platforms.android import android_nexus,android_samsung,android_pixel
class TestIdxMap(unittest.TestCase):
    def test_get_versions(self):
        options = ['chrome','safari','edge','firefox','macos','windows','ios','linux','android_nexus','android_samsung','android_pixel']
        for option in options:
            module = globals()[option]
            versions = ua_generator.get_versions(option)
            self.assertEqual(module.versions,versions)
        with self.assertRaises(InvalidArgumentError):
            ua_generator.get_versions("invalid")