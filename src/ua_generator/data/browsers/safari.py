#ua-generator/src/data/browsers/safari.py
"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import random
from typing import List

from ..version import Version, ChromiumVersion, VersionRange
from ...options import Options
from ...exceptions import InvalidVersionError

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
    ChromiumVersion(Version(major=18, minor=(0, 1)), webkit=Version(major=605, minor=1, build=15)),
]

versions_idx_map = {}

def get_version(options: Options) -> ChromiumVersion:
    selected_version : ChromiumVersion
    if options.version_ranges is not None and 'safari' in options.version_ranges:
        version_range = options.version_ranges['safari']
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
        weights[-1] = 10.0
        weights[-2] = 9.0
        selected_version = random.choices(versions, weights=weights, k=1)[0]
    else:
        selected_version = random.choice(versions)
    selected_version.get_version()
    return selected_version
