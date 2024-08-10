"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""


class Options:
    weighted_versions = False

    def __init__(self, weighted_versions: bool = False):
        self.weighted_versions = weighted_versions
