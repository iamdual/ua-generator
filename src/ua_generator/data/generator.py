"""
Random User-Agent
Copyright: 2022 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
from .browsers import chrome, safari, firefox
from .platforms import ios, android, linux, windows, macos
from .. import formats, utils, exceptions


class Generator:
    def __init__(self, device, platform, browser):
        self.device = device
        self.platform = platform
        self.browser = browser

        self.platform_version = self.generate_platform_version()
        self.browser_version = self.generate_browser_version()
        self.user_agent = self.generate_user_agent()

    def generate_platform_version(self):
        if self.platform == 'windows':
            return windows.get_version()
        elif self.platform == 'macos':
            return macos.get_version()
        elif self.platform == 'ios':
            return ios.get_version()
        elif self.platform == 'linux':
            return linux.get_version()
        elif self.platform == 'android':
            return android.get_version()

    def generate_browser_version(self):
        if self.browser == 'chrome':
            return chrome.get_version()
        elif self.browser == 'safari':
            return safari.get_version()
        elif self.browser == 'firefox':
            return firefox.get_version()

    def generate_user_agent(self):
        if self.platform == 'windows':
            if self.browser == 'chrome':
                template = utils.choice((
                    'Mozilla/5.0 (Windows NT {windows}; Win64; x64) AppleWebKit/{webkit} (KHTML, like Gecko) Chrome/{chrome} Safari/{webkit}',
                    'Mozilla/5.0 (Windows NT {windows}; WOW64) AppleWebKit/{webkit} (KHTML, like Gecko) Chrome/{chrome} Safari/{webkit}'
                ))
                template = template.replace('{windows}', self.platform_version['major'])
                template = template.replace('{webkit}', self.browser_version['webkit'])
                template = template.replace('{chrome}', formats.version(self.browser_version))
                return template
            if self.browser == 'firefox':
                template = utils.choice((
                    'Mozilla/5.0 (Windows NT {windows}; Win64; x64; rv:{firefox}) Gecko/20100101 Firefox/{firefox}',
                    'Mozilla/5.0 (Windows NT {windows}; WOW64; rv:{firefox}) Gecko/20100101 Firefox/{firefox}',
                ))
                template = template.replace('{windows}', self.platform_version['major'])
                template = template.replace('{firefox}', formats.version(self.browser_version))
                return template

        elif self.platform == 'linux':
            if self.browser == 'chrome':
                template = utils.choice((
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/{webkit} (KHTML, like Gecko) Chrome/{chrome} Safari/{webkit}',
                    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/{webkit} (KHTML, like Gecko) Chrome/{chrome} Safari/{webkit}',
                ))
                template = template.replace('{windows}', self.platform_version['major'])
                template = template.replace('{webkit}', self.browser_version['webkit'])
                template = template.replace('{chrome}', formats.version(self.browser_version))
                return template
            if self.browser == 'firefox':
                template = utils.choice((
                    'Mozilla/5.0 (X11; Linux x86_64; rv:{firefox}) Gecko/20100101 Firefox/{firefox}',
                    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:{firefox}) Gecko/20100101 Firefox/{firefox}',
                ))
                template = template.replace('{linux}', self.platform_version['major'])
                template = template.replace('{firefox}', formats.version(self.browser_version))
                return template

        elif self.platform == 'android' and self.device == 'mobile':
            if self.browser == 'chrome':
                template = 'Mozilla/5.0 (Linux; Android {android}{device}{build}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Mobile Safari/537.36'
                template = template.replace('{android}', self.platform_version['major'].replace('.0', ''))
                if 'device_name' in self.platform_version and self.platform_version['device_name']:
                    template = template.replace('{device}', '; ' + self.platform_version['device_name'])
                if 'build_number' in self.platform_version and self.platform_version['build_number']:
                    template = template.replace('{build}', '; Build/' + self.platform_version['build_number'])
                template = template.replace('{build}', '').replace('{device}', '')
                template = template.replace('{chrome}', formats.version(self.browser_version))
                return template
            if self.browser == 'firefox':
                template = 'Mozilla/5.0 (Android {android}; Mobile; rv:{firefox}) Gecko/{firefox} Firefox/{firefox}'
                template = template.replace('{android}', self.platform_version['major'].replace('.0', ''))
                template = template.replace('{firefox}', formats.version(self.browser_version))
                return template

        elif self.platform == 'macos':
            if self.browser == 'chrome':
                template = 'Mozilla/5.0 (Macintosh; Intel Mac OS X {macos}) AppleWebKit/{webkit} (KHTML, like Gecko) Chrome/{chrome} Safari/{webkit}'
                template = template.replace('{macos}',
                                            formats.version(self.platform_version, strip_zero=True).replace('.', '_'))
                template = template.replace('{webkit}', self.browser_version['webkit'])
                template = template.replace('{chrome}', formats.version(self.browser_version))
                return template
            if self.browser == 'safari':
                template = 'Mozilla/5.0 (Macintosh; Intel Mac OS X {macos}) AppleWebKit/{webkit} (KHTML, like Gecko) Version/{safari} Safari/{webkit}'
                template = template.replace('{macos}',
                                            formats.version(self.platform_version, strip_zero=True).replace('.', '_'))
                template = template.replace('{webkit}', self.browser_version['webkit'])
                template = template.replace('{safari}', formats.version(self.browser_version))
                return template
            if self.browser == 'firefox':
                template = 'Mozilla/5.0 (Macintosh; Intel Mac OS X {macos}; rv:{firefox}) Gecko/20100101 Firefox/{firefox}'
                template = template.replace('{macos}',
                                            formats.version(self.platform_version, strip_zero=True).replace('.', '_'))
                template = template.replace('{firefox}', formats.version(self.browser_version))
                return template

        elif self.platform == 'ios':
            if self.browser == 'chrome':
                template = 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/{webkit} (KHTML, like Gecko) CriOS/{chrome} Mobile/15E148 Safari/{webkit}'
                template = template.replace('{ios}',
                                            formats.version(self.platform_version, strip_zero=True).replace('.', '_'))
                template = template.replace('{webkit}', self.browser_version['webkit'])
                template = template.replace('{chrome}', formats.version(self.browser_version))
                return template
            if self.browser == 'safari':
                template = 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/{webkit} (KHTML, like Gecko) Version/{safari} Mobile/15E148 Safari/{webkit}'
                template = template.replace('{ios}',
                                            formats.version(self.platform_version, strip_zero=True).replace('.', '_'))
                template = template.replace('{webkit}', self.browser_version['webkit'])
                template = template.replace('{safari}', formats.version(self.browser_version))
                return template
            if self.browser == 'firefox':
                template = 'Mozilla/5.0 (iPhone; CPU iPhone OS {ios} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/{firefox} Mobile/15E148 Safari/605.1.15'
                template = template.replace('{ios}',
                                            formats.version(self.platform_version, strip_zero=True).replace('.', '_'))
                template = template.replace('{firefox}', formats.version(self.browser_version))
                return template

        raise exceptions.CannotGenerateError(self)
