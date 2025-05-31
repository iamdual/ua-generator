"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
import typing
from typing import Optional

from .data.version import VersionRange


class Options:
    weighted_versions: bool = False
    version_ranges: Optional[dict[str, VersionRange]] = None

    def __init__(self, weighted_versions: bool = False, version_ranges: Optional[dict[str, VersionRange]] = None):
        self.weighted_versions = weighted_versions
        if version_ranges is not None:
            self.version_ranges = version_ranges

    def __repr__(self):
        return f"Options(weighted_versions={self.weighted_versions}, version_ranges={self.version_ranges})"
