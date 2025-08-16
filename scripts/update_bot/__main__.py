"""
Random User-Agent
Copyright: 2025 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
import argparse

from .updaters.chrome import ChromeUpdater
from .updaters.edge import EdgeUpdater
from .updaters.firefox import FirefoxUpdater
from .updaters.ios import IOSUpdater
from .updaters.macos import MacOSUpdater

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ua-generator version updater")
    parser.add_argument("action", help="Action", choices=["update", "info"])
    parser.add_argument("--updater", "-u", help="Updater", choices=["chrome", "edge", "firefox", "ios", "macos"])
    args = parser.parse_args()
    is_all = args.updater is None

    if is_all or args.updater == "chrome":
        ChromeUpdater().action(args.action)
    if is_all or args.updater == "edge":
        EdgeUpdater().action(args.action)
    if is_all or args.updater == "firefox":
        FirefoxUpdater().action(args.action)
    if is_all or args.updater == "ios":
        IOSUpdater().action(args.action)
    if is_all or args.updater == "macos":
        MacOSUpdater().action(args.action)
