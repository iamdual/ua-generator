"""
Random User-Agent
Copyright: 2022 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
import random
import string

from .... import utils

# https://en.wikipedia.org/wiki/Android_version_history
# https://source.android.com/setup/start/build-numbers
versions = {
    '8.0': {
        'minor_range': (0, 5),
        'build_number': ('OPR1.{d}.{v}', 'OPR2.{d}.{v}', 'OPR3.{d}.{v}', 'OPR4.{d}.{v}', 'OPR5.{d}.{v}',
                         'OPR6.{d}.{v}', 'OPD1.{d}.{v}', 'OPD2.{d}.{v}', 'OPD3.{d}.{v}')
    },
    '8.1': {
        'minor_range': (0, 7),
        'build_number': ('OPM1.{d}.{v}', 'OPM2.{d}.{v}', 'OPM3.{d}.{v}', 'OPM4.{d}.{v}', 'OPM5.{d}.{v}')
    },
    '9.0': {
        'minor_range': (0, 0),
        'build_number': ('PPR1.{d}.{v}', 'PPR2.{d}.{v}', 'PD1A.{d}.{v}', 'PQ1A.{d}.{v}', 'PQ2A.{d}.{v}',
                         'PQ3A.{d}.{v}', 'PQ3B.{d}.{v}', 'QQ2A.{d}.{v}')
    },
    '10.0': {
        'minor_range': (0, 0),
        'build_number': ('QD1A.{d}.{v}', 'QQ1B.{d}.{v}', 'QQ1C.{d}.{v}', 'QQ1D.{d}.{v}', 'QQ2A.{d}.{v}')
    },
    '11.0': {
        'minor_range': (0, 0),
        'build_number': ('RP1A.{d}.{v}', 'RP1B.{d}.{v}', 'RP1C.{d}.{v}', 'RP1D.{d}.{v}', 'RD1A.{d}.{v}',
                         'RD1B.{d}.{v}', 'RQAA.{d}.{v}', 'RQ3A.{d}.{v}', 'RQ1D.{d}.{v}')
    },
    '12.0': {
        'minor_range': (0, 0),
        'build_number': ('SP1A.{d}.{v}', 'SD1A.{d}.{v}', 'SQ1D.{d}.{v}', 'SQ1A.{d}.{v}', 'SQ1D.{d}.{v}')
    },
}

device_names = ('Pixel 2', 'Pixel 2 XL', 'Pixel 3', 'Pixel 3a', 'Pixel 3a XL', 'Pixel 3 XL', 'Pixel 4',
                'Pixel 4 XL', 'Pixel 4a (5G)', 'Pixel 5', 'Pixel 5a (5G)', 'Pixel 6', 'Pixel 6 Pro')


def get_version():
    choice = random.randint(0, len(versions) - 1)
    i = 0
    for major, props in versions.items():
        if choice == i:
            minor = random.randint(int(props['minor_range'][0]), int(props['minor_range'][1]))
            device_name = utils.choice(device_names)

            build_number = utils.choice(props['build_number'])
            build_number = build_number.replace('{d}', '{:02d}{:02d}{:02d}'.format(
                random.randint(17, 22), random.randint(0, 12), random.randint(0, 29)))
            build_number = build_number.replace('{v}', '{}'.format(random.randint(1, 255)))

            return {'major': major, 'minor': minor, 'build_number': build_number, 'device_name': device_name}
        i = i + 1
