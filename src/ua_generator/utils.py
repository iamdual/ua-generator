"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
import random
from typing import Union


def contains(t: Union[str, tuple, list], val: str) -> bool:
    if type(t) is str and t == val:
        return True
    if (type(t) is tuple or type(t) is list) and val in t:
        return True

    return False


def contains_multiple(t: Union[str, tuple, list], arr: Union[tuple, list]) -> bool:
    for val in arr:
        if contains(t, val):
            return True

    return False


def choice(t):
    if type(t) is str:
        return t
    if type(t) is tuple or type(t) is list:
        return random.choice(t)

    return None
