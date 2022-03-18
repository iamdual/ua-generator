"""
Random User-Agent
Copyright: 2022 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import random

versions = (
    '6.1',
    '6.2',
    '6.3',
    '10.0',
)


def get_version():
    return {'major': random.choice(versions)}
