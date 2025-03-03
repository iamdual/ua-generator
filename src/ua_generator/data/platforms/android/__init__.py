"""
Random User-Agent
Copyright: 2022-2025 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
import random

from . import android_samsung, android_pixel, android_xiaomi, android_oppo
from ...version import AndroidVersion
from ....options import Options


def get_version(options: Options) -> AndroidVersion:
    choice = random.randint(0, 20)

    if choice < 2:
        return android_pixel.get_version(options=options)
    if choice < 4:
        return android_oppo.get_version(options=options)
    if choice < 10:
        return android_xiaomi.get_version(options=options)

    return android_samsung.get_version(options=options)
