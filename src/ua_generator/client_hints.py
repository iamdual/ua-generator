"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
from random import Random

from . import serialization
from .data import generator, PLATFORMS_MOBILE
from .data.version import AndroidVersion, WindowsVersion


# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-CH-UA
# https://wicg.github.io/ua-client-hints/#http-ua-hints
class ClientHints:
    # Type hinting only
    mobile: str
    platform: str
    platform_version: str
    brands: str
    brands_full_version_list: str
    bitness: str
    architecture: str
    model: str
    wow64: str

    def __init__(self, gen: generator.Generator):
        self.__generator = gen
        self.__cache: dict[str, str] = {}

    def get_mobile(self) -> bool:
        return self.__generator.platform in PLATFORMS_MOBILE

    def get_platform(self) -> str:
        platform = self.__generator.platform

        if platform == 'ios':
            platform = 'iOS'
        elif platform == 'macos':
            platform = 'macOS'
        else:
            platform = platform.title()

        return platform

    def get_platform_version(self) -> str:
        if type(self.__generator.platform_version) is WindowsVersion:
            return self.__generator.platform_version.ch_platform.format(partitions=3)

        return str(self.__generator.platform_version)

    def get_brands(self, full_version_list: bool = False) -> list:
        brand_list = [{'brand': 'Not A(Brand', 'version': '99.0.0.0' if full_version_list else '99'}]

        if self.__generator.browser == 'chrome':
            browser_version = self.get_browser_version(full_version=full_version_list)
            brand_list.append({'brand': 'Chromium', 'version': browser_version})
            brand_list.append({'brand': 'Google Chrome', 'version': browser_version})
        elif self.__generator.browser == 'edge':
            browser_version = self.get_browser_version(full_version=full_version_list)
            brand_list.append({'brand': 'Chromium', 'version': browser_version})
            brand_list.append({'brand': 'Microsoft Edge', 'version': browser_version})

        return brand_list

    def get_browser_version(self, full_version: bool = True) -> str:
        if full_version:
            return str(self.__generator.browser_version)
        else:
            return str(self.__generator.browser_version.major)

    def get_bitness(self) -> str:
        if self.__generator.platform == 'android':
            _random = Random(self.__generator.user_agent)
            return _random.choice(('32', '64', '32', '32'))

        return '64'

    def get_architecture(self) -> str:
        if self.__generator.platform == 'android' or self.__generator.platform == 'ios':
            return 'arm'
        elif self.__generator.platform == 'macos':
            _random = Random(self.__generator.user_agent)
            return _random.choice(('arm', 'x86', 'arm', 'arm'))

        return 'x86'

    def get_model(self) -> str:
        if type(self.__generator.platform_version) is AndroidVersion:
            return self.__generator.platform_version.platform_model or ''

        return ''

    def get_wow64(self) -> bool:
        return self.__generator.platform == 'windows'

    def __getattr__(self, name) -> str:
        if name in self.__cache:
            return self.__cache[name]

        if name == 'mobile':
            self.__cache[name] = serialization.ch_bool(self.get_mobile())
        elif name == 'platform':
            self.__cache[name] = serialization.ch_string(self.get_platform())
        elif name == 'platform_version':
            self.__cache[name] = serialization.ch_string(self.get_platform_version())
        elif name == 'brands':
            self.__cache[name] = serialization.ch_brand_list(self.get_brands())
        elif name == 'brands_full_version_list':
            self.__cache[name] = serialization.ch_brand_list(self.get_brands(full_version_list=True))
        elif name == 'bitness':
            self.__cache[name] = serialization.ch_string(self.get_bitness())
        elif name == 'architecture':
            self.__cache[name] = serialization.ch_string(self.get_architecture())
        elif name == 'model':
            self.__cache[name] = serialization.ch_string(self.get_model())
        elif name == 'wow64':
            self.__cache[name] = serialization.ch_bool(self.get_wow64())
        else:
            raise AttributeError('Invalid attribute: {}'.format(name))

        return self.__cache[name]

    def __str__(self):
        return self.brands

    def __repr__(self):
        return (f"ClientHints("
                f"mobile={self.mobile}, "
                f"platform={self.platform}, "
                f"platform_version={self.platform_version}, "
                f"brands_full_version_list={self.brands_full_version_list}, "
                f"bitness={self.bitness}, "
                f"architecture={self.architecture}, "
                f"model={self.model}, "
                f"wow64={self.wow64}"
                f")")
