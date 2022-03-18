"""
Random User-Agent
Copyright: 2022 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import random

# https://en.wikipedia.org/wiki/IOS_version_history
versions = {
    '9': {'minor_range': (0, 3)},
    '10': {'minor_range': (0, 3)},
    '11': {'minor_range': (0, 4)},
    '12': {'minor_range': (0, 5)},
    '13': {'minor_range': (0, 7)},
    '14': {'minor_range': (0, 8)},
    '15': {'minor_range': (0, 4)},
}


def get_version():
    choice = random.randint(0, len(versions) - 1)
    i = 0
    for major, props in versions.items():
        if choice == i:
            minor = random.randint(int(props['minor_range'][0]), int(props['minor_range'][1]))
            return {'major': major, 'minor': minor}
        i = i + 1
