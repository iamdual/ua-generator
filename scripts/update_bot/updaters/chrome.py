"""
Random User-Agent
Copyright: 2025 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
import requests

from . import Updater


class ChromeUpdater(Updater):
    def fetch_versions(self):
        obj = requests.get("https://chromiumdash.appspot.com/fetch_releases?channel=Stable&platform=Mac&num=1").json()
        for item in obj:
            if item.get("channel") != "Stable":
                continue

            version_str = item["version"]
            version_arr = (version_str.split(".") + ['0', '0', '0'])[:3]
            major, minor, build, *_ = map(int, version_arr)
            self.versions.append((major, minor, build))

    def fetch_current(self):
        from src.ua_generator.data.browsers.chrome import VERSIONS
        for version in VERSIONS:
            self.current.append((version.major, version.minor, version.build))
