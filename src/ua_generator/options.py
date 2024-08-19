"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
import typing

from src.ua_generator.data.version import VersionRange


class Options:
    weighted_versions: bool = False
    selected_versions: typing.Dict[str, VersionRange] = None

    def __init__(self, weighted_versions: bool = False, selected_versions: typing.Dict[str, VersionRange] = None):
        self.weighted_versions = weighted_versions
        if selected_versions is not None:
            self.selected_versions = selected_versions
