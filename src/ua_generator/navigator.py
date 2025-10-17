"""
Random User-Agent
Copyright: 2022-2025 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
from typing import Any

from .client_hints import ClientHints
from .data.generator import Generator


# https://developer.mozilla.org/en-US/docs/Web/API/Navigator/userAgentData
# https://developer.mozilla.org/en-US/docs/Web/API/NavigatorUAData
class Navigator:
    # Type hinting only
    brands: list
    mobile: bool
    platform: str
    architecture: str
    bitness: str
    fullVersionList: list
    model: str
    platformVersion: str
    wow64: bool

    def __init__(self, gen: Generator, ch: ClientHints):
        self.__generator = gen
        self.__client_hints = ch
        self.__is_generated = False
        self.__props: dict[str, Any] = {}

    def __generate(self):
        self.__props = {
            'brands': self.__client_hints.get_brands(),
            'mobile': self.__client_hints.get_mobile(),
            'platform': self.__client_hints.get_platform(),
            'architecture': self.__client_hints.get_architecture(),
            'bitness': self.__client_hints.get_bitness(),
            'fullVersionList': self.__client_hints.get_brands(full_version_list=True),
            'model': self.__client_hints.get_model(),
            'platformVersion': self.__client_hints.get_platform_version(),
            'wow64': self.__client_hints.get_wow64(),
        }
        self.__is_generated = True

    def get(self) -> dict[str, Any]:
        if self.__is_generated:
            return self.__props

        self.__generate()
        return self.__props

    def __getattr__(self, name) -> Any:
        if name in self.__props:
            return self.__props[name]

        self.__generate()
        return self.__props[name]
