"""
Random User-Agent
Copyright: 2025 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
import re
import requests
from . import Updater


class ChromeUpdater(Updater):
    def fetch_versions(self):
        obj = requests.get("https://chromiumdash.appspot.com/fetch_releases?channel=Stable&platform=Mac&num=1").json()
        for item in obj:
            if item.get("channel") != "Stable":
                continue

            version_str = item["version"]
            version_arr = (version_str.split(".") + ["0", "0", "0"])[:3]
            major, minor, build, *_ = map(int, version_arr)
            self.versions.append((major, minor, build))

    def fetch_current(self):
        from src.ua_generator.data.browsers.chrome import VERSIONS
        for version in VERSIONS:
            self.current.append((version.major, version.minor, version.build))

    def update(self):
        super().update()
        name = "browsers/chrome.py"

        src = self.get_data_content(name)
        src_match = re.search(
            r"(VERSIONS:\s+List\[ChromiumVersion\]\s*=\s*\[\n)(.*?)(\n\s*\])",
            src,
            flags=re.DOTALL,
        )
        assert src_match
        prefix, _, suffix = src_match.groups()

        body = ""
        for major, minor, build in self.merged:
            body += f"    ChromiumVersion(Version(major={major}, minor={minor}, build={build}, patch=(0, 255))),\n"

        self.set_data_content(name, src[:src_match.start()] + prefix + body.rstrip() + suffix + src[src_match.end():])
