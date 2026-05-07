"""
Random User-Agent
Copyright: 2022-2026 Ekin Karadeniz (github.com/iamdual)
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
VERSIONS: List[Version] = [
    Version(major=14, minor=0, build=(0, 1)),
    Version(major=14, minor=1, build=0),
    Version(major=14, minor=2, build=(0, 1)),
    Version(major=14, minor=3, build=0),
    Version(major=14, minor=4, build=(0, 2)),
    Version(major=14, minor=5, build=(0, 1)),
    Version(major=14, minor=6, build=0),
    Version(major=14, minor=7, build=(0, 1)),
    Version(major=14, minor=8, build=(0, 1)),
    Version(major=15, minor=0, build=(0, 2)),
    Version(major=15, minor=1, build=(0, 1)),
    Version(major=15, minor=2, build=(0, 1)),
    Version(major=15, minor=3, build=(0, 1)),
    Version(major=15, minor=4, build=(0, 1)),
    Version(major=15, minor=5, build=0),
    Version(major=15, minor=6, build=(0, 1)),
    Version(major=15, minor=7, build=(0, 9)),
    Version(major=15, minor=8, build=(0, 7)),
    Version(major=16, minor=4, build=(0, 1)),
    Version(major=16, minor=5, build=(0, 2)),
    Version(major=16, minor=6, build=(0, 1)),
    Version(major=16, minor=7, build=(0, 15)),
    Version(major=17, minor=0, build=(0, 3)),
    Version(major=17, minor=1, build=(0, 2)),
    Version(major=17, minor=2, build=(0, 1)),
    Version(major=17, minor=3, build=(0, 1)),
    Version(major=17, minor=4, build=(0, 1)),
    Version(major=17, minor=5, build=(0, 1)),
    Version(major=17, minor=6, build=(0, 1)),
    Version(major=17, minor=7, build=(0, 2)),
    Version(major=18, minor=0, build=(0, 1)),
    Version(major=18, minor=1, build=(0, 1)),
    Version(major=18, minor=2, build=(0, 1)),
    Version(major=18, minor=3, build=(0, 1)),
    Version(major=18, minor=4, build=(0, 1)),
    Version(major=18, minor=5, build=0),
    Version(major=18, minor=6, build=(0, 2)),
    Version(major=18, minor=7, build=(0, 8)),
    Version(major=26, minor=0, build=(0, 1)),
    Version(major=26, minor=1, build=0),
    Version(major=26, minor=2, build=(0, 1)),
    Version(major=26, minor=3, build=(0, 1)),
    Version(major=26, minor=4, build=(0, 2)),
]


def get_version(options: Options) -> Version:
    filterer = Filterer(VERSIONS, 'ios', options)

    return random.choice(filterer.versions)
