"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import random
from typing import List

from ..version import Version, VersionRange
from ...options import Options
from ...exceptions import InvalidVersionError
#ua-generator/src/data/browsers/macos.py
# User agent cap on macOS
# https://groups.google.com/a/chromium.org/g/blink-dev/c/hAI4QoX6rEo/m/qQNPThr0AAAJ

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
]

versions_idx_map = {}

def get_version(options: Options) -> Version:
    if options.version_ranges is not None and 'macos' in options.version_ranges:
        if type(options.version_ranges['macos']) == VersionRange:
            version_range = options.version_ranges['macos']
            min_idx = 0
            max_idx = len(versions)
            if(version_range.min_version is not None):
                if(version_range.min_version.major not in versions_idx_map):
                    raise InvalidVersionError("Invalid {} version {} specified, valid versions are {}-{}\n".format("firefox", version_range.min_version.major, versions[0].major, versions[-1].major))
                min_idx = versions_idx_map[version_range.min_version.major]
            if(version_range.max_version is not None):
                if(version_range.max_version.major not in versions_idx_map):
                    raise InvalidVersionError("Invalid {} version {} specified, valid versions are {}-{}\n".format("firefox", version_range.min_version.major, versions[0].major, versions[-1].major))
                max_idx = versions_idx_map[version_range.max_version.major]+1 
            filtered = versions[min_idx:max_idx]
            if len(filtered) > 0:
                return random.choice(filtered)

    weights = None
    if options.weighted_versions:
        weights = [1.0] * len(versions)
        weights[-1] = 10.0
        weights[-2] = 9.0
        weights[-3] = 8.0

    choice: List[Version] = random.choices(versions, weights=weights, k=1)
    return choice[0]
