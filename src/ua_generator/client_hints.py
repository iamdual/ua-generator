"""
Random User-Agent
Copyright: 2022 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
from . import utils, formats, serialization
from .data import platforms_mobile
from .data import generator


# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-CH-UA
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-CH-UA-Full-Version-List
class ClientHints:
    def __init__(self, _gen: generator.Generator):
        self.mobile = serialization.ch_bool(self.__mobile(_gen.platform))
        self.platform = serialization.ch_string(self.__platform(_gen.platform))
        self.platform_version = serialization.ch_string(self.__platform_version(_gen.platform_version))
        self.brands = serialization.ch_brand_list(self.__brands(_gen))
        self.brands_full_version_list = serialization.ch_brand_list(self.__brands(_gen, full_version_list=True))

    def __mobile(self, platform: str):
        return utils.contains(platforms_mobile, platform)

    def __platform(self, platform: str):
        if platform == 'ios':
            platform = 'iOS'
        elif platform == 'macos':
            platform = 'macOS'
        else:
            platform = platform.title()
        return platform

    def __platform_version(self, platform_version):
        return formats.version(platform_version)

    def __brands(self, _gen: generator.Generator, full_version_list: bool = False):
        brand_list = [{'brand': 'Not A(Brand', 'version': '99'}]

        if full_version_list:
            browser_version = formats.version(_gen.browser_version)
        else:
            browser_version = formats.major_version(_gen.browser_version)

        if _gen.browser == 'chrome':
            brand_list.append({'brand': 'Chromium', 'version': browser_version})
            brand_list.append({'brand': 'Google Chrome', 'version': browser_version})
        elif _gen.browser == 'edge':
            brand_list.append({'brand': 'Chromium', 'version': browser_version})
            brand_list.append({'brand': 'Microsoft Edge', 'version': browser_version})

        return brand_list

    def __str__(self):
        return self.brands
