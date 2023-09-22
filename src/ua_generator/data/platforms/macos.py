"""
Random User-Agent
Copyright: 2022 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import random

# User agent cap on macOS
# https://groups.google.com/a/chromium.org/g/blink-dev/c/hAI4QoX6rEo/m/qQNPThr0AAAJ

# https://en.wikipedia.org/wiki/MacOS_version_history
versions = {
    '10.11': {'minor_range': (0, 6)},
    '10.12': {'minor_range': (0, 6)},
    '10.13': {'minor_range': (0, 6)},
    '10.14': {'minor_range': (0, 6)},
    '10.15': {'minor_range': (0, 7)},
    '11.0': {'minor_range': (0, 0)},
    '11.2': {'minor_range': (0, 3)},
    '11.3': {'minor_range': (0, 1)},
    '11.5': {'minor_range': (0, 2)},
    '11.6': {'minor_range': (0, 6)},
    '12.0': {'minor_range': (0, 1)},
    '12.2': {'minor_range': (0, 1)},
    '12.3': {'minor_range': (0, 1)},
    '12.4': {'minor_range': (0, 0)},
    '12.5': {'minor_range': (0, 1)},
    '12.6': {'minor_range': (0, 4)},
    '13.0': {'minor_range': (0, 1)},
    '13.1': {'minor_range': (0, 0)},
    '13.2': {'minor_range': (0, 1)},
    '13.3': {'minor_range': (0, 1)},
    '13.4': {'minor_range': (0, 1)},
    '13.5': {'minor_range': (0, 2)},
    '13.6': {'minor_range': (0, 0)},
}


def get_version():
    choice = random.randint(0, len(versions) - 1)
    i = 0
    for major, props in versions.items():
        if choice == i:
            minor = random.randint(int(props['minor_range'][0]), int(props['minor_range'][1]))
            return {'major': major, 'minor': minor}
        i = i + 1
