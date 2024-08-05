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
            random.choice(x) if isinstance(x, tuple) else x,
            (major, minor, build, patch)
        )

    def __str__(self):
        if self.patch is not None:
            return "%d.%d.%d.%d" % (self.major, self.minor, self.build, self.patch)
        if self.build is not None:
            return "%d.%d.%d" % (self.major, self.minor, self.build)
        if self.minor is not None:
            return "%d.%d" % (self.major, self.minor)
        if self.major is not None:
            return "%d" % (self.major)


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
        self.webkit = ch_platform


version_types = (
    Version,
    ChromiumVersion,
    AndroidVersion,
    WindowsVersion,
)
