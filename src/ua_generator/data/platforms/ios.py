"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import random
from typing import List

from ..filterer import Filterer
from ..version import Version
from ...options import Options

# https://developer.apple.com/documentation/ios-ipados-release-notes
# https://developer.apple.com/news/releases/
# https://support.apple.com/en-us/HT201222
versions: List[Version] = [
    Version(major=14, minor=0, build=(0, 1)),
    Version(major=14, minor=1, build=0),
    Version(major=14, minor=2, build=(0, 1)),
    Version(major=14, minor=3, build=0),
    Version(major=14, minor=4, build=(0, 2)),
    Version(major=14, minor=5, build=(0, 1)),
    Version(major=14, minor=6, build=0),
    Version(major=14, minor=7, build=(0, 1)),
    Version(major=15, minor=0, build=(0, 2)),
    Version(major=15, minor=1, build=(0, 1)),
    Version(major=15, minor=2, build=(0, 1)),
    Version(major=15, minor=3, build=(0, 1)),
    Version(major=15, minor=4, build=(0, 1)),
    Version(major=15, minor=5, build=0),
    Version(major=15, minor=6, build=(0, 1)),
    Version(major=16, minor=4, build=(0, 1)),
    Version(major=16, minor=5, build=(0, 2)),
    Version(major=16, minor=6, build=(0, 1)),
    Version(major=17, minor=0, build=(0, 3)),
    Version(major=17, minor=1, build=(0, 2)),
    Version(major=17, minor=2, build=(0, 1)),
    Version(major=17, minor=3, build=(0, 1)),
    Version(major=17, minor=4, build=(0, 1)),
    Version(major=17, minor=5, build=(0, 1)),
    Version(major=17, minor=6, build=(0, 1)),
    Version(major=18, minor=0, build=(0, 1)),
    Version(major=18, minor=1, build=(0, 1)),
    Version(major=18, minor=2, build=(0, 1)),
    Version(major=18, minor=3, build=(0, 1)),
    Version(major=18, minor=5, build=(0, 1)),
]


def get_version(options: Options) -> Version:
    filterer = Filterer(versions)

    if options.version_ranges and 'ios' in options.version_ranges:
        filterer.version_range(options.version_ranges['ios'])

    if options.weighted_versions:
        filterer.weighted_versions()

    return random.choice(filterer.versions)
