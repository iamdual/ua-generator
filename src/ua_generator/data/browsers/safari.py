"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import random
from typing import List

from ..version import Version, ChromiumVersion

# https://developer.apple.com/documentation/safari-release-notes
versions: List[ChromiumVersion] = [
    ChromiumVersion(Version(major=10, minor=(0, 0)), webkit=Version(major=602, minor=4, build=8)),
    ChromiumVersion(Version(major=11, minor=(0, 0)), webkit=Version(major=604, minor=1, build=38)),
    ChromiumVersion(Version(major=12, minor=(0, 1)), webkit=Version(major=605, minor=1, build=15)),
    ChromiumVersion(Version(major=13, minor=(0, 1)), webkit=Version(major=605, minor=1, build=15)),
    ChromiumVersion(Version(major=14, minor=(0, 1)), webkit=Version(major=605, minor=1, build=15)),
    ChromiumVersion(Version(major=15, minor=(0, 6)), webkit=Version(major=605, minor=1, build=15)),
    ChromiumVersion(Version(major=16, minor=(0, 6)), webkit=Version(major=605, minor=1, build=15)),
    ChromiumVersion(Version(major=17, minor=(0, 6)), webkit=Version(major=605, minor=1, build=15)),
]

version_weights = [1.0] * len(versions)
version_weights[-1] = 10.0
version_weights[-2] = 9.0


def get_version() -> ChromiumVersion:
    choice: List[ChromiumVersion] = random.choices(versions, weights=version_weights, k=1)
    return choice[0]
