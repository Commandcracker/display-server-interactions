from display_server_interactions import DSI
import numpy as np
import cv2

with DSI() as dsi:
    windows = dsi.get_all_windows()
    print("Windows:", windows)
    window = dsi.get_active_window()

    print("Name:", window.name)
    print("PID:", window.pid)
    if window.xid:
        print("XID:", window.xid)
    print("Geometry:", window.geometry)

    window.send_str("Hello World")

    window.warp_pointer(100, 100)
    window.send_mouse_click(100, 100)

    img = np.array(window.get_image())
    cv2.imshow('img', img)
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
