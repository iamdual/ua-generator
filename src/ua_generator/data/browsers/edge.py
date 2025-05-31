"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import random
from typing import List

from ..filterer import Filterer
from ..version import Version, ChromiumVersion
from ...options import Options

# https://learn.microsoft.com/en-us/deployedge/microsoft-edge-release-schedule
versions: List[ChromiumVersion] = [
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
    ChromiumVersion(Version(major=129, minor=0, build=2792, patch=(0, 99))),
    ChromiumVersion(Version(major=130, minor=0, build=2849, patch=(0, 99))),
    ChromiumVersion(Version(major=131, minor=0, build=2903, patch=(0, 99))),
    ChromiumVersion(Version(major=132, minor=0, build=2957, patch=(0, 99))),
    ChromiumVersion(Version(major=133, minor=0, build=3065, patch=(0, 99))),
    ChromiumVersion(Version(major=134, minor=0, build=3124, patch=(0, 99))),
    ChromiumVersion(Version(major=135, minor=0, build=3179, patch=(0, 99))),
    ChromiumVersion(Version(major=136, minor=0, build=3240, patch=(0, 99))),
    ChromiumVersion(Version(major=137, minor=0, build=3296, patch=(0, 99))),
]


def get_version(options: Options) -> ChromiumVersion:
    filterer = Filterer(versions)

    if options.version_ranges and 'edge' in options.version_ranges:
        filterer.version_range(options.version_ranges['edge'])

    if options.weighted_versions:
        filterer.weighted_versions()

    return random.choice(filterer.versions)
