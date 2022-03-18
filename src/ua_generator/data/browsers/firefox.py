"""
Random User-Agent
Copyright: 2022 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import random

# https://en.wikipedia.org/wiki/Firefox_version_history
versions = {
    '60': {'minor_range': (0, 9)},
    '61': {'minor_range': (0, 0)},
    '62': {'minor_range': (0, 0)},
    '63': {'minor_range': (0, 0)},
    '64': {'minor_range': (0, 0)},
    '65': {'minor_range': (0, 0)},
    '66': {'minor_range': (0, 0)},
    '67': {'minor_range': (0, 0)},
    '68': {'minor_range': (0, 9)},
    '70': {'minor_range': (0, 0)},
    '71': {'minor_range': (0, 0)},
    '72': {'minor_range': (0, 0)},
    '73': {'minor_range': (0, 0)},
    '74': {'minor_range': (0, 0)},
    '75': {'minor_range': (0, 0)},
    '76': {'minor_range': (0, 0)},
    '77': {'minor_range': (0, 0)},
    '78': {'minor_range': (0, 0)},
    '79': {'minor_range': (0, 0)},
    '80': {'minor_range': (0, 0)},
    '81': {'minor_range': (0, 0)},
    '82': {'minor_range': (0, 0)},
    '83': {'minor_range': (0, 0)},
    '84': {'minor_range': (0, 0)},
    '85': {'minor_range': (0, 0)},
    '86': {'minor_range': (0, 0)},
    '87': {'minor_range': (0, 0)},
    '88': {'minor_range': (0, 0)},
    '89': {'minor_range': (0, 0)},
    '90': {'minor_range': (0, 0)},
    '91': {'minor_range': (0, 7)},
    '92': {'minor_range': (0, 0)},
    '93': {'minor_range': (0, 0)},
    '94': {'minor_range': (0, 0)},
    '95': {'minor_range': (0, 0)},
    '96': {'minor_range': (0, 0)},
    '97': {'minor_range': (0, 0)},
    '98': {'minor_range': (0, 0)},
    '99': {'minor_range': (0, 0)},
}


def get_version():
    choice = random.randint(0, len(versions) - 1)
    i = 0
    for major, props in versions.items():
        if choice == i:
            minor = random.randint(int(props['minor_range'][0]), int(props['minor_range'][1]))
            return {'major': major, 'minor': minor}
        i = i + 1
