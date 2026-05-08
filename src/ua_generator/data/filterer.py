import random

from ..data.version import VersionRange
from ..options import Options


class Filterer:
    def __init__(self, versions, version_id: str, options: Options, max_weighted_version=4):
        self.versions = versions
        self._version_id = version_id
        self._options = options
        self._max_weighted_version = max_weighted_version
        self.apply_options()

    def _version_range(self, v_range: VersionRange):
        if not isinstance(v_range, VersionRange):
            raise TypeError('Parameter v_range must be type of VersionRange')

        filtered = v_range.filter(self.versions)
        if len(filtered) > 0:
            self.versions = filtered

    def _latest_versions(self, limit=1):
        if not isinstance(limit, int) or isinstance(limit, bool):
            raise TypeError('Parameter limit must be type of int')
        if limit < 1:
            raise ValueError('Parameter limit must be greater than 0')

        self.versions = self.versions[-limit:]

    def _weighted_version(self):
        if not self._options.weighted_versions:
            return

        weights = [1.0] * len(self.versions)
        for i in range(1, min(self._max_weighted_version, len(self.versions))):
            weights[-i] = 10.0 - i

        self.versions = random.choices(self.versions, weights=weights, k=1)

    def apply_options(self):
        if self._options.version_ranges and self._version_id in self._options.version_ranges:
            self._version_range(self._options.version_ranges[self._version_id])

        latest_version_limit = self._options.latest_version_limit(self._version_id)
        if latest_version_limit is not None:
            self._latest_versions(latest_version_limit)

        self._weighted_version()

        return self
