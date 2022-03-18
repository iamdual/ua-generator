"""
Random User-Agent
Copyright: 2022 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""


def version(version_dict, strip_zero=False):
    v_str = str(version_dict['major'])

    if 'minor' in version_dict and (
            strip_zero is False or
            (strip_zero is True and version_dict['minor'] > 0)):
        v_str += '.' + str(version_dict['minor'])

    return v_str
