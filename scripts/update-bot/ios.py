import json
import os
import re
from pathlib import Path
import requests

# Version file
DATA_PATH = os.path.realpath(os.path.dirname(__file__) + "/../../src/ua_generator/data/")
file_path = Path(DATA_PATH + "/platforms/ios.py")
code = file_path.read_text(encoding="utf-8")

# JSON data
json_data = requests.get("https://endoflife.date/api/ios.json").text
parsed = json.loads(json_data)

# Sort JSON
parsed = sorted(parsed, key=lambda p: float(p.get('cycle', 0)))

# Get versions
versions_match = re.search(
    r"(versions:\s+List\[Version\]\s*=\s*\[\n)(.*?)(\n\s*\])",
    code,
    flags=re.DOTALL,
)

if not versions_match:
    raise RuntimeError("cannot found versions")

prefix, body, suffix = versions_match.groups()

# Extract current versions
existing_versions = []
for major, minor, b1, b2, b_simple in re.findall(r"Version\(major=(\d+),\s*minor=(\d+),\s*build=(?:\((\d+),\s*(\d+)\)|(\d+))", body):
    major = int(major)
    minor = int(minor)
    if b_simple:
        build = int(b_simple)
    else:
        build = int(b2)  # second format (0, **X**)
    existing_versions.append((major, minor, build))

# Collect versions
new_entries = []

for item in parsed:
    if "latest" not in item:
        continue

    version_str = item["latest"]
    version_arr = version_str.split(".")
    if len(version_arr) == 3:
        major, minor, build, *_ = map(int, version_str.split("."))
    else:
        major, minor, *_ = map(int, version_str.split("."))
        build = 0

    # Skip older versions
    if major < 14:
        continue

    key = (major, minor, build)
    if key not in existing_versions:
        entry = f"    Version(major={major}, minor={minor}, build=(0, {build})),"
        new_entries.append(entry)
        existing_versions.append(key)

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
