"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
import random

from . import android_samsung, android_pixel, android_nexus
from ...version import AndroidVersion
from ....options import Options


def get_version(options: Options) -> AndroidVersion:
    choice = random.randint(0, 10)

    if choice == 0:
        return android_nexus.get_version(options=options)
    if choice == 1:
        return android_pixel.get_version(options=options)

    return android_samsung.get_version(options=options)
