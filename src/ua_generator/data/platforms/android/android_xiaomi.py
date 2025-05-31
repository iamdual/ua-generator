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


# https://whatmyuseragent.com/brand/xi/xiaomi
# https://gist.github.com/iamdual/2ef10eeae2c3ce22470bb9acfa77435e
platform_models = (
    '11i HyperCharge 5G', '12', '12 Lite', '12 Pro', '12 Pro Dimensity', '12S', '12S Pro', '12S Ultra', '12T', '12T Pro',
    '12X', '13 Lite', '13 Pro', '13 Ultra', '13T', '13T Pro', '14', '14 Civi', '14 Pro', '14 Pro Ti', '14 Ultra', '14T Pro',
    '15', '15 Pro', 'Black Shark', 'Black Shark 2', 'Black Shark 2 Pro', 'Black Shark 3', 'Black Shark 3 5G',
    'Black Shark 3 Pro', 'Black Shark 3 Pro 5G', 'Black Shark 4', 'Black Shark 4 Pro', 'Black Shark 5', 'Black Shark 5 Pro',
    'Black Shark Helo', 'CC11', 'Civi', 'Civi 1S', 'Civi 2', 'Civi 3', 'Civi 4', 'Mi 10', 'Mi 10 Lite 5G', 'Mi 10 Pro',
    'Mi 10 Ultra 5G', 'Mi 10i', 'Mi 10S', 'Mi 10T 5G', 'Mi 10T Lite 5G', 'Mi 10T Pro 5G', 'Mi 11', 'Mi 11 Lite',
    'Mi 11 Lite 5G', 'Mi 11 Lite 5G NE', 'Mi 11 Pro', 'Mi 11 Ultra', 'Mi 11i', 'Mi 11T', 'Mi 11T Pro', 'Mi 11X',
    'Mi 11X Pro', 'Mi 4 LTE', 'Mi 4i', 'Mi 4W', 'Mi 5s Plus', 'Mi 5X', 'Mi 8', 'Mi 8 Explorer Edition', 'Mi 8 Lite', 'Mi 9',
    'Mi 9 Lite', 'Mi 9 Pro 5G', 'Mi 9 SE', 'Mi 9 Transparent Edition', 'Mi 9T Pro', 'Mi A2 Lite', 'Mi A3', 'Mi CC 9',
    'Mi CC 9 Pro', 'Mi CC 9 Pro Premium Edition', 'Mi CC 9e', 'Mi Laser Projector 150"', 'Mi Max', 'Mi Max 3 Pro', 'Mi Mix',
    'Mi Mix 2', 'Mi Mix 2S', 'Mi Mix 2S Art', 'Mi Mix 3 5G', 'Mi Mix 4', 'Mi Mix Fold', 'Mi Note 10', 'Mi Note 10 Lite',
    'Mi Note 10 Pro', 'Mi Note 3', 'Mi Note Pro', 'Mi One Plus', 'Mi Pad', 'Mi Pad 2', 'Mi Pad 3', 'Mi Pad 4',
    'Mi Pad 4 Plus', 'Mi Pad 4 WiFi', 'Mi Pad 5', 'Mi Pad 5 Pro', 'Mi Pad 5 Pro 5G', 'Mi Play',
    'Mi Smart Compact Projector', 'Mix Flip', 'Mix Fold 2', 'Mix Fold 3', 'Mix Fold 4', 'Note 12 Pro', 'Pad 6 Max 14',
    'Pad 6 Pro', 'Pad 6S Pro 12.4"', 'Pocophone F1', 'Qin 1s+', 'Qin 2', 'Qin 2 Pro', 'Qin 3 Ultra', 'Redmi 1', 'Redmi 10',
    'Redmi 10 (2022)', 'Redmi 10 5G', 'Redmi 10 Power', 'Redmi 10 Prime', 'Redmi 10 Prime (2022)', 'Redmi 10 Prime+ 5G',
    'Redmi 10A', 'Redmi 10C', 'Redmi 10X', 'Redmi 10X Pro', 'Redmi 11 Prime', 'Redmi 12', 'Redmi 12 5G', 'Redmi 12C',
    'Redmi 13', 'Redmi 13 5G', 'Redmi 13C', 'Redmi 13C 5G', 'Redmi 14C', 'Redmi 1S', 'Redmi 2', 'Redmi 2 Pro', 'Redmi 2A',
    'Redmi 3', 'Redmi 4 Prime', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 6 Pro Extreme', 'Redmi 7A', 'Redmi 8', 'Redmi 8A',
    'Redmi 9', 'Redmi 9 Power', 'Redmi 9 Prime', 'Redmi 9A', 'Redmi 9AT', 'Redmi 9C', 'Redmi 9C NFC', 'Redmi 9i',
    'Redmi 9i Sport', 'Redmi 9T', 'Redmi 9T NFC', 'Redmi A1', 'Redmi A1+', 'Redmi A2', 'Redmi A2+', 'Redmi A3', 'Redmi A3x',
    'Redmi Go', 'Redmi K20', 'Redmi K20 Pro', 'Redmi K20 Pro Premium Edition', 'Redmi K30 4G', 'Redmi K30 5G',
    'Redmi K30 Pro Zoom', 'Redmi K30 Pro Zoom Edition', 'Redmi K30 Ultra', 'Redmi K30i 5G', 'Redmi K30S Ultra', 'Redmi K40',
    'Redmi K40 Gaming', 'Redmi K40 Pro', 'Redmi K40 Pro+', 'Redmi K40S', 'Redmi K50', 'Redmi K50 Pro', 'Redmi K50 Ultra',
    'Redmi K50G', 'Redmi K50i', 'Redmi K60', 'Redmi K60 Pro', 'Redmi K60 Ultra', 'Redmi K60E', 'Redmi K70', 'Redmi K70 Pro',
    'Redmi K70 Ultra', 'Redmi K70E', 'Redmi K80 Pro', 'Redmi Note', 'Redmi Note 10', 'Redmi Note 10 5G', 'Redmi Note 10 JE',
    'Redmi Note 10 Lite', 'Redmi Note 10 Pro', 'Redmi Note 10S', 'Redmi Note 10T', 'Redmi Note 10T 5G', 'Redmi Note 10X',
    'Redmi Note 11 4G', 'Redmi Note 11 5G', 'Redmi Note 11 Pro', 'Redmi Note 11 Pro 5G', 'Redmi Note 11 Pro+',
    'Redmi Note 11 Pro+ 5G', 'Redmi Note 11 SE', 'Redmi Note 11E', 'Redmi Note 11E Pro', 'Redmi Note 11R 5G',
    'Redmi Note 11S', 'Redmi Note 11S 5G', 'Redmi Note 11T 5G', 'Redmi Note 11T Pro', 'Redmi Note 11T Pro+',
    'Redmi Note 12', 'Redmi Note 12 Discovery', 'Redmi Note 12 Pro', 'Redmi Note 12 Pro DE', 'Redmi Note 12 Pro Speed',
    'Redmi Note 12 Pro+', 'Redmi Note 12 Pro+ 5G', 'Redmi Note 12R', 'Redmi Note 12R Pro', 'Redmi Note 12S',
    'Redmi Note 12T', 'Redmi Note 12T Pro', 'Redmi Note 13', 'Redmi Note 13 5G', 'Redmi Note 13 Pro',
    'Redmi Note 13 Pro 5G', 'Redmi Note 13 Pro+', 'Redmi Note 13 Pro+ 5G', 'Redmi Note 13R', 'Redmi Note 13R Pro',
    'Redmi Note 14', 'Redmi Note 14 5G', 'Redmi Note 14 Pro', 'Redmi Note 14 Pro 5G', 'Redmi Note 14 Pro+', 'Redmi Note 3',
    'Redmi Note 5A Lite', 'Redmi Note 5A Prime', 'Redmi Note 7', 'Redmi Note 7 Pro', 'Redmi Note 7S', 'Redmi Note 8',
    'Redmi Note 8 (2021)', 'Redmi Note 8 Pro', 'Redmi Note 8T', 'Redmi Note 9', 'Redmi Note 9 5G', 'Redmi Note 9 Pro',
    'Redmi Note 9 Pro 5G', 'Redmi Note 9 Pro Max', 'Redmi Note 9S', 'Redmi Note 9T 5G', 'Redmi Pad', 'Redmi Pad Pro',
    'Redmi Pad Pro 5G', 'Redmi Pad SE', 'Redmi Pad SE 8.7"', 'Redmi Turbo 3', 'Redmi Y1 Lite'
)


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
