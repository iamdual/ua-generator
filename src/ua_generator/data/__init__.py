"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
from .version import ChromiumVersion, Version

DEVICES = ('desktop', 'mobile')
PLATFORMS = ('windows', 'macos', 'ios', 'linux', 'android')
PLATFORMS_DESKTOP = ('windows', 'macos', 'linux')  # Platforms on desktop devices
PLATFORMS_MOBILE = ('ios', 'android')  # Platforms on mobile devices
BROWSERS = ('chrome', 'edge', 'firefox', 'safari')
BROWSERS_SUPPORT_CH = ('chrome', 'edge')  # Browsers that support Client Hints
#empty index map initialized at import (preprocessing)
browser_versions_idx_map = {"chrome":{}, 'edge':{},'safari':{},'firefox':{}}
browser_versions = {
    "chrome": [
        ChromiumVersion(Version(major=100, minor=0, build=4896, patch=(0, 255))),
        ChromiumVersion(Version(major=101, minor=0, build=4951, patch=(0, 255))),
        ChromiumVersion(Version(major=102, minor=0, build=5005, patch=(0, 255))),
        ChromiumVersion(Version(major=103, minor=0, build=5060, patch=(0, 255))),
        ChromiumVersion(Version(major=104, minor=0, build=5112, patch=(0, 255))),
        ChromiumVersion(Version(major=105, minor=0, build=5195, patch=(0, 255))),
        ChromiumVersion(Version(major=106, minor=0, build=5249, patch=(0, 255))),
        ChromiumVersion(Version(major=107, minor=0, build=5304, patch=(0, 255))),
        ChromiumVersion(Version(major=108, minor=0, build=5359, patch=(0, 255))),
        ChromiumVersion(Version(major=109, minor=0, build=5414, patch=(0, 255))),
        ChromiumVersion(Version(major=110, minor=0, build=5481, patch=(0, 255))),
        ChromiumVersion(Version(major=111, minor=0, build=5563, patch=(0, 255))),
        ChromiumVersion(Version(major=112, minor=0, build=5615, patch=(0, 255))),
        ChromiumVersion(Version(major=114, minor=0, build=5735, patch=(0, 255))),
        ChromiumVersion(Version(major=115, minor=0, build=5790, patch=(0, 255))),
        ChromiumVersion(Version(major=116, minor=0, build=5845, patch=(0, 255))),
        ChromiumVersion(Version(major=117, minor=0, build=5938, patch=(0, 255))),
        ChromiumVersion(Version(major=118, minor=0, build=5993, patch=(0, 255))),
        ChromiumVersion(Version(major=119, minor=0, build=6045, patch=(0, 255))),
        ChromiumVersion(Version(major=120, minor=0, build=6099, patch=(0, 255))),
        ChromiumVersion(Version(major=121, minor=0, build=6167, patch=(0, 255))),
        ChromiumVersion(Version(major=122, minor=0, build=6261, patch=(0, 255))),
        ChromiumVersion(Version(major=123, minor=0, build=6312, patch=(0, 255))),
        ChromiumVersion(Version(major=124, minor=0, build=6367, patch=(0, 255))),
        ChromiumVersion(Version(major=125, minor=0, build=6422, patch=(0, 255))),
        ChromiumVersion(Version(major=126, minor=0, build=6478, patch=(0, 255))),
        ChromiumVersion(Version(major=127, minor=0, build=6533, patch=(0, 255))),
    ],

    "firefox": [
        Version(major=103, minor=0, build=(0, 2)),
        Version(major=104, minor=0, build=(0, 2)),
        Version(major=105, minor=0, build=(0, 3)),
        Version(major=106, minor=0, build=(0, 5)),
        Version(major=107, minor=0, build=(0, 1)),
        Version(major=108, minor=0, build=(0, 2)),
        Version(major=109, minor=0, build=(0, 1)),
        Version(major=110, minor=0, build=(0, 1)),
        Version(major=111, minor=0, build=(0, 1)),
        Version(major=112, minor=0, build=(0, 2)),
        Version(major=113, minor=0, build=(0, 2)),
        Version(major=114, minor=0, build=(0, 2)),
        Version(major=115, minor=0, build=(0, 3)),
        Version(major=115, minor=1, build=0),
        Version(major=115, minor=2, build=(0, 1)),
        Version(major=115, minor=3, build=(0, 1)),
        Version(major=115, minor=4, build=0),
        Version(major=115, minor=5, build=0),
        Version(major=115, minor=6, build=0),
        Version(major=115, minor=7, build=0),
        Version(major=115, minor=8, build=0),
        Version(major=116, minor=0, build=(0, 3)),
        Version(major=117, minor=0, build=(0, 1)),
        Version(major=118, minor=0, build=(0, 2)),
        Version(major=119, minor=0, build=(0, 1)),
        Version(major=120, minor=0, build=(0, 1)),
        Version(major=121, minor=0, build=(0, 1)),
        Version(major=122, minor=0, build=(0, 1)),
        Version(major=123, minor=0, build=(0, 1)),
        Version(major=124, minor=0, build=(0, 2)),
        Version(major=125, minor=0, build=(1, 3)),
        Version(major=126, minor=0, build=0),
        Version(major=127, minor=0, build=(0, 2)),
        Version(major=128, minor=0, build=(0, 3)),
        Version(major=128, minor=1, build=0),
        Version(major=129, minor=0, build=0),
    ],

    "edge": [
        ChromiumVersion(Version(major=100, minor=0, build=1185, patch=(0, 99))),
        ChromiumVersion(Version(major=101, minor=0, build=1210, patch=(0, 99))),
        ChromiumVersion(Version(major=102, minor=0, build=1245, patch=(0, 99))),
        ChromiumVersion(Version(major=103, minor=0, build=1264, patch=(0, 99))),
        ChromiumVersion(Version(major=104, minor=0, build=1293, patch=(0, 99))),
        ChromiumVersion(Version(major=105, minor=0, build=1343, patch=(0, 99))),
        ChromiumVersion(Version(major=106, minor=0, build=1370, patch=(0, 99))),
        ChromiumVersion(Version(major=107, minor=0, build=1418, patch=(0, 99))),
        ChromiumVersion(Version(major=108, minor=0, build=1462, patch=(0, 99))),
        ChromiumVersion(Version(major=109, minor=0, build=1518, patch=(0, 99))),
        ChromiumVersion(Version(major=110, minor=0, build=1587, patch=(0, 99))),
        ChromiumVersion(Version(major=111, minor=0, build=1661, patch=(0, 99))),
        ChromiumVersion(Version(major=112, minor=0, build=1722, patch=(0, 99))),
        ChromiumVersion(Version(major=113, minor=0, build=1774, patch=(0, 99))),
        ChromiumVersion(Version(major=114, minor=0, build=1823, patch=(0, 99))),
        ChromiumVersion(Version(major=115, minor=0, build=1901, patch=(0, 99))),
        ChromiumVersion(Version(major=116, minor=0, build=1938, patch=(0, 99))),
        ChromiumVersion(Version(major=117, minor=0, build=2045, patch=(0, 99))),
        ChromiumVersion(Version(major=118, minor=0, build=2088, patch=(0, 99))),
        ChromiumVersion(Version(major=119, minor=0, build=2151, patch=(0, 99))),
        ChromiumVersion(Version(major=120, minor=0, build=2210, patch=(0, 99))),
        ChromiumVersion(Version(major=121, minor=0, build=2277, patch=(0, 99))),
        ChromiumVersion(Version(major=122, minor=0, build=2365, patch=(0, 99))),
        ChromiumVersion(Version(major=123, minor=0, build=2420, patch=(0, 99))),
        ChromiumVersion(Version(major=124, minor=0, build=2478, patch=(0, 99))),
        ChromiumVersion(Version(major=125, minor=0, build=2535, patch=(0, 99))),
        ChromiumVersion(Version(major=126, minor=0, build=2592, patch=(0, 99))),
        ChromiumVersion(Version(major=127, minor=0, build=2651, patch=(0, 99))),
        ChromiumVersion(Version(major=128, minor=0, build=2739, patch=(0, 99))),
    ],

    "safari": [
        ChromiumVersion(Version(major=10, minor=0), webkit=Version(major=602, minor=4, build=8)),
        ChromiumVersion(Version(major=11, minor=0), webkit=Version(major=604, minor=1, build=38)),
        ChromiumVersion(Version(major=12, minor=(0, 1)), webkit=Version(major=605, minor=1, build=15)),
        ChromiumVersion(Version(major=13, minor=(0, 1)), webkit=Version(major=605, minor=1, build=15)),
        ChromiumVersion(Version(major=14, minor=(0, 1)), webkit=Version(major=605, minor=1, build=15)),
        ChromiumVersion(Version(major=15, minor=(0, 6)), webkit=Version(major=605, minor=1, build=15)),
        ChromiumVersion(Version(major=16, minor=(0, 6)), webkit=Version(major=605, minor=1, build=15)),
        ChromiumVersion(Version(major=17, minor=(0, 6)), webkit=Version(major=605, minor=1, build=15)),
    ]
}
