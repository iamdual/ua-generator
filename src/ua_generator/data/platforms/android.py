"""
Random User-Agent
Copyright: 2022 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import random

# https://en.wikipedia.org/wiki/Android_version_history
versions = {
    '5.0': {'minor_range': (0, 3)},
    '5.1': {'minor_range': (0, 1)},
    '6.0': {'minor_range': (0, 1)},
    '7.0': {'minor_range': (0, 0)},
    '7.1': {'minor_range': (0, 2)},
    '8.0': {'minor_range': (0, 5)},
    '8.1': {'minor_range': (0, 7)},
    '9.0': {'minor_range': (0, 0)},
    '10.0': {'minor_range': (0, 0)},
    '11.0': {'minor_range': (0, 0)},
    '12.0': {'minor_range': (0, 0)},
}


def get_version():
    choice = random.randint(0, len(versions) - 1)
    i = 0
    for major, props in versions.items():
        if choice == i:
            minor = random.randint(int(props['minor_range'][0]), int(props['minor_range'][1]))
            return {'major': major, 'minor': minor}
        i = i + 1
