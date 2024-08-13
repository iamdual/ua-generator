"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
from . import utils, exceptions
from .data import platforms, browsers  # TODO: learn why the error is triggered when moving this to the bottom
from .client_hints import ClientHints
from .data import devices, platforms_desktop, platforms_mobile
from .data.generator import Generator
from .headers import Headers
from .options import Options


class UserAgent:
    def __init__(self, device=None, platform=None, browser=None, options=None):
        self.device: str = utils.choice(device)
        self.platform: str = utils.choice(platform)
        self.browser: str = utils.choice(browser)
        self.options: Options = options if options is not None else Options()
        self.__complete()

        # Type hinting only
        self.text: str
        self.ch: ClientHints
        self.headers: Headers

    def __find_device(self) -> str:
        if self.device is not None and self.device not in devices:
            raise exceptions.InvalidArgumentError('No such device type found: {}'.format(self.device))

        # Override the device type, if the platform is specified
        if self.platform is not None:
            if self.platform in platforms_desktop:
                self.device = 'desktop'
            elif self.platform in platforms_mobile:
                self.device = 'mobile'

        if self.device is None:
            self.device = utils.choice(devices)

        return self.device

    def __find_platform(self) -> str:
        if self.platform is not None and self.platform not in platforms:
            raise exceptions.InvalidArgumentError('No such platform found: {}'.format(self.platform))

        # Make the platform consistent with the device type and browser
        if self.device == 'desktop' and self.platform not in platforms_desktop:
            # Safari only supports the macOS and iOS platforms
            if self.browser is not None and self.browser == 'safari':
                self.platform = utils.choice(('macos', 'ios'))
            else:
                self.platform = utils.choice(platforms_desktop)
        elif self.device == 'mobile' and self.platform not in platforms_mobile:
            self.platform = utils.choice(platforms_mobile)

        if self.platform is None:
            self.platform = utils.choice(platforms)

        return self.platform

    def __find_browser(self) -> str:
        if self.browser is not None and self.browser not in browsers:
            raise exceptions.InvalidArgumentError('No such browser found: {}'.format(self.browser))

        if self.browser is None:
            self.browser = utils.choice(browsers)

        # Safari only supports the macOS and iOS platforms
        if self.browser == 'safari' and self.platform not in ('macos', 'ios'):
            self.browser = 'chrome'

        return self.browser

    def __complete(self):
        self.device = self.__find_device()
        self.platform = self.__find_platform()
        self.browser = self.__find_browser()

        ua = Generator(device=self.device, platform=self.platform, browser=self.browser, options=self.options)
        self.text = ua.user_agent
        self.ch = ClientHints(ua)
        self.headers = Headers(ua, self.ch)

    def __str__(self):
        return self.text
