"""
Random User-Agent
Copyright: 2025 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""


class Updater(object):
    def __init__(self):
        self.versions = []
        self.current = []

    def get_title(self):
        title = self.__class__.__name__.removesuffix("Updater")
        title = title.replace("IOS", "iOS").replace("MacOS", "macOS")
        return title

    def fetch_current(self):
        pass

    def fetch_versions(self):
        pass

    def update(self):
        print("Updating {}".format(self.get_title()))
        self.fetch_current()
        self.fetch_versions()

    def info(self):
        print("{} version info".format(self.get_title()))
        self.fetch_current()
        self.fetch_versions()

        print("Current versions:")
        print(self.current)
        print("Recent versions:")
        print(self.versions)
        print("\n")

    def action(self, action):
        if action == "update":
            self.update()
        if action == "info":
            self.info()
        return self
