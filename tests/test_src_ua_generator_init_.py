import unittest
import src.ua_generator as ua_generator
from src.ua_generator.options import Options
from typing import List
from src.ua_generator.data.version import VersionRange, Version
from src.ua_generator.data.browsers import chrome,safari,edge,firefox
from src.ua_generator.data.platforms import linux,ios,macos,windows
from src.ua_generator.data.platforms.android import android_nexus,android_samsung,android_pixel
from src.ua_generator.data import VERSION_SUPPORTED_MODULES
class TestUaGeneratorSrcInit(unittest.TestCase):
    def test_idx_maps_persist_on_browser_and_platform_modules_across_generates(self):
        options = Options(version_ranges={
            "chrome": VersionRange(chrome.versions[0], chrome.versions[-1]),
            "safari": VersionRange(safari.versions[0], safari.versions[-1]),
            "edge": VersionRange(edge.versions[0], edge.versions[-1]),
            "firefox": VersionRange(firefox.versions[0], firefox.versions[-1]),
            "linux": VersionRange(linux.versions[0], linux.versions[-1]),
            "ios": VersionRange(ios.versions[0], ios.versions[-1]),
            "macos": VersionRange(macos.versions[0], macos.versions[-1]),
            "windows": VersionRange(windows.versions[0], windows.versions[-1]),
            "android_nexus": VersionRange(android_nexus.versions[0], android_nexus.versions[-1]),
            "android_pixel": VersionRange(android_pixel.versions[0], android_pixel.versions[-1]),
            "android_samsung": VersionRange(android_samsung.versions[0], android_samsung.versions[-1]),
        })
        for i in range(10000):
            #if no indexing error is thrown, then pass
            ua_generator.generate(options=options)
        for i in ua_generator.versions_idx_map.keys():
            self.assertGreater(len(ua_generator.versions_idx_map[i]),0)
            #ensures the index map persists
    def test_get_versions(self):
        for option in VERSION_SUPPORTED_MODULES:
            versions = ua_generator.get_versions(option)
            # Check if versions is a list
            self.assertIsInstance(versions, list, f"Expected 'versions' to be a list for option {option}")
            # Check if the list is not empty
            self.assertGreater(len(versions), 0, f"'versions' list is empty for option {option}")
            # Check if each element in the list is an instance of Version
            for version in versions:
                self.assertIsInstance(version, Version, f"Expected each element to be a 'Version', got {type(version)}")
