"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import random
from typing import List

from ..version import Version

# User agent cap on macOS
# https://groups.google.com/a/chromium.org/g/blink-dev/c/hAI4QoX6rEo/m/qQNPThr0AAAJ

# https://support.apple.com/en-us/HT201222
versions: List[Version] = [
    Version(major=10, minor=11, build=(0, 6)),
    Version(major=10, minor=12, build=(0, 6)),
    Version(major=10, minor=13, build=(0, 6)),
    Version(major=10, minor=14, build=(0, 6)),
    Version(major=10, minor=15, build=(0, 7)),
    Version(major=11, minor=0, build=(0, 0)),
    Version(major=11, minor=2, build=(0, 3)),
    Version(major=11, minor=3, build=(0, 1)),
    Version(major=11, minor=5, build=(0, 2)),
    Version(major=11, minor=6, build=(0, 6)),
    Version(major=12, minor=0, build=(0, 1)),
    Version(major=12, minor=2, build=(0, 1)),
    Version(major=12, minor=3, build=(0, 1)),
    Version(major=12, minor=4, build=(0, 0)),
    Version(major=12, minor=5, build=(0, 1)),
    Version(major=12, minor=6, build=(0, 4)),
    Version(major=12, minor=7, build=(0, 5)),
    Version(major=13, minor=0, build=(0, 1)),
    Version(major=13, minor=1, build=(0, 0)),
    Version(major=13, minor=2, build=(0, 1)),
    Version(major=13, minor=3, build=(0, 1)),
    Version(major=13, minor=4, build=(0, 1)),
    Version(major=13, minor=5, build=(0, 2)),
    Version(major=14, minor=0, build=(0, 1)),
    Version(major=14, minor=1, build=(0, 2)),
    Version(major=14, minor=2, build=(0, 1)),
    Version(major=14, minor=3, build=(0, 1)),
    Version(major=14, minor=4, build=(0, 1)),
    Version(major=14, minor=5, build=(0, 0)),
]

version_weights = [1.0] * len(versions)
version_weights[-1] = 10.0
version_weights[-2] = 9.0
version_weights[-2] = 8.0
version_weights[-3] = 8.0


def get_version() -> Version:
    choice: List[Version] = random.choices(versions, weights=version_weights, k=1)
    return choice[0]
