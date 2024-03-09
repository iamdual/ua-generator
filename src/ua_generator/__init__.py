"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
from . import user_agent


def generate(**kwargs):
    return user_agent.UserAgent(**kwargs)
