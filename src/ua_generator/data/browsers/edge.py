"""
Random User-Agent
Copyright: 2022 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import random

# https://docs.microsoft.com/en-us/deployedge/microsoft-edge-release-schedule
versions = {
    '88.0.705': {'minor_range': (0, 99), 'webkit': '537.36'},
    '89.0.774': {'minor_range': (0, 99), 'webkit': '537.36'},
    '90.0.818': {'minor_range': (0, 99), 'webkit': '537.36'},
    '91.0.864': {'minor_range': (0, 99), 'webkit': '537.36'},
    '92.0.902': {'minor_range': (0, 99), 'webkit': '537.36'},
    '93.0.961': {'minor_range': (0, 99), 'webkit': '537.36'},
    '94.0.992': {'minor_range': (0, 99), 'webkit': '537.36'},
    '95.0.1020': {'minor_range': (0, 99), 'webkit': '537.36'},
    '96.0.1054': {'minor_range': (0, 99), 'webkit': '537.36'},
    '97.0.1072': {'minor_range': (0, 99), 'webkit': '537.36'},
    '98.0.1108': {'minor_range': (0, 99), 'webkit': '537.36'},
    '99.0.1141': {'minor_range': (0, 99), 'webkit': '537.36'},
    '99.0.1146': {'minor_range': (0, 99), 'webkit': '537.36'},
    '100.0.1185': {'minor_range': (0, 99), 'webkit': '537.36'},
    '101.0.1210': {'minor_range': (0, 99), 'webkit': '537.36'},
    '102.0.1245': {'minor_range': (0, 99), 'webkit': '537.36'},
    '103.0.1264': {'minor_range': (0, 99), 'webkit': '537.36'},
    '104.0.1293': {'minor_range': (0, 99), 'webkit': '537.36'},
    '105.0.1343': {'minor_range': (0, 99), 'webkit': '537.36'},
    '106.0.1370': {'minor_range': (0, 99), 'webkit': '537.36'},
    '107.0.1418': {'minor_range': (0, 99), 'webkit': '537.36'},
    '108.0.1462': {'minor_range': (0, 99), 'webkit': '537.36'},
    '109.0.1518': {'minor_range': (0, 99), 'webkit': '537.36'},
    '110.0.1587': {'minor_range': (0, 99), 'webkit': '537.36'},
    '111.0.1661': {'minor_range': (0, 99), 'webkit': '537.36'},
}


def get_version():
    choice = random.randint(0, len(versions) - 1)
    i = 0
    for major, props in versions.items():
        if choice == i:
            minor = random.randint(int(props['minor_range'][0]), int(props['minor_range'][1]))
            return {'major': major, 'minor': minor, 'webkit': props['webkit']}
        i = i + 1
