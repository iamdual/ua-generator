"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
import typing

from . import user_agent, options as _options


def generate(device: typing.Union[tuple, str, None] = None,
             platform: typing.Union[tuple, str, None] = None,
             browser: typing.Union[tuple, str, None] = None,
             options: typing.Union[_options.Options, None] = None) -> user_agent.UserAgent:
    return user_agent.UserAgent(device, platform, browser, options)
