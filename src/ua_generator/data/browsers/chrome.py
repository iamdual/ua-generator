"""
Random User-Agent
Copyright: 2022 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import random

# https://en.wikipedia.org/wiki/Google_Chrome_version_history
versions = {
    '76.0.3809': {'minor_range': (0, 255), 'webkit': '537.36'},
    '77.0.3865': {'minor_range': (0, 255), 'webkit': '537.36'},
    '78.0.3904': {'minor_range': (0, 255), 'webkit': '537.36'},
    '79.0.3945': {'minor_range': (0, 255), 'webkit': '537.36'},
    '80.0.3987': {'minor_range': (0, 255), 'webkit': '537.36'},
    '81.0.4044': {'minor_range': (0, 255), 'webkit': '537.36'},
    '83.0.4103': {'minor_range': (0, 255), 'webkit': '537.36'},
    '84.0.4147': {'minor_range': (0, 255), 'webkit': '537.36'},
    '85.0.4183': {'minor_range': (0, 255), 'webkit': '537.36'},
    '86.0.4240': {'minor_range': (0, 255), 'webkit': '537.36'},
    '87.0.4280': {'minor_range': (0, 255), 'webkit': '537.36'},
    '88.0.4324': {'minor_range': (0, 255), 'webkit': '537.36'},
    '89.0.4389': {'minor_range': (0, 255), 'webkit': '537.36'},
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
}


def get_version():
    choice = random.randint(0, len(versions) - 1)
    i = 0
    for major, props in versions.items():
        if choice == i:
            minor = random.randint(int(props['minor_range'][0]), int(props['minor_range'][1]))
            return {'major': major, 'minor': minor, 'webkit': props['webkit']}
        i = i + 1
