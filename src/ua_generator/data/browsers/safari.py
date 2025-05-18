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

# https://developer.apple.com/documentation/safari-release-notes
versions: List[ChromiumVersion] = [
    ChromiumVersion(Version(major=10, minor=0), webkit=Version(major=602, minor=4, build=8)),
    ChromiumVersion(Version(major=11, minor=0), webkit=Version(major=604, minor=1, build=38)),
    ChromiumVersion(Version(major=12, minor=(0, 1)), webkit=Version(major=605, minor=1, build=15)),
    ChromiumVersion(Version(major=13, minor=(0, 1)), webkit=Version(major=605, minor=1, build=15)),
    ChromiumVersion(Version(major=14, minor=(0, 1)), webkit=Version(major=605, minor=1, build=15)),
    ChromiumVersion(Version(major=15, minor=(0, 6)), webkit=Version(major=605, minor=1, build=15)),
    ChromiumVersion(Version(major=16, minor=(0, 6)), webkit=Version(major=605, minor=1, build=15)),
    ChromiumVersion(Version(major=17, minor=(0, 6)), webkit=Version(major=605, minor=1, build=15)),
    ChromiumVersion(Version(major=18, minor=(0, 5)), webkit=Version(major=605, minor=1, build=15)),
]


def get_version(options: Options) -> ChromiumVersion:
    filterer = Filterer(versions)

    if options.version_ranges and 'safari' in options.version_ranges:
        filterer.version_range(options.version_ranges['safari'])

    if options.weighted_versions:
        filterer.weighted_versions(max_range=3)

    return random.choice(filterer.versions)
