"""
Random User-Agent
Copyright: 2025 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
import requests

from . import Updater


class FirefoxUpdater(Updater):
    def fetch_versions(self):
        obj = requests.get("https://product-details.mozilla.org/1.0/firefox_versions.json").json()
        version_str = obj["LATEST_FIREFOX_VERSION"]
        version_arr = (version_str.split(".") + ['0', '0', '0'])[:3]
        major, minor, build, *_ = map(int, version_arr)
        self.versions.append((major, minor, build))

    def fetch_current(self):
        from src.ua_generator.data.browsers.firefox import VERSIONS
        for version in VERSIONS:
            self.current.append((version.major, version.minor, version.build))
