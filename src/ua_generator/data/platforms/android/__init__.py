"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
import random

from . import android_samsung, android_pixel, android_nexus
from ...version import AndroidVersion


def get_version() -> AndroidVersion:
    choice = random.randint(0, 6)

    if choice == 0:
        return android_nexus.get_version()
    if choice == 1:
        return android_pixel.get_version()

    return android_samsung.get_version()
