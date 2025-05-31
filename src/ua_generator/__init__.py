"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
from typing import Union, Optional

from . import user_agent, options as _options, data as _data


def generate(device: Optional[Union[_data.T_DEVICES, tuple, list]] = None,
             platform: Optional[Union[_data.T_PLATFORMS, tuple, list]] = None,
             browser: Optional[Union[_data.T_BROWSERS, tuple, list]] = None,
             options: Optional[Union[_options.Options]] = None) -> user_agent.UserAgent:
    return user_agent.UserAgent(device, platform, browser, options)
