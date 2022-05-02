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
    '5.0': {
        'minor_range': (0, 3),
        'build_number': ('LRX21{s}', 'LRX22{s}')
    },
    '5.1': {
        'minor_range': (0, 1),
        'build_number': ('LMY47{s}', 'LMY48{s}', 'LYZ28{s}', 'LVY48{s}', 'LMY49{s}')
    },
    '6.0': {
        'minor_range': (0, 1),
        'build_number': ('MRA58{s}', 'MRA59{s}', 'MDA89{s}', 'MDB08{s}', 'MMB29{s}', 'MXC14{s}', 'MHC19{s}',
                         'MOB30{s}', 'M5C14{s}', 'MTC19{s}', 'MMB30{s}', 'MXC89{s}', 'MTC20{s}', 'MOB31{s}')
    },
    '7.0': {
        'minor_range': (0, 0),
        'build_number': ('NRD90{s}', 'NRD91{s}', 'NBD91{s}', 'N5D91{s}', 'NBD92{s}')
    },
    '7.1': {
        'minor_range': (0, 2),
        'build_number': ('NDE63{s}', 'NMF26{s}', 'NMF27{s}', 'N2G47{s}', 'NHG47{s}', 'NJH34{s}', 'NKG47{s}',
                         'NOF27{s}', 'N6F26{s}', 'N4F27{s}', 'N8I11{s}', 'NGI55{s}', 'N9F27{s}')
    },
    '8.0': {
        'minor_range': (0, 5),
        'build_number': ('OPR1.{d}.{v}', 'OPR2.{d}.{v}', 'OPR3.{d}.{v}', 'OPR4.{d}.{v}', 'OPR5.{d}.{v}',
                         'OPR6.{d}.{v}', 'OPD1.{d}.{v}', 'OPD2.{d}.{v}', 'OPD3.{d}.{v}')
    },
    '8.1': {
        'minor_range': (0, 7),
        'build_number': ('OPM1.{d}.{v}', 'OPM2.{d}.{v}', 'OPM3.{d}.{v}', 'OPM4.{d}.{v}', 'OPM5.{d}.{v}')
    }
}

device_names = ('Nexus 5', 'Nexus 5X', 'Nexus 6', 'Nexus 6P', 'Nexus 9')


def get_version():
    choice = random.randint(0, len(versions) - 1)
    i = 0
    for major, props in versions.items():
        if choice == i:
            minor = random.randint(int(props['minor_range'][0]), int(props['minor_range'][1]))
            device_name = utils.choice(device_names)

            build_number = utils.choice(props['build_number'])
            build_number = build_number.replace('{s}', '{}'.format(random.choice(string.ascii_uppercase)))
            build_number = build_number.replace('{d}', '{:02d}{:02d}{:02d}'.format(
                random.randint(17, 22), random.randint(0, 12), random.randint(0, 29)))
            build_number = build_number.replace('{v}', '{}'.format(random.randint(1, 255)))

            return {'major': major, 'minor': minor, 'build_number': build_number, 'device_name': device_name}
        i = i + 1
