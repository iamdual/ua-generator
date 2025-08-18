"""
Random User-Agent
Copyright: 2025 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
import os
from pathlib import Path

from src.ua_generator import data as _data

DATA_PATH = os.path.dirname(_data.__file__)


class Updater(object):
    def __init__(self):
        self.versions = []
        self.current = []
        self.merged = []

    def get_title(self):
        title = self.__class__.__name__.removesuffix("Updater")
        title = title.replace("IOS", "iOS").replace("MacOS", "macOS")
        return title

    def get_data_content(self, filename):
        return Path(DATA_PATH, filename).read_text(encoding="utf-8")

    def set_data_content(self, filename, source):
        return Path(DATA_PATH, filename).write_text(source, encoding="utf-8")

    def fetch_current(self):
        pass

    def fetch_versions(self):
        pass

    def merge_versions(self):
        merged = {}

        for major, minor, build in self.current + self.versions:
            key = (major, minor)
            if key not in merged or build > merged[key]:
                merged[key] = build

        self.merged = [(major, minor, build) for (major, minor), build in sorted(merged.items())]

    def prepare(self):
        self.fetch_current()
        self.fetch_versions()
        self.merge_versions()

    def update(self):
        print("Updating {}...".format(self.get_title()))
        self.prepare()

    def info(self):
        print("{} version info".format(self.get_title()))
        self.prepare()

        print("Current versions:")
        print(self.current)
        print("Recent versions:")
        print(self.versions)
        print("Merged versions:")
        print(self.merged)
        print("\n")

    def action(self, action):
        if action == "update":
            self.update()
        if action == "info":
            self.info()
        return self
