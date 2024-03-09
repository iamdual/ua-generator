"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""


def ch_brand_list(brand_list: list):
    serialized = []
    for _dict in brand_list:
        serialized.append('"' + _dict['brand'] + '";v="' + _dict['version'] + '"')

    return ', '.join(serialized)


def ch_bool(val: bool):
    return '?1' if val else '?0'


def ch_string(val: str):
    return '"' + val + '"'
