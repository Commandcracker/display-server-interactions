#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This is an example of DSI
"""

# local modules
from . import DSI


def main() -> None:
    """
    This is an example of DSI
    """
    with DSI() as dsi:
        window = dsi.get_active_window()

        print("Active window: ")
        print(f"\tName: {window.name}")
        print(f"\tPID: {window.pid}")
        if window.xid:
            print(f"\tXID: {window.xid}")
        print(f"\tGeometry: {window.geometry}")


if __name__ == "__main__":
    main()
