"""
Random User-Agent
Copyright: 2025 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
import re
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

    def update(self):
        super().update()
        name = "platforms/macos.py"

        src = self.get_data_content(name)
        src_match = re.search(
            r"(VERSIONS:\s+List\[Version\]\s*=\s*\[\n)(.*?)(\n\s*\])",
            src,
            flags=re.DOTALL,
        )
        assert src_match
        prefix, _, suffix = src_match.groups()

        body = ""
        for major, minor, build in self.merged:
            build_arg = f"(0, {build})" if build > 0 else "0"
            body += f"    Version(major={major}, minor={minor}, build={build_arg}),\n"

        self.set_data_content(name, src[:src_match.start()] + prefix + body.rstrip() + suffix + src[src_match.end():])
