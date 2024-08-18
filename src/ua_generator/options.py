"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""

from .data.version import VersionRange
from .data import browser_versions 


class Options:
    weighted_versions : bool = False
    browser_version_ranges = {
            'chrome': VersionRange(browser_versions['chrome'][0].major, browser_versions['chrome'][-1].major),
            'edge': VersionRange(browser_versions['edge'][0].major, browser_versions['edge'][-1].major),
            'safari': VersionRange(browser_versions['safari'][0].major, browser_versions['safari'][-1].major),
            'firefox': VersionRange(browser_versions['firefox'][0].major, browser_versions['firefox'][-1].major)
    }
    def __init__(self,
                weighted_versions=False, 
                chrome_versions=(browser_versions['chrome'][0].major,browser_versions['chrome'][-1].major), 
                firefox_versions=(browser_versions['firefox'][0].major, browser_versions['firefox'][-1].major), 
                safari_versions=(browser_versions['safari'][0].major, browser_versions['safari'][-1].major), 
                edge_versions=(browser_versions['edge'][0].major, browser_versions['edge'][-1].major)):
        self.browser_version_ranges['chrome'] = VersionRange(chrome_versions[0],chrome_versions[1])
        self.browser_version_ranges['edge'] = VersionRange(edge_versions[0],edge_versions[1])
        self.browser_version_ranges['safari'] = VersionRange(safari_versions[0],safari_versions[1])
        self.browser_version_ranges['firefox'] = VersionRange(firefox_versions[0],firefox_versions[1])
        self.weighted_versions=weighted_versions 