"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
from typing import Literal

DEVICES = ('desktop', 'mobile')
_DEVICES_TYPE = Literal['desktop', 'mobile', None]

PLATFORMS = ('windows', 'macos', 'ios', 'linux', 'android')
_PLATFORMS_TYPE = Literal['windows', 'macos', 'ios', 'linux', 'android', None]
PLATFORMS_DESKTOP = ('windows', 'macos', 'linux')  # Platforms on desktop devices
PLATFORMS_MOBILE = ('ios', 'android')  # Platforms on mobile devices

BROWSERS = ('chrome', 'edge', 'firefox', 'safari')
_BROWSERS_TYPE = Literal['chrome', 'edge', 'firefox', 'safari', None]
BROWSERS_SUPPORT_CH = ('chrome', 'edge')  # Browsers that support Client Hints
_BROWSERS_SUPPORT_CH_TYPE = Literal['chrome', 'edge', None]
