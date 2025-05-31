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
    AndroidVersion(Version(major=11, minor=0, build=0), build_numbers=('RD2A.{d}.{v}', 'RQ3A.{d}.{v}', 'RQ2A.{d}.{v}', 'RQ1D.{d}.{v}', 'RQ1C.{d}.{v}', 'RQ1A.{d}.{v}', 'RD1B.{d}.{v}', 'RD1A.{d}.{v}', 'RP1A.{d}.{v}')),
    AndroidVersion(Version(major=12, minor=0, build=0), build_numbers=('SP1A.{d}.{v}', 'SQ1D.{d}.{v}', 'SD1A.{d}.{v}')),
    AndroidVersion(Version(major=12, minor=1, build=0), build_numbers=('SP2A.{d}.{v}', 'SD2A.{d}.{v}', 'SQ3A.{d}.{v}')),
    AndroidVersion(Version(major=13, minor=0, build=0), build_numbers=('TQ3A.{d}.{v}', 'TQ3C.{d}.{v}', 'TQ2B.{d}.{v}', 'TD4A.{d}.{v}', 'TQ2A.{d}.{v}', 'TQ1A.{d}.{v}', 'TD1A.{d}.{v}', 'TP1A.{d}.{v}')),
    AndroidVersion(Version(major=14, minor=0, build=0), build_numbers=('AP2A.{d}.{v}', 'AD1A.{d}.{v}', 'UD2A.{d}.{v}', 'UQ1A.{d}.{v}', 'UP1A.{d}.{v}', 'UD1A.{d}.{v}')),
    AndroidVersion(Version(major=15, minor=0, build=0), build_numbers=('AP4A.{d}.{v}', 'AP3A.{d}.{v}')),
]

platform_models = ('CH1933', 'CPH2195', 'CPH2263', 'CPH1941', 'CPH2021', 'CPH2211GDPR',
    'CPH2023', 'CPH2009', 'CPH2025', 'CPH2207', 'CPH2173', 'PEEM00',
    'CPH2307', 'CPH2305', 'CPH1917', 'Global', 'Global', 'CPH2125GDPR',
    'CPH2145', 'Global', 'PEGM10', 'CPH1951', 'CPH2089', 'CPH2065',
    'CPH2251', 'CPH2371', )


def get_version(options: Options) -> AndroidVersion:
    filterer = Filterer(versions)

    if options.version_ranges and 'android' in options.version_ranges:
        filterer.version_range(options.version_ranges['android'])

    if options.weighted_versions:
        filterer.weighted_versions(max_range=3)

    choice: AndroidVersion = random.choice(filterer.versions)
    if choice.build_number is not None:
        choice.build_number = choice.build_number.replace('{d}', '{:02d}{:02d}{:02d}'.format(random.randint(22, 25), random.randint(0, 12), random.randint(0, 29)))
        choice.build_number = choice.build_number.replace('{v}', '{}'.format(random.randint(1, 255)))
    choice.platform_model = random.choice(platform_models)
    return choice
