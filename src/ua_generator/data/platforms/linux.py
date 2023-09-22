"""
Random User-Agent
Copyright: 2022 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import random

# https://en.wikipedia.org/wiki/Linux_kernel_version_history
versions = {
    '5.0': {'minor_range': (0, 21)},
    '5.1': {'minor_range': (0, 21)},
    '5.2': {'minor_range': (0, 20)},
    '5.3': {'minor_range': (0, 18)},
    '5.4': {'minor_range': (0, 184)},
    '5.5': {'minor_range': (0, 19)},
    '5.6': {'minor_range': (0, 19)},
    '5.7': {'minor_range': (0, 19)},
    '5.8': {'minor_range': (0, 18)},
    '5.9': {'minor_range': (0, 16)},
    '5.10': {'minor_range': (0, 105)},
    '5.11': {'minor_range': (0, 22)},
    '5.12': {'minor_range': (0, 19)},
    '5.13': {'minor_range': (0, 19)},
    '5.14': {'minor_range': (0, 21)},
    '5.15': {'minor_range': (0, 103)},
    '5.16': {'minor_range': (0, 20)},
    '5.17': {'minor_range': (0, 15)},
    '5.18': {'minor_range': (0, 19)},
    '5.19': {'minor_range': (0, 17)},
    '6.0': {'minor_range': (0, 19)},
    '6.1': {'minor_range': (0, 20)},
    '6.2': {'minor_range': (0, 16)},
    '6.3': {'minor_range': (0, 13)},
    '6.4': {'minor_range': (0, 15)},
    '6.5': {'minor_range': (0, 4)},
}


def get_version():
    choice = random.randint(0, len(versions) - 1)
    i = 0
    for major, props in versions.items():
        if choice == i:
            minor = random.randint(int(props['minor_range'][0]), int(props['minor_range'][1]))
            return {'major': major, 'minor': minor}
        i = i + 1
