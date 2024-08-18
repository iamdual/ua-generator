"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import random
from typing import List

from ...data import browser_versions,browser_versions_idx_map
from ..version import Version, ChromiumVersion
from ...options import Options



def get_version(options: Options) -> ChromiumVersion:
    weights = None 
    min_ver_idx = browser_versions_idx_map['edge'][options.browser_version_ranges['edge'].min]
    max_ver_idx = browser_versions_idx_map['edge'][options.browser_version_ranges['edge'].max]
    versions = browser_versions['edge'][min_ver_idx:max_ver_idx+1]
    #Version ranges that range less than 3 versions currently unsupported with weighted_versions
    if options.weighted_versions and len(versions) >= 3:
        weights = [1.0] * len(versions)
        weights[-1] = 10.0
        weights[-2] = 9.0
        weights[-3] = 8.0

    choice: List[ChromiumVersion] = random.choices(versions, weights=weights, k=1)
    return choice[0]
