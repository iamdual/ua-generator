"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import random
from typing import List

from ..filterer import Filterer
from ..version import Version, WindowsVersion
from ...options import Options

# https://learn.microsoft.com/en-us/windows/win32/sysinfo/operating-system-version
# https://learn.microsoft.com/en-us/microsoft-edge/web-platform/how-to-detect-win11
versions: List[WindowsVersion] = [
    WindowsVersion(Version(major=6, minor=1), ch_platform=Version(major=0)),
    WindowsVersion(Version(major=6, minor=2), ch_platform=Version(major=0)),
    WindowsVersion(Version(major=6, minor=3), ch_platform=Version(major=0)),
    WindowsVersion(Version(major=10, minor=0), ch_platform=Version(major=10)),
    WindowsVersion(Version(major=10, minor=0), ch_platform=Version(major=(13, 15))),
]


def get_version(options: Options) -> WindowsVersion:
    filterer = Filterer(versions)

    if options.version_ranges and 'windows' in options.version_ranges:
        filterer.version_range(options.version_ranges['windows'])

    if options.weighted_versions:
        weights = [1.0] * len(versions)
        # https://gs.statcounter.com/os-version-market-share/windows/desktop/worldwide
        weights[-2] = 10.0
        weights[-1] = 7.0
        filterer.weighted_versions(weights=weights)

    return random.choice(filterer.versions)
