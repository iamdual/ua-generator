"""
Random User-Agent
Copyright: 2025 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
import requests

from . import Updater

class EdgeUpdater(Updater):
    def fetch_versions(self):
        obj = requests.get("https://edgeupdates.microsoft.com/api/products").json()
        for item in obj:
            if item.get("Product") != "Stable":
                continue

            if "Releases" not in item:
                continue

            for release in item["Releases"]:
                if "Platform" not in release or release["Platform"] != "Windows":
                    continue

                version_str = release["ProductVersion"]
                version_arr = (version_str.split(".") + ['0', '0', '0'])[:3]
                major, minor, build, *_ = map(int, version_arr)
                self.versions.append((major, minor, build))

    def fetch_current(self):
        from src.ua_generator.data.browsers.edge import VERSIONS
        for version in VERSIONS:
            self.current.append((version.major, version.minor, version.build))
