#!/usr/bin/python3
# -*- coding: utf-8 -*-

from display_server_interactions import DSI
from numpy import array
from cv2 import imshow, waitKey

try:
    from rich import print
except ImportError:
    pass


def main() -> None:
    with DSI() as dsi:
        windows = dsi.get_all_windows()
        print("Windows:", windows)
        window = dsi.get_active_window()

        print("Name:", window.name)
        print("Active:", window.active)
        print("PID:", window.pid)
        if hasattr(window, "xid"):
            print("XID:", window.xid)
        print("Geometry:", window.geometry)

        window.send_str("Hello World")
        window.send_chr("Up")

        window.warp_pointer(100, 100)
        window.send_mouse_click(100, 100)

        img = window.get_image()
        print(img)

        print(img.get_pixel(200, 200))
        imshow('img', array(img))
        while True:
            if waitKey(1) & 0xFF == ord('q'):
                break


if __name__ == "__main__":
    main()
