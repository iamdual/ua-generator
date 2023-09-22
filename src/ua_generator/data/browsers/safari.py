"""
Random User-Agent
Copyright: 2022 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import random

# https://en.wikipedia.org/wiki/Safari_version_history
versions = {
    '8': {'minor_range': (0, 0), 'webkit': '600.5.17'},
    '9': {'minor_range': (0, 0), 'webkit': '601.1.46'},
    '10': {'minor_range': (0, 0), 'webkit': '602.4.8'},
    '11': {'minor_range': (0, 0), 'webkit': '604.1.38'},
    '12': {'minor_range': (0, 1), 'webkit': '605.1.15'},
    '13': {'minor_range': (0, 1), 'webkit': '605.1.15'},
    '14': {'minor_range': (0, 1), 'webkit': '605.1.15'},
    '15': {'minor_range': (0, 5), 'webkit': '605.1.15'},
    '16': {'minor_range': (0, 5), 'webkit': '605.1.15'},
}


def get_version():
    choice = random.randint(0, len(versions) - 1)
    i = 0
    for major, props in versions.items():
        if choice == i:
            minor = random.randint(int(props['minor_range'][0]), int(props['minor_range'][1]))
            return {'major': major, 'minor': minor, 'webkit': props['webkit']}
        i = i + 1
