"""
Random User-Agent
Copyright: 2025 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
import requests

from . import Updater


class IOSUpdater(Updater):
    def fetch_versions(self):
        obj = requests.get("https://endoflife.date/api/ios.json").json()
        for item in obj:
            if "latest" not in item:
                continue

            version_str = item["latest"]
            version_arr = (version_str.split(".") + ['0', '0', '0'])[:3]
            major, minor, build, *_ = map(int, version_arr)

            if major < 14:
                continue

            self.versions.append((major, minor, build))

    def fetch_current(self):
        from src.ua_generator.data.platforms.ios import VERSIONS
        for version in VERSIONS:
            self.current.append((version.major, version.minor, version.build))
