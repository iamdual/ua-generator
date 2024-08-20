"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import random
from typing import List

from ..version import Version, VersionRange
from ...options import Options

# https://www.mozilla.org/en-US/firefox/releases/
versions: List[Version] = [
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
]


def get_version(options: Options) -> Version:
    if options.version_ranges is not None and 'firefox' in options.version_ranges:
        if type(options.version_ranges['firefox']) == VersionRange:
            filtered = options.version_ranges['firefox'].filter(versions)
            if type(filtered) == list and len(filtered) > 0:
                return random.choice(filtered)

    weights = None
    if options.weighted_versions:
        weights = [1.0] * len(versions)
        weights[-1] = 10.0
        weights[-2] = 9.0
        weights[-3] = 8.0

    choice: List[Version] = random.choices(versions, weights=weights, k=1)
    return choice[0]
