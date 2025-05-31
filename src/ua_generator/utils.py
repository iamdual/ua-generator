"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
import random
from typing import Union, Optional


def choice(t: Optional[Union[str, tuple, list]]) -> Optional[str]:
    if isinstance(t, str):
        return t
    if isinstance(t, tuple) or isinstance(t, list):
        return random.choice(t)

    return None
