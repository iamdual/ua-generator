"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
from . import utils, exceptions
from .data import devices, platforms, platforms_desktop, platforms_mobile, browsers
from .data.generator import Generator
from .client_hints import ClientHints
from .headers import Headers


class UserAgent:
    def __init__(self, device=None, platform=None, browser=None):
        self.device: str = device
        self.platform: str = platform
        self.browser: str = browser
        self.__complete()

        # Type hinting only
        self.text: str
        self.ch: ClientHints
        self.headers: Headers

    def __find_device(self):
        if self.device is not None:
            if not utils.contains_multiple(self.device, devices):
                raise exceptions.InvalidArgumentError('No device type found: {}'.format(self.device))
            else:
                self.device = utils.choice(self.device)
                return self.device

        if self.platform is not None and utils.contains_multiple(self.platform, platforms_desktop):
            self.device = 'desktop'
        elif self.platform is not None and utils.contains_multiple(self.platform, platforms_mobile):
            self.device = 'mobile'
        elif self.device is None:
            self.device = utils.choice(devices)

        return self.device

    def __find_platform(self):
        if self.platform is not None:
            if not utils.contains_multiple(self.platform, platforms):
                raise exceptions.InvalidArgumentError('No platform found: {}'.format(self.platform))
            else:
                self.platform = utils.choice(self.platform)
                return self.platform

        if self.device is not None and 'desktop' in self.device:
            self.platform = utils.choice(platforms_desktop)
        elif self.device is not None and 'mobile' in self.device:
            self.platform = utils.choice(platforms_mobile)
        elif self.platform is None:
            self.platform = utils.choice(platforms)

        return self.platform

    def __find_browser(self):
        if self.browser is not None:
            if not utils.contains_multiple(self.browser, browsers):
                raise exceptions.InvalidArgumentError('No browser found: {}'.format(self.browser))
            else:
                self.browser = utils.choice(self.browser)

        if self.browser is None:
            self.browser = utils.choice(browsers)

        # Safari only support for macOS and iOS
        if self.platform != 'macos' and self.platform != 'ios' and self.browser == 'safari':
            self.browser = 'chrome'

        return self.browser

    def __complete(self):
        self.device = self.__find_device()
        self.platform = self.__find_platform()
        self.browser = self.__find_browser()

        ua = Generator(device=self.device, platform=self.platform, browser=self.browser)
        self.text = ua.user_agent
        self.ch = ClientHints(ua)
        self.headers = Headers(ua, self.ch)

    def __str__(self):
        return self.text
