"""
Random User-Agent
Copyright: 2025 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
import requests

from . import Updater


class MacOSUpdater(Updater):
    def fetch_versions(self):
        obj = requests.get("https://endoflife.date/api/macos.json").json()
        for item in obj:
            if "latest" not in item:
                continue

            version_str = item["latest"]
            version_arr = (version_str.split(".") + ["0", "0", "0"])[:3]
            major, minor, build, *_ = map(int, version_arr)

            if major <= 10:
                continue

            self.versions.append((major, minor, build))

    def fetch_current(self):
        from src.ua_generator.data.platforms.macos import VERSIONS
        for version in VERSIONS:
            self.current.append((version.major, version.minor, version.build))
