"""
Random User-Agent
Copyright: 2022-2025 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import random
from typing import List

from ..filterer import Filterer
from ..version import Version, WindowsVersion
from ...options import Options

# https://learn.microsoft.com/en-us/windows/win32/sysinfo/operating-system-version
# https://learn.microsoft.com/en-us/microsoft-edge/web-platform/how-to-detect-win11
VERSIONS: List[WindowsVersion] = [
    WindowsVersion(Version(major=6, minor=1), ch_platform=Version(major=0)),  # Win7
    WindowsVersion(Version(major=6, minor=2), ch_platform=Version(major=0)),  # Win8
    WindowsVersion(Version(major=6, minor=3), ch_platform=Version(major=0)),  # Win8.1
    WindowsVersion(Version(major=10, minor=0), ch_platform=Version(major=(1, 10))),  # Win10
    WindowsVersion(Version(major=10, minor=0), ch_platform=Version(major=(13, 15))),  # Win11
]


def get_version(options: Options) -> WindowsVersion:
    filterer = Filterer(VERSIONS)

    if options.version_ranges and 'windows' in options.version_ranges:
        filterer.version_range(options.version_ranges['windows'])

    if options.weighted_versions:
        filterer.weighted_versions(max_range=2)

    return random.choice(filterer.versions)
