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

# User agent cap on macOS
# https://groups.google.com/a/chromium.org/g/blink-dev/c/hAI4QoX6rEo/m/qQNPThr0AAAJ

# https://developer.apple.com/news/releases/
# https://support.apple.com/en-us/HT201222
versions: List[Version] = [
    Version(major=10, minor=11, build=(0, 6)),
    Version(major=10, minor=12, build=(0, 6)),
    Version(major=10, minor=13, build=(0, 6)),
    Version(major=10, minor=14, build=(0, 6)),
    Version(major=10, minor=15, build=(0, 7)),
    Version(major=11, minor=0, build=0),
    Version(major=11, minor=2, build=(0, 3)),
    Version(major=11, minor=3, build=(0, 1)),
    Version(major=11, minor=5, build=(0, 2)),
    Version(major=11, minor=6, build=(0, 6)),
    Version(major=12, minor=0, build=(0, 1)),
    Version(major=12, minor=2, build=(0, 1)),
    Version(major=12, minor=3, build=(0, 1)),
    Version(major=12, minor=4, build=0),
    Version(major=12, minor=5, build=(0, 1)),
    Version(major=12, minor=6, build=(0, 4)),
    Version(major=12, minor=7, build=(0, 5)),
    Version(major=13, minor=0, build=(0, 1)),
    Version(major=13, minor=1, build=0),
    Version(major=13, minor=2, build=(0, 1)),
    Version(major=13, minor=3, build=(0, 1)),
    Version(major=13, minor=4, build=(0, 1)),
    Version(major=13, minor=5, build=(0, 2)),
    Version(major=14, minor=0, build=(0, 1)),
    Version(major=14, minor=1, build=(0, 2)),
    Version(major=14, minor=2, build=(0, 1)),
    Version(major=14, minor=3, build=(0, 1)),
    Version(major=14, minor=4, build=(0, 1)),
    Version(major=14, minor=5, build=0),
    Version(major=14, minor=6, build=(0, 1)),
    Version(major=15, minor=0, build=(0, 1)),
    Version(major=15, minor=1, build=(0, 1)),
    Version(major=15, minor=2, build=(0, 1)),
    Version(major=15, minor=3, build=(0, 1)),
    Version(major=15, minor=4, build=(0, 1)),
]


def get_version(options: Options) -> Version:
    filterer = Filterer(versions)

    if options.version_ranges and 'macos' in options.version_ranges:
        filterer.version_range(options.version_ranges['macos'])

    if options.weighted_versions:
        filterer.weighted_versions()

    return random.choice(filterer.versions)
