"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
from typing import Union

from . import user_agent, options as _options, data as _data


def generate(device: Union[_data.T_DEVICES, tuple, list, None] = None,
             platform: Union[_data.T_PLATFORMS, tuple, list, None] = None,
             browser: Union[_data.T_BROWSERS, tuple, list, None] = None,
             options: Union[_options.Options, None] = None) -> user_agent.UserAgent:
    return user_agent.UserAgent(device, platform, browser, options)
