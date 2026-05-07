"""
Random User-Agent
Copyright: 2022-2025 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
import random
from typing import Union, List, Optional

from .. import utils


class Version:
    major: Optional[int]
    minor: Optional[int]
    build: Optional[int]
    patch: Optional[int]

    def __init__(self,
                 major: Optional[Union[int, tuple]] = None,
                 minor: Optional[Union[int, tuple]] = None,
                 build: Optional[Union[int, tuple]] = None,
                 patch: Optional[Union[int, tuple]] = None):
        self.original = (major, minor, build, patch)
        self.major, self.minor, self.build, self.patch = map(
            lambda x:
            # https://docs.python.org/3/tutorial/controlflow.html#tut-unpacking-arguments
            random.randrange(*x) if isinstance(x, tuple) else x,
            (major, minor, build, patch)
        )
        self.__tuple: Optional[tuple] = None

    def format(self, partitions=None, limit=None, separator='.', trim_zero=False) -> str:
        versions = [self.major, self.minor, self.build, self.patch]

        if partitions is not None:
            versions = versions[:partitions]
        else:
            # Stop at None
            while versions and versions[-1] is None:
                versions.pop()

        if limit is not None and len(versions) > limit:
            for i in range(limit, len(versions)):
                versions[i] = 0

        # None to zero
        versions = list(part or 0 for part in versions)

        if trim_zero:
            while versions[-1] == 0:
                versions.pop()

        return separator.join(str(part) for part in versions)

    def __str__(self):
        return self.format()

    # We use it for comparison. See: https://docs.python.org/3/reference/expressions.html#comparisons
    def to_tuple(self) -> tuple:
        if self.__tuple is not None:
            return self.__tuple

        self.__tuple = tuple(part or 0 for part in [self.major, self.minor, self.build, self.patch])
        return self.__tuple

    def __eq__(self, other):
        return self.to_tuple() == other.to_tuple()

    def __ne__(self, other):
        return self.to_tuple() != other.to_tuple()

    def __lt__(self, other):
        return self.to_tuple() < other.to_tuple()

    def __gt__(self, other):
        return self.to_tuple() > other.to_tuple()

    def __le__(self, other):
        return self.to_tuple() <= other.to_tuple()

    def __ge__(self, other):
        return self.to_tuple() >= other.to_tuple()


class ChromiumVersion(Version):
    webkit: Version

    def __init__(self, version: Version, webkit: Version = Version(major=537, minor=36)):
        super().__init__(version.major, version.minor, version.build, version.patch)
        self.webkit = webkit


class SafariVersion(Version):
    webkit: Version

    def __init__(self, version: Version, webkit: Version = Version(major=605, minor=1, build=15)):
        super().__init__(version.major, version.minor, version.build, version.patch)
        self.webkit = webkit


class AndroidVersion(Version):
    build_number: Optional[str]
    platform_model: Optional[str]

    def __init__(self, version: Version, build_numbers: Optional[Union[str, tuple, list]] = None):
        super().__init__(version.major, version.minor, version.build, version.patch)
        self.build_number = utils.choice(build_numbers)


class WindowsVersion(Version):
    ch_platform: Version

    def __init__(self, version: Version, ch_platform: Version):
        super().__init__(version.major, version.minor, version.build, version.patch)
        self.ch_platform = ch_platform


VERSION_TYPES = (
    Version,
    ChromiumVersion,
    SafariVersion,
    AndroidVersion,
    WindowsVersion,
)


class VersionRange:
    min_version: Optional[Version]
    max_version: Optional[Version]

    def __init__(self, min_version: Optional[Union[Version, int]] = None, max_version: Optional[Union[Version, int]] = None):
        self.min_version = Version(major=min_version) if isinstance(min_version, int) else min_version
        self.max_version = Version(major=max_version) if isinstance(max_version, int) else max_version

    @staticmethod
    def _lower_bound(version: Version) -> tuple:
        return tuple(
            resolved_part if original_part is not None else 0
            for original_part, resolved_part in zip(version.original, version.to_tuple())
        )

    @staticmethod
    def _upper_bound(version: Version) -> tuple:
        # Treat omitted components as wildcards for upper bounds. This keeps
        # VersionRange(125, 129) matching every 129.x release, while letting
        # Version(10, 15, 7) cap macOS at 10.15.7.
        return tuple(
            resolved_part if original_part is not None else 10 ** 9
            for original_part, resolved_part in zip(version.original, version.to_tuple())
        )

    def filter(self, versions: List[Version]) -> List[Version]:
        tmp_versions: List[Version] = []

        min_version = self._lower_bound(self.min_version) if self.min_version is not None else None
        max_version = self._upper_bound(self.max_version) if self.max_version is not None else None

        for version in versions:
            version_tuple = version.to_tuple()
            if min_version is not None and version_tuple < min_version:
                continue
            if max_version is not None and version_tuple > max_version:
                continue
            if min_version is not None or max_version is not None:
                tmp_versions.append(version)

        return tmp_versions

    def __repr__(self):
        return f"VersionRange(min_version={self.min_version}, max_version={self.max_version})"
