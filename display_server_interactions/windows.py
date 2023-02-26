#!/usr/bin/python3
# -*- coding: utf-8 -*-

# local modules
from .base import DSIBase
from .window import WindowBase
from .image import Image
from .buttons import MouseButtons
from .box import Box

# built-in modules
from ctypes import windll, WINFUNCTYPE, c_long, Structure, create_string_buffer
from ctypes.wintypes import DWORD, RECT, BOOL, HWND, LPARAM
from ctypes import byref, create_unicode_buffer, sizeof

user32 = windll.user32
gdi32 = windll.gdi32

"""
https://learn.microsoft.com/en-us/windows/win32/api/wingdi/nf-wingdi-bitblt#SRCCOPY
Copies the source rectangle directly to the destination rectangle.
"""
SRCCOPY = 0x00CC0020
WM_CHAR = 0x0102


class POINT(Structure):
    _fields_ = [("x", c_long),
                ("y", c_long)]


class Window(WindowBase):
    def __init__(self, window) -> None:
        self.window = window

    @property
    def name(self) -> str:
        buffer = create_unicode_buffer(1024)
        user32.GetWindowTextW(self.window, buffer, sizeof(buffer))
        return buffer.value

    @property
    def pid(self) -> int:
        pid = DWORD()
        user32.GetWindowThreadProcessId(self.window, byref(pid))
        return pid.value

    @property
    def active(self) -> bool:
        return self.window == user32.GetForegroundWindow()

    @property
    def geometry(self) -> Box:
        rect = RECT()
        user32.GetWindowRect(self.window, byref(rect))
        return Box(
            x=0,
            y=0,
            width=rect.right - rect.left,
            height=rect.bottom - rect.top
        )

    def get_image(self, geometry: Box = None):
        if geometry is None:
            geometry = self.geometry

        # get the window image data
        hdcSrc = user32.GetDC(self.window)
        hdcDest = gdi32.CreateCompatibleDC(hdcSrc)
        hBitmap = gdi32.CreateCompatibleBitmap(
            hdcSrc,
            geometry.width,
            geometry.height
        )
        gdi32.SelectObject(hdcDest, hBitmap)
        user32.PrintWindow(self.window, hdcDest, 0)

        # convert the raw data into a format opencv can read
        bits = create_string_buffer(geometry.width * geometry.height * 4)
        gdi32.GetBitmapBits(
            hBitmap, geometry.width *
            geometry.height * 4,
            bits
        )
        img = Image(bits, geometry.width, geometry.height)

        # free resources
        user32.ReleaseDC(self.window, hdcSrc)
        gdi32.DeleteDC(hdcDest)
        gdi32.DeleteObject(hBitmap)

        return img

    def send_chr(self, chr: chr) -> None:
        user32.PostMessageW(self.window, WM_CHAR, ord(chr), 0)

    def send_str(self, str: str) -> None:
        for chr in str:
            self.send_chr(chr)

    def warp_pointer(self, x: int, y: int, geometry: Box = None) -> None:
        if geometry:
            rel_x, rel_y = x - geometry.x, y - geometry.y
        else:
            rel_x, rel_y = x, y
        point = POINT(rel_x, rel_y)
        user32.SetCursorPos(point.x, point.y)

    def send_mouse_click(self, x: int, y: int, button: MouseButtons = MouseButtons.LEFT) -> None:
        # Press and release the button
        down_code = 0
        up_code = 0
        if button == MouseButtons.LEFT:
            down_code = 0x201
            up_code = 0x202
        elif button == MouseButtons.MIDDLE:
            down_code = 0x207
            up_code = 0x208
        elif button == MouseButtons.RIGHT:
            down_code = 0x204
            up_code = 0x205
        elif button == MouseButtons.FORWARD:
            down_code = 0x20B
            up_code = 0x20C
        elif button == MouseButtons.BACKWARD:
            down_code = 0x20D
            up_code = 0x20E
        else:
            raise ValueError(f"Invalid button '{button}'.")

        user32.mouse_event(down_code, x, y, 0, 0)
        user32.mouse_event(up_code, x, y, 0, 0)


class DSI(DSIBase):
    def __init__(self):
        pass

    def get_active_window(self) -> WindowBase:
        # GetDesktopWindow
        return Window(user32.GetForegroundWindow())

    def get_all_windows(self) -> list[WindowBase]:
        windows = []

        @WINFUNCTYPE(BOOL, HWND, LPARAM)
        def callback(hwnd, lparam):
            windows.append(Window(hwnd))
            return True

        user32.EnumWindows(callback)

        return windows
