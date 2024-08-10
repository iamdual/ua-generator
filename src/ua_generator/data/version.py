"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
import random
from typing import Union


class Version:
    major: int = None
    minor: int = None
    build: int = None
    patch: int = None

    def __init__(self,
                 major: Union[int, tuple] = None,
                 minor: Union[int, tuple] = None,
                 build: Union[int, tuple] = None,
                 patch: Union[int, tuple] = None):
        self.major, self.minor, self.build, self.patch = map(
            lambda x:
            # https://docs.python.org/3/tutorial/controlflow.html#tut-unpacking-arguments
            random.randrange(*x) if isinstance(x, tuple) else x,
            (major, minor, build, patch)
        )

    def format(self, partitions=None) -> str:
        if partitions == 4 or (partitions is None and self.patch is not None):
            return "%d.%d.%d.%d" % (self.major or 0, self.minor or 0, self.build or 0, self.patch or 0)
        if partitions == 3 or (partitions is None and self.build is not None):
            return "%d.%d.%d" % (self.major or 0, self.minor or 0, self.build or 0)
        if partitions == 2 or (partitions is None and self.minor is not None):
            return "%d.%d" % (self.major or 0, self.minor or 0)

        return "%d" % self.major or 0

    def __str__(self):
        return self.format()


class ChromiumVersion(Version):
    webkit: Version = None

    def __init__(self, version: Version, webkit: Version = Version(major=537, minor=36)):
        super().__init__(version.major, version.minor, version.build, version.patch)
        self.webkit = webkit


class AndroidVersion(Version):
    build_number: str = None
    platform_model: str = None

    def __init__(self, version: Version, build_numbers: tuple = None):
        super().__init__(version.major, version.minor, version.build, version.patch)
        if build_numbers is not None:
            self.build_number = random.choice(build_numbers)


class WindowsVersion(Version):
    ch_platform: Version = None

    def __init__(self, version: Version, ch_platform: Version):
        super().__init__(version.major, version.minor, version.build, version.patch)
        self.ch_platform = ch_platform


version_types = (
    Version,
    ChromiumVersion,
    AndroidVersion,
    WindowsVersion,
)
