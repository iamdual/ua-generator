"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
from typing import Literal

DEVICES = ('desktop', 'mobile')
T_DEVICES = Literal['desktop', 'mobile']

PLATFORMS = ('windows', 'macos', 'ios', 'linux', 'android')
T_PLATFORMS = Literal['windows', 'macos', 'ios', 'linux', 'android']
PLATFORMS_DESKTOP = ('windows', 'macos', 'linux')  # Platforms on desktop devices
PLATFORMS_MOBILE = ('ios', 'android')  # Platforms on mobile devices

BROWSERS = ('chrome', 'edge', 'firefox', 'safari')
T_BROWSERS = Literal['chrome', 'edge', 'firefox', 'safari']
BROWSERS_SUPPORT_CH = ('chrome', 'edge')  # Browsers that support Client Hints
