"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import random

# https://www.mozilla.org/en-US/firefox/releases/
versions = {
    '103.0': {'minor_range': (0, 2)},
    '104.0': {'minor_range': (0, 2)},
    '105.0': {'minor_range': (0, 3)},
    '106.0': {'minor_range': (0, 5)},
    '107.0': {'minor_range': (0, 1)},
    '108.0': {'minor_range': (0, 2)},
    '109.0': {'minor_range': (0, 1)},
    '110.0': {'minor_range': (0, 1)},
    '111.0': {'minor_range': (0, 1)},
    '112.0': {'minor_range': (0, 2)},
    '113.0': {'minor_range': (0, 2)},
    '114.0': {'minor_range': (0, 2)},
    '115.0': {'minor_range': (0, 3)},
    '115.1': {'minor_range': (0, 0)},
    '115.2': {'minor_range': (0, 1)},
    '115.3': {'minor_range': (0, 1)},
    '115.4': {'minor_range': (0, 0)},
    '115.5': {'minor_range': (0, 0)},
    '115.6': {'minor_range': (0, 0)},
    '115.7': {'minor_range': (0, 0)},
    '115.8': {'minor_range': (0, 0)},
    '116.0': {'minor_range': (0, 3)},
    '117.0': {'minor_range': (0, 1)},
    '118.0': {'minor_range': (0, 2)},
    '119.0': {'minor_range': (0, 1)},
    '120.0': {'minor_range': (0, 1)},
    '121.0': {'minor_range': (0, 1)},
    '122.0': {'minor_range': (0, 1)},
    '123.0': {'minor_range': (0, 1)},
    '124.0': {'minor_range': (0, 2)},
    '125.0': {'minor_range': (1, 3)},
    '126.0': {'minor_range': (0, 0)},
}


def get_version():
    choice = random.randint(0, len(versions) - 1)
    i = 0
    for major, props in versions.items():
        if choice == i:
            minor = random.randint(int(props['minor_range'][0]), int(props['minor_range'][1]))
            return {'major': major, 'minor': minor}
        i = i + 1
