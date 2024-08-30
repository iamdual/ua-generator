"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
import typing

from .data.version import VersionRange


class Options:
    weighted_versions: bool = False
    version_ranges: typing.Dict[str, VersionRange] = None

    def __init__(self, weighted_versions: bool = False, version_ranges: typing.Dict[str, VersionRange] = None):
        self.weighted_versions = weighted_versions
        if version_ranges is not None:
            self.version_ranges = version_ranges
    def __str__(self) -> str:
        # Stringify version_ranges if it exists
        version_ranges_str = (
            {k: str(v) for k, v in self.version_ranges.items()}
            if self.version_ranges is not None
            else None
        )
        return f"Options(weighted_versions={self.weighted_versions}, version_ranges={version_ranges_str})"
