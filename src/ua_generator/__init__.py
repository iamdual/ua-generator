"""
Random User-Agent
Copyright: 2022 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
from . import useragent


def generate(**kwargs):
    return useragent.UserAgent().generate(**kwargs)
