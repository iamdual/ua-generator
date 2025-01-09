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
#ua-generator/src/data/browsers/linux.py
# https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/refs/
versions: List[Version] = [
    Version(major=5, minor=0, build=(0, 21)),
    Version(major=5, minor=1, build=(0, 21)),
    Version(major=5, minor=2, build=(0, 20)),
    Version(major=5, minor=3, build=(0, 18)),
    Version(major=5, minor=4, build=(0, 184)),
    Version(major=5, minor=5, build=(0, 19)),
    Version(major=5, minor=6, build=(0, 19)),
    Version(major=5, minor=7, build=(0, 19)),
    Version(major=5, minor=8, build=(0, 18)),
    Version(major=5, minor=9, build=(0, 16)),
    Version(major=5, minor=10, build=(0, 105)),
    Version(major=5, minor=11, build=(0, 22)),
    Version(major=5, minor=12, build=(0, 19)),
    Version(major=5, minor=13, build=(0, 19)),
    Version(major=5, minor=14, build=(0, 21)),
    Version(major=5, minor=15, build=(0, 103)),
    Version(major=5, minor=16, build=(0, 20)),
    Version(major=5, minor=17, build=(0, 15)),
    Version(major=5, minor=18, build=(0, 19)),
    Version(major=5, minor=19, build=(0, 17)),
    Version(major=6, minor=0, build=(0, 19)),
    Version(major=6, minor=1, build=(0, 78)),
    Version(major=6, minor=2, build=(0, 16)),
    Version(major=6, minor=3, build=(0, 13)),
    Version(major=6, minor=4, build=(0, 16)),
    Version(major=6, minor=5, build=(0, 13)),
    Version(major=6, minor=6, build=(0, 17)),
    Version(major=6, minor=7, build=(0, 5)),
]

versions_idx_map = {}

def get_version(options: Options) -> Version:
    selected_version : Version
    if options.version_ranges is not None and 'linux' in options.version_ranges:
        version_range = options.version_ranges['linux']
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
            selected_version = random.choice(filtered)
    
    elif options.weighted_versions:
        weights = [1.0] * len(versions)
        selected_version = random.choices(versions, weights=weights, k=1)[0]
    else:
        selected_version = random.choice(versions)
    selected_version.get_version()
    return selected_version
