import json
import os
import re
from pathlib import Path
import requests

# Version file
DATA_PATH = os.path.realpath(os.path.dirname(__file__) + "/../../src/ua_generator/data/")
file_path = Path(DATA_PATH + "/browsers/chrome.py")
code = file_path.read_text(encoding="utf-8")

# JSON data
json_data = requests.get("https://chromiumdash.appspot.com/fetch_releases?channel=Stable&platform=Mac&num=1").text
parsed = json.loads(json_data)

# Get versions
versions_match = re.search(
    r"(versions:\s+List\[ChromiumVersion\]\s*=\s*\[\n)(.*?)(\n\s*\])",
    code,
    flags=re.DOTALL,
)

if not versions_match:
    raise RuntimeError("cannot found versions")

prefix, body, suffix = versions_match.groups()

# Extract current versions
existing_versions = set(
    (int(m), int(n), int(b))
    for m, n, b in re.findall(
        r"Version\(major=(\d+),\s*minor=(\d+),\s*build=(\d+),", body
    )
)

# Collect versions
new_entries = []
for item in parsed:
    if item.get("channel") != "Stable":
        continue

    version_str = item["version"]
    version_arr = (version_str.split(".") + ['0', '0', '0'])[:3]
    major, minor, build, *_ = map(int, version_arr)

    key = (major, minor, build)
    if key not in existing_versions:
        entry = f"    ChromiumVersion(Version(major={major}, minor={minor}, build={build}, patch=(0, 255))),"
        new_entries.append(entry)
        existing_versions.add(key)

# Update versions
if new_entries:
    updated_body = body.rstrip() + "\n" + "\n".join(new_entries)
    new_code = (
        code[:versions_match.start()] + prefix + updated_body + suffix + code[versions_match.end():]
    )
    file_path.write_text(new_code, encoding="utf-8")
    print(f"{len(new_entries)} new version(s) added.")
else:
    print("No new version found.")
