"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
import random
from typing import List

from ...version import Version, AndroidVersion
from ....options import Options

# https://en.wikipedia.org/wiki/Android_version_history
# https://source.android.com/setup/start/build-numbers
versions: List[AndroidVersion] = [
    AndroidVersion(Version(major=8, minor=0, build=(0, 5)),
                   build_numbers=('OPR1.{d}.{v}', 'OPR2.{d}.{v}', 'OPR3.{d}.{v}', 'OPR4.{d}.{v}', 'OPR5.{d}.{v}',
                                  'OPR6.{d}.{v}', 'OPD1.{d}.{v}', 'OPD2.{d}.{v}', 'OPD3.{d}.{v}')),
    AndroidVersion(Version(major=8, minor=1, build=(0, 7)),
                   build_numbers=('OPM1.{d}.{v}', 'OPM2.{d}.{v}', 'OPM3.{d}.{v}', 'OPM4.{d}.{v}', 'OPM5.{d}.{v}')),
    AndroidVersion(Version(major=9, minor=0, build=0),
                   build_numbers=('PPR1.{d}.{v}', 'PPR2.{d}.{v}', 'PD1A.{d}.{v}', 'PQ1A.{d}.{v}', 'PQ2A.{d}.{v}',
                                  'PQ3A.{d}.{v}', 'PQ3B.{d}.{v}', 'QQ2A.{d}.{v}')),
    AndroidVersion(Version(major=10, minor=0, build=0),
                   build_numbers=('QD1A.{d}.{v}', 'QQ1B.{d}.{v}', 'QQ1C.{d}.{v}', 'QQ1D.{d}.{v}', 'QQ2A.{d}.{v}')),
    AndroidVersion(Version(major=11, minor=0, build=0),
                   build_numbers=('RP1A.{d}.{v}', 'RP1B.{d}.{v}', 'RP1C.{d}.{v}', 'RP1D.{d}.{v}', 'RD1A.{d}.{v}',
                                  'RD1B.{d}.{v}', 'RQAA.{d}.{v}', 'RQ3A.{d}.{v}', 'RQ1D.{d}.{v}')),
    AndroidVersion(Version(major=12, minor=0, build=0),
                   build_numbers=('SP1A.{d}.{v}', 'SD1A.{d}.{v}', 'SQ1D.{d}.{v}', 'SQ1A.{d}.{v}', 'SQ1D.{d}.{v}')),
    AndroidVersion(Version(major=12, minor=1, build=0),
                   build_numbers=('SP2A.{d}.{v}', 'SD2A.{d}.{v}', 'SQ3A.{d}.{v}')),
    AndroidVersion(Version(major=13, minor=0, build=0),
                   build_numbers=('TQ3A.{d}.{v}', 'TQ2A.{d}.{v}', 'TP1A.{d}.{v}', 'TQ1A.{d}.{v}', 'TD1A.{d}.{v}')),
    AndroidVersion(Version(major=14, minor=0, build=0),
                   build_numbers=('UP1A.{d}.{v}', 'UD1A.{d}.{v}', 'UQ1A.{d}.{v}')),
]

platform_models = ('Pixel 2', 'Pixel 2 XL', 'Pixel 3', 'Pixel 3a', 'Pixel 3a XL', 'Pixel 3 XL', 'Pixel 4',
                   'Pixel 4 XL', 'Pixel 4a (5G)', 'Pixel 5', 'Pixel 5a (5G)', 'Pixel 6', 'Pixel 6 Pro',
                   'Pixel 6a', 'Pixel 7', 'Pixel 7 Pro', 'Pixel 8', 'Pixel 8 Pro')


def get_version(options: Options) -> AndroidVersion:
    weights = None
    if options.weighted_versions:
        weights = [1.0] * len(versions)
        weights[-1] = 10.0
        weights[-2] = 9.0
        weights[-3] = 8.0

    choice: List[AndroidVersion] = random.choices(versions, weights=weights, k=1)

    build_number = choice[0].build_number
    build_number = build_number.replace('{d}', '{:02d}{:02d}{:02d}'.format(random.randint(17, 22), random.randint(0, 12), random.randint(0, 29)))
    build_number = build_number.replace('{v}', '{}'.format(random.randint(1, 255)))

    choice[0].build_number = build_number
    choice[0].platform_model = random.choice(platform_models)
    return choice[0]
