"""
Random User-Agent
Copyright: 2022-2025 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
import random
from typing import Union, List

from .. import utils


class Version:
    major: int | None = None
    minor: int | None = None
    build: int | None = None
    patch: int | None = None

    def __init__(self,
                 major: Union[int, tuple] | None = None,
                 minor: Union[int, tuple] | None = None,
                 build: Union[int, tuple] | None = None,
                 patch: Union[int, tuple] | None = None):
        self.major, self.minor, self.build, self.patch = map(
            lambda x:
            # https://docs.python.org/3/tutorial/controlflow.html#tut-unpacking-arguments
            random.randrange(*x) if isinstance(x, tuple) else x,
            (major, minor, build, patch)
        )
        self.__tuple : tuple[int, ...] | None = None

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
    webkit: Version | None = None

    def __init__(self, version: Version, webkit: Version = Version(major=537, minor=36)):
        super().__init__(version.major, version.minor, version.build, version.patch)
        self.webkit = webkit


class AndroidVersion(Version):
    build_number: str | None = None
    platform_model: str | None = None

    def __init__(self, version: Version, build_numbers: Union[str, tuple, list, None] = None):
        super().__init__(version.major, version.minor, version.build, version.patch)
        self.build_number = utils.choice(build_numbers)


class WindowsVersion(Version):
    ch_platform: Version | None = None

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
    min_version: Version | None = None
    max_version: Version | None = None

    def __init__(self, min_version: Union[Version, int] | None = None, max_version: Union[Version, int] | None = None):
        
        if isinstance(min_version, int):
            self.min_version = Version(major=min_version)
        else:
            self.min_version = min_version
        
        if isinstance(max_version, int):
            self.max_version = Version(major=max_version)
        else:
            self.max_version = max_version

    def filter(self, versions: List[Version]) -> List[Version]:
        tmp_versions: List[Version] = []

        # TODO: Perhaps support for full version comparison, instead of just major versions
        for version in versions:
            if (version.major is None):
                continue
            
            include = False
            
            if self.min_version is not None and self.max_version is not None:
                
                if self.min_version.major is not None and self.max_version.major is not None:
                    if self.min_version.major <= version.major <= self.max_version.major:
                        include = True
            
            elif self.min_version is not None and self.max_version is None:
                if self.min_version.major is not None:
                    if self.min_version.major <= version.major:
                        include = True
            
            elif self.min_version is None and self.max_version is not None:
                if self.max_version.major is not None:
                    if version.major <= self.max_version.major:
                        include = True
            
            # elif self.min_version is None and self.max_version is None:
            #     include = True

            if include:
                tmp_versions.append(version)

        return tmp_versions

    def __repr__(self):
        return f"VersionRange(min_version={self.min_version}, max_version={self.max_version})"
