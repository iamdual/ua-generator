"""
Random User-Agent
Copyright: 2022 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import random

# https://en.wikipedia.org/wiki/Safari_version_history
versions = {
    '8': {'minor_range': (0, 0), 'webkit': '600.1.4'},
    '9': {'minor_range': (0, 0), 'webkit': '600.1.4'},
    '10': {'minor_range': (0, 0), 'webkit': '600.1.4'},
    '11': {'minor_range': (0, 0), 'webkit': '604.1.38'},
    '12': {'minor_range': (0, 2), 'webkit': '604.1.38'},
    '13': {'minor_range': (0, 1), 'webkit': '604.1.38'},
    '14': {'minor_range': (0, 1), 'webkit': '604.1.38'},
    '15': {'minor_range': (0, 3), 'webkit': '604.1.38'},
}


def get_version():
    choice = random.randint(0, len(versions) - 1)
    i = 0
    for major, props in versions.items():
        if choice == i:
            minor = random.randint(int(props['minor_range'][0]), int(props['minor_range'][1]))
            return {'major': major, 'minor': minor, 'webkit': props['webkit']}
        i = i + 1
