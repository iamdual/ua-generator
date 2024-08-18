"""
Random User-Agent
Copyright: 2022 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import re
import unittest
from src.ua_generator.options import Options

import src.ua_generator as ua_generator
from src.ua_generator import exceptions 

class TestUserAgent(unittest.TestCase):
    def test_user_agent(self):
        for i in range(0, 100):
            ua = ua_generator.generate()
            self.assertIsNotNone(ua.device)
            self.assertIsNotNone(ua.platform)
            self.assertIsNotNone(ua.browser)
            self.assertIsNotNone(ua.text)

    def test_user_agent_2(self):
        for i in range(0, 100):
            ua = ua_generator.generate(platform=('ios', 'macos'), browser='safari')
            self.assertIsNotNone(ua.device)
            self.assertIsNotNone(ua.platform)
            self.assertIsNotNone(ua.browser)
            self.assertIsNotNone(ua.text)

    def test_user_agent_3(self):
        for i in range(0, 100):
            ua = ua_generator.generate(device='mobile', browser=('safari', 'chrome'))
            self.assertIsNotNone(ua.device)
            self.assertIsNotNone(ua.platform)
            self.assertIsNotNone(ua.browser)
            self.assertIsNotNone(ua.text)

    def test_user_agent_4(self):
        for i in range(0, 100):
            ua = ua_generator.generate(device='desktop', browser='firefox')
            self.assertIsNotNone(ua.device)
            self.assertIsNotNone(ua.platform)
            self.assertIsNotNone(ua.browser)
            self.assertIsNotNone(ua.text)

    def test_user_agent_5(self):
        for i in range(0, 1000):
            device = ('desktop', 'mobile')
            platform = ('windows', 'macos', 'ios', 'linux', 'android')
            browser = ('chrome', 'edge', 'firefox', 'safari')
            ua = ua_generator.generate(device=device, browser=browser, platform=platform)
            self.assertIsNotNone(ua.device)
            self.assertIsNotNone(ua.platform)
            self.assertIsNotNone(ua.browser)
            self.assertIsNotNone(ua.text)

    def test_user_agent_not_contains_brackets(self):
        brackets = re.compile('{(d|s|v|build|chrome|firefox|safari|webkit|windows|android|ios|macos|linux)}')
        for i in range(0, 200):
            ua = ua_generator.generate()
            self.assertNotRegex(ua.text, brackets)
    def test_invalid_browser_version_range(self):
        #Goal is to ensure the proper error(s) are raised when an invalid browser version range is specified
        # Case 1: Chrome version range with 101 and 100 
        options = Options(chrome_versions=(101, 100))
        with self.assertRaises(exceptions.InvalidArgumentError):
            ua_generator.generate(browser="chrome", options=options)

        # Case 2: Chrome version range with 99 and 101 (99 is an invalid version)
        options = Options(chrome_versions=(99, 101))
        with self.assertRaises(exceptions.InvalidArgumentError):
            ua_generator.generate(browser="chrome", options=options)

        # Case 3: Firefox version range with 129 and 130 (130 not valid version)
        options = Options(firefox_versions=(129, 130))
        with self.assertRaises(exceptions.InvalidArgumentError):
            ua_generator.generate(browser="firefox", options=options)

        # Case 4: Edge version range with 106 and 102 (invalid range)
        options = Options(edge_versions=(106, 102))
        with self.assertRaises(exceptions.InvalidArgumentError):
            ua_generator.generate(browser="edge", options=options)

        # Case 5: Safari version range with 12 and 10 (invalid range)
        options = Options(safari_versions=(12, 10))
        with self.assertRaises(exceptions.InvalidArgumentError):
            ua = ua_generator.generate(platform="macos", browser="safari", options=options)
            print(ua.text)
    
    def test_valid_browser_version_ranges(self):
    #Make sure proper browser version ranges are accepted
        # Define the valid version ranges for each browser
        valid_ranges = {
            "chrome": (100, 127),  # Ranges from major version 100 to 127
            "firefox": (103, 129),  # Ranges from major version 103 to 129
            "edge": (100, 128),     # Ranges from major version 100 to 128
            "safari": (10, 17)      # Ranges from major version 10 to 17
        }

        for browser, (min_version, max_version) in valid_ranges.items():
            # Create Options instance with the valid version range
            options = Options(**{f"{browser}_versions": (min_version, max_version)})

            # Generate a user agent for the given browser and options
            try:
                ua = ua_generator.generate(browser=browser, options=options)
            except exceptions.InvalidArgumentError as e:
                self.fail(f"Unexpected InvalidArgumentError for {browser} with version range {min_version}-{max_version}: {str(e)}")
          
        
if __name__ == '__main__':
    unittest.main()
