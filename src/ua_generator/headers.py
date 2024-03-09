"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
from .data.generator import Generator
from .client_hints import ClientHints


# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-CH
class Headers:

    def __init__(self, gen: Generator, ch: ClientHints):
        self.__generator = gen
        self.__client_hints = ch
        self.__headers: dict[str, str] = {
            'user-agent': gen.user_agent,
        }

        # https://developer.mozilla.org/en-US/docs/Web/HTTP/Client_hints#low_entropy_hints
        if self.__generator.browser in ('chrome', 'edge'):
            self.add('sec-ch-ua')
            self.add('sec-ch-ua-mobile')
            self.add('sec-ch-ua-platform')

    def add(self, key: str):
        if key == 'sec-ch-ua':
            self.__headers[key] = self.__client_hints.brands
        elif key == 'sec-ch-ua-full-version-list':
            self.__headers[key] = self.__client_hints.brands_full_version_list
        if key == 'sec-ch-ua-platform':
            self.__headers[key] = self.__client_hints.platform
        elif key == 'sec-ch-ua-platform-version':
            self.__headers[key] = self.__client_hints.platform_version
        elif key == 'sec-ch-ua-mobile':
            self.__headers[key] = self.__client_hints.mobile

    def accept_ch(self, val: str):
        if self.__generator.browser not in ('chrome', 'edge'):
            return

        requested_hints = val.split(',')
        for hint in requested_hints:
            self.add(hint.strip().lower())

    def get(self) -> dict[str, str]:
        return self.__headers
