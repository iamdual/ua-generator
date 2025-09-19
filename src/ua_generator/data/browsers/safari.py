"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import random
from typing import List

from ..filterer import Filterer
from ..version import Version, SafariVersion
from ...options import Options

# https://developer.apple.com/documentation/safari-release-notes
VERSIONS: List[SafariVersion] = [
    SafariVersion(Version(major=10, minor=0), webkit=Version(major=602, minor=4, build=8)),
    SafariVersion(Version(major=11, minor=0), webkit=Version(major=604, minor=1, build=38)),
    SafariVersion(Version(major=12, minor=(0, 1))),
    SafariVersion(Version(major=13, minor=(0, 1))),
    SafariVersion(Version(major=14, minor=(0, 1))),
    SafariVersion(Version(major=15, minor=(0, 6))),
    SafariVersion(Version(major=16, minor=(0, 6))),
    SafariVersion(Version(major=17, minor=(0, 6))),
    SafariVersion(Version(major=18, minor=(0, 5))),
    SafariVersion(Version(major=26, minor=0)),
]


def get_version(options: Options, platform_version: Version) -> SafariVersion:
    if options.tied_safari_version:
        return SafariVersion(platform_version)

    filterer = Filterer(VERSIONS)

    if options.version_ranges and 'safari' in options.version_ranges:
        filterer.version_range(options.version_ranges['safari'])

    if options.weighted_versions:
        filterer.weighted_versions(max_range=3)

    return random.choice(filterer.versions)
