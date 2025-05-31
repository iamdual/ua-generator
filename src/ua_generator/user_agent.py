"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
from typing import Union, Optional

from . import utils
from .client_hints import ClientHints
from .data import DEVICES, BROWSERS, PLATFORMS, PLATFORMS_DESKTOP, PLATFORMS_MOBILE, T_DEVICES, T_PLATFORMS, T_BROWSERS
from .data.generator import Generator
from .headers import Headers
from .options import Options


class UserAgent:
    def __init__(self,
                 device: Optional[Union[T_DEVICES, tuple, list]] = None,
                 platform: Optional[Union[T_PLATFORMS, tuple, list]] = None,
                 browser: Optional[Union[T_BROWSERS, tuple, list]] = None,
                 options: Optional[Union[Options]] = None):

        self.device: Optional[Union[str]] = utils.choice(device) if device else None
        self.platform: Optional[Union[str]] = utils.choice(platform) if platform else None
        self.browser: Optional[Union[str]] = utils.choice(browser) if browser else None
        self.options: Options = options if options else Options()
        self.__complete()

        # Type hinting only
        self.text: str
        self.ch: ClientHints
        self.headers: Headers
        self.generator: Generator

    def __find_device(self) -> str:
        if self.device is not None and self.device not in DEVICES:
            raise ValueError('No such device type found: {}'.format(self.device))

        # Override the device type, if the platform is specified
        if self.platform is not None:
            if self.platform in PLATFORMS_DESKTOP:
                self.device = 'desktop'
            elif self.platform in PLATFORMS_MOBILE:
                self.device = 'mobile'

        if self.device is None:
            self.device = utils.choice(DEVICES)

        assert self.device is not None
        return self.device

    def __find_platform(self) -> str:
        if self.platform is not None and self.platform not in PLATFORMS:
            raise ValueError('No such platform found: {}'.format(self.platform))

        # Make the platform consistent with the device type and browser
        if self.device == 'desktop' and self.platform not in PLATFORMS_DESKTOP:
            # Safari only supports the macOS and iOS platforms
            if self.browser is not None and self.browser == 'safari':
                self.platform = utils.choice(('macos', 'ios'))
            else:
                self.platform = utils.choice(PLATFORMS_DESKTOP)
        elif self.device == 'mobile' and self.platform not in PLATFORMS_MOBILE:
            self.platform = utils.choice(PLATFORMS_MOBILE)

        if self.platform is None:
            self.platform = utils.choice(PLATFORMS)

        assert self.platform is not None
        return self.platform

    def __find_browser(self) -> str:
        if self.browser is not None and self.browser not in BROWSERS:
            raise ValueError('No such browser found: {}'.format(self.browser))

        if self.browser is None:
            self.browser = utils.choice(BROWSERS)

        # Safari only supports the macOS and iOS platforms
        if self.browser == 'safari' and self.platform not in ('macos', 'ios'):
            self.browser = 'chrome'

        assert self.browser is not None
        return self.browser

    def __complete(self):
        self.device = self.__find_device()
        self.platform = self.__find_platform()
        self.browser = self.__find_browser()

        ua = Generator(device=self.device, platform=self.platform, browser=self.browser, options=self.options)
        self.text = ua.user_agent
        self.ch = ClientHints(ua)
        self.headers = Headers(ua, self.ch)
        self.generator = ua

    def __str__(self):
        return self.text

    def __repr__(self):
        return f"UserAgent(device='{self.device}', platform='{self.platform}', browser='{self.browser}')"
