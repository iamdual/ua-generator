"""
Random User-Agent
Copyright: 2022 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import random

# https://en.wikipedia.org/wiki/IOS_version_history
versions = {
    '14.0': {'minor_range': (0, 1)},
    '14.1': {'minor_range': (0, 0)},
    '14.2': {'minor_range': (0, 1)},
    '14.3': {'minor_range': (0, 0)},
    '14.4': {'minor_range': (0, 2)},
    '14.5': {'minor_range': (0, 1)},
    '14.6': {'minor_range': (0, 0)},
    '14.7': {'minor_range': (0, 1)},
    '14.8': {'minor_range': (0, 1)},
    '15.0': {'minor_range': (0, 2)},
    '15.1': {'minor_range': (0, 1)},
    '15.2': {'minor_range': (0, 1)},
    '15.3': {'minor_range': (0, 1)},
    '15.4': {'minor_range': (0, 1)},
    '15.5': {'minor_range': (0, 0)},
    '15.6': {'minor_range': (0, 1)},
    '15.7': {'minor_range': (0, 4)},
    '16.4': {'minor_range': (0, 1)},
    '16.5': {'minor_range': (0, 1)},
    '16.6': {'minor_range': (0, 1)},
    '17.0': {'minor_range': (0, 2)},
}


def get_version():
    choice = random.randint(0, len(versions) - 1)
    i = 0
    for major, props in versions.items():
        if choice == i:
            minor = random.randint(int(props['minor_range'][0]), int(props['minor_range'][1]))
            return {'major': major, 'minor': minor}
        i = i + 1
