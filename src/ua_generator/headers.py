"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
from .client_hints import ClientHints
from .data import BROWSERS_SUPPORT_CH
from .data.generator import Generator


# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-CH
class Headers:

    def __init__(self, gen: Generator, ch: ClientHints):
        self.__generator = gen
        self.__client_hints = ch
        self.__is_generated = False
        self.__headers: dict[str, str] = {}

    def reset(self):
        self.__is_generated = True
        self.__headers = {
            'user-agent': self.__generator.user_agent,
        }

        # https://developer.mozilla.org/en-US/docs/Web/HTTP/Client_hints#low_entropy_hints
        if self.__generator.browser in BROWSERS_SUPPORT_CH:
            self.add('sec-ch-ua')
            self.add('sec-ch-ua-mobile')
            self.add('sec-ch-ua-platform')

    def add(self, key: str):
        if not self.__is_generated:
            self.reset()

        if key == 'sec-ch-ua':
            self.__headers[key] = self.__client_hints.brands
        elif key == 'sec-ch-ua-full-version-list':
            self.__headers[key] = self.__client_hints.brands_full_version_list
        elif key == 'sec-ch-ua-platform':
            self.__headers[key] = self.__client_hints.platform
        elif key == 'sec-ch-ua-platform-version':
            self.__headers[key] = self.__client_hints.platform_version
        elif key == 'sec-ch-ua-mobile':
            self.__headers[key] = self.__client_hints.mobile
        elif key == 'sec-ch-ua-bitness':
            self.__headers[key] = self.__client_hints.bitness
        elif key == 'sec-ch-ua-arch':
            self.__headers[key] = self.__client_hints.architecture
        elif key == 'sec-ch-ua-model':
            self.__headers[key] = self.__client_hints.model
        elif key == 'sec-ch-ua-wow64':
            self.__headers[key] = self.__client_hints.wow64

    def accept_ch(self, val: str):
        self.reset()

        if self.__generator.browser not in BROWSERS_SUPPORT_CH:
            return

        requested_hints = val.split(',')
        for hint in requested_hints:
            self.add(hint.strip().lower())

    def get(self) -> dict[str, str]:
        if not self.__is_generated:
            self.reset()

        return self.__headers

    def __str__(self):
        text = ""
        for k, v in self.get().items():
            text += f"{k}: {v}\n"
        return text
