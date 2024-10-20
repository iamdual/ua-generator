"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
import typing

from . import user_agent, options as _options, data as _data


def generate(
    device: typing.Union[tuple[_data._DEVICES_TYPE], _data._DEVICES_TYPE, None] = None,
    platform: typing.Union[tuple[_data._PLATFORMS_TYPE], _data._PLATFORMS_TYPE, None] = None,
    browser: typing.Union[tuple[_data._BROWSERS_TYPE], _data._BROWSERS_TYPE, None] = None,
    options: typing.Union[_options.Options, None] = None
):
    return user_agent.UserAgent(device, platform, browser, options)
