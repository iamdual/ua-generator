"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
from typing import Optional

from .data.version import VersionRange


class Options:
    weighted_versions: bool = False
    version_ranges: Optional[dict[str, VersionRange]] = None
    tied_safari_version: bool = False

    """
    Argument usages like `Options(weighted_versions=)` and `Options(version_ranges=)` are deprecated.
    Use options as variables instead:
        ```
        options = Options()
        options.weighted_versions = True
        options.tied_safari_version = True
        options.version_ranges = {
            'chrome': VersionRange(125, 129),
            'edge': VersionRange(min_version=120),
        }
        ua = ua_generator.generate(options=options)
        ```
    """
    def __init__(self, weighted_versions: bool = False, version_ranges: Optional[dict[str, VersionRange]] = None):
        self.weighted_versions = weighted_versions
        if version_ranges is not None:
            self.version_ranges = version_ranges

    def __repr__(self):
        v = []
        for var in vars(self):
            if var.startswith('_'):
                continue
            v.append(f"{var}={getattr(self, var)}")
        return f"Options({', '.join(v)})"
