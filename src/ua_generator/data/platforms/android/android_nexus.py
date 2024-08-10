"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
import random
import string
from typing import List

from ...version import Version, AndroidVersion
from ....options import Options

# https://en.wikipedia.org/wiki/Android_version_history
# https://source.android.com/setup/start/build-numbers
versions: List[AndroidVersion] = [
    AndroidVersion(Version(major=5, minor=0, build=(0, 3)),
                   build_numbers=('LRX21{s}', 'LRX22{s}')),
    AndroidVersion(Version(major=5, minor=1, build=(0, 1)),
                   build_numbers=('LMY47{s}', 'LMY48{s}', 'LYZ28{s}', 'LVY48{s}', 'LMY49{s}')),
    AndroidVersion(Version(major=6, minor=0, build=(0, 1)),
                   build_numbers=('MRA58{s}', 'MRA59{s}', 'MDA89{s}', 'MDB08{s}', 'MMB29{s}', 'MXC14{s}', 'MHC19{s}',
                                  'MOB30{s}', 'M5C14{s}', 'MTC19{s}', 'MMB30{s}', 'MXC89{s}', 'MTC20{s}', 'MOB31{s}')),
    AndroidVersion(Version(major=7, minor=0, build=0),
                   build_numbers=('NRD90{s}', 'NRD91{s}', 'NBD91{s}', 'N5D91{s}', 'NBD92{s}')),
    AndroidVersion(Version(major=7, minor=1, build=(0, 2)),
                   build_numbers=('NDE63{s}', 'NMF26{s}', 'NMF27{s}', 'N2G47{s}', 'NHG47{s}', 'NJH34{s}', 'NKG47{s}',
                                  'NOF27{s}', 'N6F26{s}', 'N4F27{s}', 'N8I11{s}', 'NGI55{s}', 'N9F27{s}')),
    AndroidVersion(Version(major=8, minor=0, build=(0, 5)),
                   build_numbers=('OPR1.{d}.{v}', 'OPR2.{d}.{v}', 'OPR3.{d}.{v}', 'OPR4.{d}.{v}', 'OPR5.{d}.{v}',
                                  'OPR6.{d}.{v}', 'OPD1.{d}.{v}', 'OPD2.{d}.{v}', 'OPD3.{d}.{v}')),
    AndroidVersion(Version(major=8, minor=1, build=(0, 7)),
                   build_numbers=('OPM1.{d}.{v}', 'OPM2.{d}.{v}', 'OPM3.{d}.{v}', 'OPM4.{d}.{v}', 'OPM5.{d}.{v}')),
]

platform_models = ('Nexus 5', 'Nexus 5X', 'Nexus 6', 'Nexus 6P', 'Nexus 9')


def get_version(options: Options) -> AndroidVersion:
    weights = None
    if options.weighted_versions:
        weights = [1.0] * len(versions)
        weights[-1] = 10.0
        weights[-2] = 9.0
        weights[-3] = 8.0
        weights[-4] = 8.0

    choice: List[AndroidVersion] = random.choices(versions, weights=weights, k=1)

    build_number = choice[0].build_number
    build_number = build_number.replace('{s}', '{}'.format(random.choice(string.ascii_uppercase)))
    build_number = build_number.replace('{d}', '{:02d}{:02d}{:02d}'.format(random.randint(17, 22), random.randint(0, 12), random.randint(0, 29)))
    build_number = build_number.replace('{v}', '{}'.format(random.randint(1, 255)))

    choice[0].build_number = build_number
    choice[0].platform_model = random.choice(platform_models)
    return choice[0]
