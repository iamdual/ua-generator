"""
Random User-Agent
Copyright: 2022 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import unittest

import src.ua_generator as ua_generator
from src.ua_generator.data import browser_versions_idx_map, browser_versions
from src.ua_generator.options import Options
from src.ua_generator.data.browsers import firefox,safari,chrome,edge
from src.ua_generator import exceptions
class TestBrowser(unittest.TestCase):
    def assertWithinRange(self, value, min_value, max_value):
        self.assertGreaterEqual(value, min_value, f"{value} is less than {min_value}")
        self.assertLessEqual(value, max_value, f"{value} is greater than {max_value}")

    def test_browser(self):
        for i in range(0, 100):
            ua = ua_generator.generate(browser=('chrome',))
            self.assertTrue(ua.browser == 'chrome')

    def test_browser_2(self):
        for i in range(0, 100):
            ua = ua_generator.generate(browser=('chrome', 'firefox'))
            self.assertTrue(ua.browser == 'chrome' or ua.browser == 'firefox')

    def test_browser_3(self):
        for i in range(0, 100):
            ua = ua_generator.generate(platform=('macos', 'ios'), browser='safari')
            self.assertTrue(ua.browser == 'safari')

    def test_browser_4(self):
        for i in range(0, 100):
            ua = ua_generator.generate(platform=('windows', 'linux'), browser='safari')
            self.assertTrue(ua.browser == 'chrome')

    def test_browser_5(self):
        for i in range(0, 100):
            ua = ua_generator.generate(platform=('macos', 'linux'), browser='safari')
            self.assertTrue((ua.platform == 'macos' and ua.browser == 'safari') or
                            (ua.platform == 'linux' and ua.browser == 'chrome'))
    def test_idx_map(self):
        #Ensure the idx_map is initialized correctly
        for k,v in browser_versions_idx_map.items():
            for k2,v2 in v.items():
                self.assertTrue(browser_versions[k][v2].major == k2)
    def test_valid_version_ranges(self):
        #Ensure that a browser version range within the range specified is produced
        chrome_options = Options(chrome_versions=(100, 105))
        safari_options = Options(safari_versions=(10, 10))
        edge_options = Options(edge_versions=(104, 105))
        firefox_options = Options(firefox_versions=(103, 129))

        # Assuming you have methods like get_version() that returns the major version number of the browser
        chrome_version = chrome.get_version(chrome_options)
        safari_version = safari.get_version(safari_options)
        edge_version = edge.get_version(edge_options)
        firefox_version = firefox.get_version(firefox_options)

        self.assertWithinRange(
        chrome_version.major, 
        chrome_options.browser_version_ranges['chrome'].min, 
        chrome_options.browser_version_ranges['chrome'].max
        )   
        self.assertWithinRange(
            safari_version.major, 
            safari_options.browser_version_ranges['safari'].min, 
            safari_options.browser_version_ranges['safari'].max
        )
        self.assertWithinRange(
            edge_version.major, 
            edge_options.browser_version_ranges['edge'].min, 
            edge_options.browser_version_ranges['edge'].max
        )
        self.assertWithinRange(
            firefox_version.major, 
            firefox_options.browser_version_ranges['firefox'].min, 
            firefox_options.browser_version_ranges['firefox'].max
        )
if __name__ == '__main__':
    unittest.main()
