"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import random
from typing import List

from ..version import Version, ChromiumVersion, VersionRange
from ...options import Options

# https://chromereleases.googleblog.com/search/label/Stable%20updates
versions: List[ChromiumVersion] = [
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
    ChromiumVersion(Version(major=128, minor=0, build=6613, patch=(0, 255))),
    ChromiumVersion(Version(major=129, minor=0, build=6668, patch=(0, 255))),
]


def get_version(options: Options) -> ChromiumVersion:
    if options.version_ranges is not None and 'chrome' in options.version_ranges:
        if type(options.version_ranges['chrome']) == VersionRange:
            filtered = options.version_ranges['chrome'].filter(versions)
            if type(filtered) == list and len(filtered) > 0:
                return random.choice(filtered)

    weights = None
    if options.weighted_versions:
        weights = [1.0] * len(versions)
        weights[-1] = 10.0
        weights[-2] = 9.0
        weights[-3] = 8.0

    choice: List[ChromiumVersion] = random.choices(versions, weights=weights, k=1)
    return choice[0]
