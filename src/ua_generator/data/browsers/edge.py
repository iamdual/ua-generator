"""
Random User-Agent
Copyright: 2022 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import random

# https://en.wikipedia.org/wiki/Microsoft_Edge#New_Edge_release_history
versions = {
    '84.0.522': {'minor_range': (0, 255), 'webkit': '537.36'},
    '85.0.564': {'minor_range': (0, 255), 'webkit': '537.36'},
    '86.0.622': {'minor_range': (0, 255), 'webkit': '537.36'},
    '87.0.664': {'minor_range': (0, 255), 'webkit': '537.36'},
    '88.0.705': {'minor_range': (0, 255), 'webkit': '537.36'},
    '89.0.774': {'minor_range': (0, 255), 'webkit': '537.36'},
    '90.0.818': {'minor_range': (0, 255), 'webkit': '537.36'},
    '91.0.864': {'minor_range': (0, 255), 'webkit': '537.36'},
    '92.0.902': {'minor_range': (0, 255), 'webkit': '537.36'},
    '93.0.961': {'minor_range': (0, 255), 'webkit': '537.36'},
    '94.0.992': {'minor_range': (0, 255), 'webkit': '537.36'},
    '95.0.1020': {'minor_range': (0, 255), 'webkit': '537.36'},
    '96.0.1054': {'minor_range': (0, 255), 'webkit': '537.36'},
    '97.0.1072': {'minor_range': (0, 255), 'webkit': '537.36'},
    '98.0.1108': {'minor_range': (0, 255), 'webkit': '537.36'},
    '99.0.1141': {'minor_range': (0, 255), 'webkit': '537.36'},
    '99.0.1146': {'minor_range': (0, 255), 'webkit': '537.36'},
}


def get_version():
    choice = random.randint(0, len(versions) - 1)
    i = 0
    for major, props in versions.items():
        if choice == i:
            minor = random.randint(int(props['minor_range'][0]), int(props['minor_range'][1]))
            return {'major': major, 'minor': minor, 'webkit': props['webkit']}
        i = i + 1
