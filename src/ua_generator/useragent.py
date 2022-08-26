"""
Random User-Agent
Copyright: 2022 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
from . import utils, formats, exceptions
from .data import devices, platforms, platforms_desktop, platforms_mobile, browsers
from .data import generator


class UserAgent:
    def __init__(self):
        self.device = None
        self.platform = None
        self.platform_version = None
        self.browser = None
        self.browser_version = None
        self.text = None
        self.ch: ClientHints = None

    def generate(self, device=None, platform=None, browser=None):
        self.device = device
        self.platform = platform
        self.browser = browser
        self.complete()
        return self

    def find_device(self):
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

    def find_platform(self):
        if self.platform is not None:
            if not utils.contains_multiple(self.platform, platforms):
                raise exceptions.InvalidArgumentError('No platform found: {}'.format(self.platform))
            else:
                self.platform = utils.choice(self.platform)
                return self.platform

        if self.device is not None and utils.contains(self.device, 'desktop'):
            self.platform = utils.choice(platforms_desktop)
        elif self.device is not None and utils.contains(self.device, 'mobile'):
            self.platform = utils.choice(platforms_mobile)
        elif self.platform is None:
            self.platform = utils.choice(platforms)

        return self.platform

    def find_browser(self):
        if self.browser is not None:
            if not utils.contains_multiple(self.browser, browsers):
                raise exceptions.InvalidArgumentError('No browser found: {}'.format(self.browser))
            else:
                self.browser = utils.choice(self.browser)

        if self.browser is None:
            self.browser = utils.choice(browsers)

        '''Safari only support for macOS and iOS'''
        if self.platform != 'macos' and self.platform != 'ios' and self.browser == 'safari':
            self.browser = 'chrome'

        return self.browser

    def complete(self):
        self.device = self.find_device()
        self.platform = self.find_platform()
        self.browser = self.find_browser()

        ua = generator.Generator(device=self.device, platform=self.platform, browser=self.browser)
        self.platform_version = ua.platform_version
        self.browser_version = ua.browser_version
        self.text = ua.user_agent
        self.ch = ClientHints(ua)

    def __str__(self):
        return self.text


# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-CH-UA
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-CH-UA-Full-Version-List
class ClientHints:
    def __init__(self, _gen: generator.Generator):
        self.mobile = self.ch_mobile(_gen.platform)
        self.platform = self.ch_platform(_gen.platform)
        self.platform_version = self.ch_platform_version(_gen.platform_version)
        self.brands = self.ch_brands(_gen)
        self.brands_full_version_list = self.ch_brands(_gen, full_version_list=True)

    def ch_mobile(self, platform: str):
        if utils.contains(('ios', 'android'), platform):
            return '?1'
        return '?0'

    def ch_platform(self, platform: str):
        if platform == 'ios':
            platform = 'iOS'
        elif platform == 'macos':
            platform = 'macOS'
        else:
            platform = platform.title()
        return '"' + platform + '"'

    def ch_platform_version(self, platform_version):
        return '"' + formats.version(platform_version) + '"'

    def ch_brands(self, _gen: generator.Generator, full_version_list: bool = False):
        brand_list = [{'brand': ' Not A;Brand', 'version': '99'}]

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

        return self.serialize_brand_list(brand_list)

    def serialize_brand_list(self, brand_list: list):
        serialized = []
        for _dict in brand_list:
            serialized.append('"' + _dict['brand'] + '";v="' + _dict['version'] + '"')
        return ', '.join(serialized)

    def __str__(self):
        return self.brands