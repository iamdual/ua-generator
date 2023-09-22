"""
Random User-Agent
Copyright: 2022 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import random

# https://en.wikipedia.org/wiki/Google_Chrome_version_history
versions = {
    '90.0.4430': {'minor_range': (0, 255), 'webkit': '537.36'},
    '91.0.4472': {'minor_range': (0, 255), 'webkit': '537.36'},
    '92.0.4515': {'minor_range': (0, 255), 'webkit': '537.36'},
    '93.0.4577': {'minor_range': (0, 255), 'webkit': '537.36'},
    '94.0.4606': {'minor_range': (0, 255), 'webkit': '537.36'},
    '95.0.4638': {'minor_range': (0, 255), 'webkit': '537.36'},
    '96.0.4664': {'minor_range': (0, 255), 'webkit': '537.36'},
    '97.0.4692': {'minor_range': (0, 255), 'webkit': '537.36'},
    '98.0.4758': {'minor_range': (0, 255), 'webkit': '537.36'},
    '99.0.4844': {'minor_range': (0, 255), 'webkit': '537.36'},
    '100.0.4896': {'minor_range': (0, 255), 'webkit': '537.36'},
    '101.0.4951': {'minor_range': (0, 255), 'webkit': '537.36'},
    '102.0.5005': {'minor_range': (0, 255), 'webkit': '537.36'},
    '103.0.5060': {'minor_range': (0, 255), 'webkit': '537.36'},
    '104.0.5112': {'minor_range': (0, 255), 'webkit': '537.36'},
    '105.0.5195': {'minor_range': (0, 255), 'webkit': '537.36'},
    '106.0.5249': {'minor_range': (0, 255), 'webkit': '537.36'},
    '107.0.5304': {'minor_range': (0, 255), 'webkit': '537.36'},
    '108.0.5359': {'minor_range': (0, 255), 'webkit': '537.36'},
    '109.0.5414': {'minor_range': (0, 255), 'webkit': '537.36'},
    '110.0.5481': {'minor_range': (0, 255), 'webkit': '537.36'},
    '111.0.5563': {'minor_range': (0, 255), 'webkit': '537.36'},
    '112.0.5615': {'minor_range': (0, 255), 'webkit': '537.36'},
    '114.0.5735': {'minor_range': (0, 255), 'webkit': '537.36'},
    '115.0.5790': {'minor_range': (0, 255), 'webkit': '537.36'},
    '116.0.5845': {'minor_range': (0, 255), 'webkit': '537.36'},
    '117.0.5938': {'minor_range': (0, 255), 'webkit': '537.36'},
}


def get_version():
    choice = random.randint(0, len(versions) - 1)
    i = 0
    for major, props in versions.items():
        if choice == i:
            minor = random.randint(int(props['minor_range'][0]), int(props['minor_range'][1]))
            return {'major': major, 'minor': minor, 'webkit': props['webkit']}
        i = i + 1
