"""
Random User-Agent
Copyright: 2022-2026 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
from typing import Optional, Union

from .data.version import VersionRange


class Options:
    weighted_versions: bool = False
    version_ranges: Optional[dict[str, VersionRange]] = None
    latest_versions: Union[bool, dict[str, int]] = False
    tied_safari_version: bool = False

    """
    Options can be configured with constructor arguments:
    ```
    options = Options(
        weighted_versions=True,
        tied_safari_version=True,
        latest_versions={
            'chrome': 3,
            'macos': 1,
        },
        version_ranges={
            'chrome': VersionRange(125, 129),
            'edge': VersionRange(min_version=120),
        },
    )
    ua = ua_generator.generate(options=options)
    ```
    """

    def __init__(self,
                 weighted_versions: bool = False,
                 tied_safari_version: bool = False,
                 latest_versions: Union[bool, dict[str, int]] = False,
                 version_ranges: Optional[dict[str, VersionRange]] = None):
        self.weighted_versions = weighted_versions
        self.tied_safari_version = tied_safari_version
        self.latest_versions = latest_versions
        if version_ranges is not None:
            self.version_ranges = version_ranges

    def latest_version_limit(self, key: str) -> Optional[int]:
        if isinstance(self.latest_versions, bool):
            return 1 if self.latest_versions else None

        if not isinstance(self.latest_versions, dict):
            raise TypeError('Parameter latest_versions must be type of bool or dict')

        if key not in self.latest_versions:
            return None

        limit = self.latest_versions[key]
        if not isinstance(limit, int) or isinstance(limit, bool):
            raise TypeError('Parameter latest_versions values must be type of int')
        if limit < 1:
            raise ValueError('Parameter latest_versions values must be greater than 0')

        return limit

    def __repr__(self):
        v = []
        for var in vars(self):
            if var.startswith('_'):
                continue
            v.append(f"{var}={getattr(self, var)}")
        return f"Options({', '.join(v)})"
