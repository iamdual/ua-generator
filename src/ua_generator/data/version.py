"""
Random User-Agent
Copyright: 2022-2025 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
import random
from typing import Union, List, Optional

from .. import utils


class Version:
    major: Optional[Union[int]]
    minor: Optional[Union[int]]
    build: Optional[Union[int]]
    patch: Optional[Union[int]]

    def __init__(self,
                 major: Optional[Union[int, tuple]] = None,
                 minor: Optional[Union[int, tuple]] = None,
                 build: Optional[Union[int, tuple]] = None,
                 patch: Optional[Union[int, tuple]] = None):
        self.major, self.minor, self.build, self.patch = map(
            lambda x:
            # https://docs.python.org/3/tutorial/controlflow.html#tut-unpacking-arguments
            random.randrange(*x) if isinstance(x, tuple) else x,
            (major, minor, build, patch)
        )
        self.__tuple: Optional[tuple] = None

    def format(self, partitions=None, separator='.', trim_zero=False) -> str:
        versions = [self.major, self.minor, self.build, self.patch]

        if partitions is not None:
            versions = versions[:partitions]
        else:
            # Stop at None
            while versions and versions[-1] is None:
                versions.pop()

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
    AndroidVersion,
    WindowsVersion,
)


class VersionRange:
    min_version: Optional[Version]
    max_version: Optional[Version]

    def __init__(self, min_version: Optional[Union[Version, int]] = None, max_version: Optional[Union[Version, int]] = None):
        self.min_version = Version(major=min_version) if isinstance(min_version, int) else min_version
        self.max_version = Version(major=max_version) if isinstance(max_version, int) else max_version

    def filter(self, versions: List[Version]) -> List[Version]:
        tmp_versions: List[Version] = []

        # TODO: Perhaps support for full version comparison, instead of just major versions
        for version in versions:
            if isinstance(self.min_version, Version) and isinstance(self.max_version, Version) and self.min_version.major <= int(version.major or 0) <= self.max_version.major: # type: ignore[operator]
                tmp_versions.append(version)
            elif isinstance(self.min_version, Version) and self.max_version is None and self.min_version.major <= int(version.major or 0): # type: ignore[operator]
                tmp_versions.append(version)
            elif self.min_version is None and isinstance(self.max_version, Version) and int(version.major or 0) <= self.max_version.major: # type: ignore[operator]
                tmp_versions.append(version)

        return tmp_versions

    def __repr__(self):
        return f"VersionRange(min_version={self.min_version}, max_version={self.max_version})"
