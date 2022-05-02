"""
Random User-Agent
Copyright: 2022 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import random

# https://en.wikipedia.org/wiki/MacOS_version_history
versions = {
    '10.8': {'minor_range': (0, 8)},
    '10.9': {'minor_range': (0, 5)},
    '10.10': {'minor_range': (0, 5)},
    '10.11': {'minor_range': (0, 6)},
    '10.12': {'minor_range': (0, 6)},
    '10.13': {'minor_range': (0, 6)},
    '10.14': {'minor_range': (0, 6)},
    '10.15': {'minor_range': (0, 7)},
    '11.0': {'minor_range': (0, 0)},
    '11.2': {'minor_range': (0, 3)},
    '11.3': {'minor_range': (0, 1)},
    '11.5': {'minor_range': (0, 2)},
    '11.6': {'minor_range': (0, 5)},
    '12.0': {'minor_range': (0, 1)},
    '12.2': {'minor_range': (0, 1)},
    '12.3': {'minor_range': (0, 1)},
}


def get_version():
    choice = random.randint(0, len(versions) - 1)
    i = 0
    for major, props in versions.items():
        if choice == i:
            minor = random.randint(int(props['minor_range'][0]), int(props['minor_range'][1]))
            return {'major': major, 'minor': minor}
        i = i + 1
