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

# https://www.mozilla.org/en-US/firefox/releases/
versions: List[Version] = [
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
    Version(major=128, minor=2, build=0),
    Version(major=128, minor=3, build=0),
    Version(major=128, minor=4, build=0),
    Version(major=128, minor=5, build=(0, 2)),
    Version(major=128, minor=6, build=0),
    Version(major=129, minor=0, build=(0, 2)),
    Version(major=130, minor=0, build=(0, 1)),
    Version(major=131, minor=0, build=(0, 3)),
    Version(major=132, minor=0, build=(0, 2)),
    Version(major=133, minor=0, build=(0, 3)),
    Version(major=134, minor=0, build=(0, 2)),
    Version(major=135, minor=0, build=(0, 1)),
    Version(major=136, minor=0, build=(0, 4)),
    Version(major=137, minor=0, build=(0, 2)),
    Version(major=138, minor=0, build=(0, 4)),
    Version(major=139, minor=0, build=(0, 1)),
]


def get_version(options: Options) -> Version:
    filterer = Filterer(versions)

    if options.version_ranges and 'firefox' in options.version_ranges:
        filterer.version_range(options.version_ranges['firefox'])

    if options.weighted_versions:
        filterer.weighted_versions()

    return random.choice(filterer.versions)
