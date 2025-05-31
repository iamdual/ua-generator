"""
Random User-Agent
Copyright: 2022-2025 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
import random
from typing import List

from ...filterer import Filterer
from ...version import Version, AndroidVersion
from ....options import Options

# https://en.wikipedia.org/wiki/Android_version_history
# https://source.android.com/setup/start/build-numbers
versions: List[AndroidVersion] = [
    AndroidVersion(Version(major=8, minor=0, build=0), build_numbers=('OPR6.{d}.{v}', 'OPR5.{d}.{v}', 'OPR4.{d}.{v}', 'OPR3.{d}.{v}', 'OPR2.{d}.{v}', 'OPR1.{d}.{v}', 'OPD3.{d}.{v}', 'OPD2.{d}.{v}', 'OPD1.{d}.{v}')),
    AndroidVersion(Version(major=8, minor=1, build=0), build_numbers=('OPM8.{d}.{v}', 'OPM7.{d}.{v}', 'OPM6.{d}.{v}', 'OPM5.{d}.{v}', 'OPM4.{d}.{v}', 'OPM3.{d}.{v}', 'OPM2.{d}.{v}')),
    AndroidVersion(Version(major=9, minor=0, build=0), build_numbers=('PQ3B.{d}.{v}', 'PQ3A.{d}.{v}', 'PQ2A.{d}.{v}', 'PQ1A.{d}.{v}', 'PPR2.{d}.{v}', 'PPR1.{d}.{v}')),
    AndroidVersion(Version(major=10, minor=0, build=0), build_numbers=('QD4A.{d}.{v}', 'QQ3A.{d}.{v}', 'QQ2A.{d}.{v}', 'QQ1D.{d}.{v}', 'QQ1C.{d}.{v}', 'QQ1B.{d}.{v}', 'QQ1A.{d}.{v}', 'QP1A.{d}.{v}', 'QD1A.{d}.{v}')),
    AndroidVersion(Version(major=11, minor=0, build=0), build_numbers=('RD2A.{d}.{v}', 'RQ3A.{d}.{v}', 'RQ2A.{d}.{v}', 'RQ1D.{d}.{v}', 'RQ1C.{d}.{v}', 'RQ1A.{d}.{v}', 'RD1B.{d}.{v}', 'RD1A.{d}.{v}', 'RP1A.{d}.{v}')),
    AndroidVersion(Version(major=12, minor=0, build=0), build_numbers=('SP1A.{d}.{v}', 'SQ1D.{d}.{v}', 'SD1A.{d}.{v}')),
    AndroidVersion(Version(major=12, minor=1, build=0), build_numbers=('SP2A.{d}.{v}', 'SD2A.{d}.{v}', 'SQ3A.{d}.{v}')),
    AndroidVersion(Version(major=13, minor=0, build=0), build_numbers=('TQ3A.{d}.{v}', 'TQ3C.{d}.{v}', 'TQ2B.{d}.{v}', 'TD4A.{d}.{v}', 'TQ2A.{d}.{v}', 'TQ1A.{d}.{v}', 'TD1A.{d}.{v}', 'TP1A.{d}.{v}')),
    AndroidVersion(Version(major=14, minor=0, build=0), build_numbers=('AP2A.{d}.{v}', 'AD1A.{d}.{v}', 'UD2A.{d}.{v}', 'UQ1A.{d}.{v}', 'UP1A.{d}.{v}', 'UD1A.{d}.{v}')),
    AndroidVersion(Version(major=15, minor=0, build=0), build_numbers=('AP4A.{d}.{v}', 'AP3A.{d}.{v}')),
]

platform_models = ('Pixel 2', 'Pixel 2 XL', 'Pixel 3', 'Pixel 3a', 'Pixel 3a XL', 'Pixel 3 XL', 'Pixel 4',
                   'Pixel 4 XL', 'Pixel 4a (5G)', 'Pixel 5', 'Pixel 5a (5G)', 'Pixel 6', 'Pixel 6 Pro',
                   'Pixel 6a', 'Pixel 7', 'Pixel 7 Pro', 'Pixel 8', 'Pixel 8 Pro', 'Pixel 8a')


def get_version(options: Options) -> AndroidVersion:
    filterer = Filterer(versions)

    if options.version_ranges and 'android' in options.version_ranges:
        filterer.version_range(options.version_ranges['android'])

    if options.weighted_versions:
        filterer.weighted_versions(max_range=4)

    choice: AndroidVersion = random.choice(filterer.versions)
    if choice.build_number is not None:
        choice.build_number = choice.build_number.replace('{d}', '{:02d}{:02d}{:02d}'.format(random.randint(17, 25), random.randint(0, 12), random.randint(0, 29)))
        choice.build_number = choice.build_number.replace('{v}', '{}'.format(random.randint(1, 255)))
    choice.platform_model = random.choice(platform_models)
    return choice
