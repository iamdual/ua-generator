"""
Random User-Agent
Copyright: 2022 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import random

# https://en.wikipedia.org/wiki/Firefox_version_history
versions = {
    '83': {'minor_range': (0, 0)},
    '84': {'minor_range': (0, 2)},
    '85': {'minor_range': (0, 2)},
    '86': {'minor_range': (0, 1)},
    '87': {'minor_range': (0, 0)},
    '88': {'minor_range': (0, 1)},
    '89': {'minor_range': (0, 2)},
    '90': {'minor_range': (0, 2)},
    '91.0': {'minor_range': (0, 13)},
    '92.0': {'minor_range': (0, 1)},
    '93.0': {'minor_range': (0, 0)},
    '94.0': {'minor_range': (0, 2)},
    '95.0': {'minor_range': (0, 2)},
    '96.0': {'minor_range': (0, 3)},
    '97.0': {'minor_range': (0, 2)},
    '98.0': {'minor_range': (0, 2)},
    '99.0': {'minor_range': (0, 1)},
    '100.0': {'minor_range': (0, 2)},
    '101.0': {'minor_range': (0, 1)},
    '102.0': {'minor_range': (0, 6)},
    '103.0': {'minor_range': (0, 2)},
    '104.0': {'minor_range': (0, 2)},
    '105.0': {'minor_range': (0, 3)},
    '106.0': {'minor_range': (0, 5)},
    '107.0': {'minor_range': (0, 1)},
    '108.0': {'minor_range': (0, 2)},
    '109.0': {'minor_range': (0, 1)},
    '110.0': {'minor_range': (0, 1)},
    '111.0': {'minor_range': (0, 1)},
    '112.0': {'minor_range': (0, 0)},
    '113.0': {'minor_range': (0, 1)},
    '114.0': {'minor_range': (0, 1)},
    '115.0': {'minor_range': (0, 1)},
    '116.0': {'minor_range': (0, 1)},
    '117.0': {'minor_range': (0, 1)},
}


def get_version():
    choice = random.randint(0, len(versions) - 1)
    i = 0
    for major, props in versions.items():
        if choice == i:
            minor = random.randint(int(props['minor_range'][0]), int(props['minor_range'][1]))
            return {'major': major, 'minor': minor}
        i = i + 1
