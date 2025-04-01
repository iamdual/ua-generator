import random

from ..data.version import VersionRange


class Filterer:
    def __init__(self, versions):
        self.versions = versions

    def version_range(self, version_ranges: VersionRange):
        filtered = version_ranges.filter(self.versions)
        if len(filtered) > 0:
            self.versions = filtered

    def weighted_versions(self, weights=None, max_range=4):
        if weights is None:
            weights = [1.0] * len(self.versions)
            for i in range(1, min(max_range, len(self.versions))):
                weights[-i] = 10.0 - i
        self.versions = random.choices(self.versions, weights=weights, k=1)
