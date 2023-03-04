#!/usr/bin/python3
# -*- coding: utf-8 -*-

# built-in modules
from typing import Optional
from ctypes import (
    windll,
    WINFUNCTYPE,
    c_long,
    Structure,
    create_string_buffer
)
from ctypes.wintypes import (
    DWORD,
    BOOL,
    HWND,
    LPARAM
)
from ctypes import (
    byref,
    create_unicode_buffer,
    sizeof
)

# local modules
from .base import DSIBase
from .window import WindowBase
from .image import Image
from .buttons import MouseButtons
from .box import Box

user32 = windll.user32
gdi32 = windll.gdi32

"""
https://learn.microsoft.com/en-us/windows/win32/api/wingdi/nf-wingdi-bitblt#SRCCOPY
Copies the source rectangle directly to the destination rectangle.
"""
SRCCOPY = 0x00CC0020
WM_CHAR = 0x0102


class RECT(Structure):
    _fields_ = [
        ("left", c_long),
        ("top", c_long),
        ("right", c_long),
        ("bottom", c_long)
    ]


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
        user32.GetClientRect(self.window, byref(rect))

        window_rect = RECT()
        user32.GetWindowRect(self.window, byref(window_rect))

        title_bar_height = window_rect.bottom - \
            window_rect.top - (rect.bottom - rect.top)

        return Box(
            x=window_rect.left,
            y=window_rect.top + title_bar_height,
            width=rect.right - rect.left,
            height=rect.bottom - rect.top
        )

    def get_image(self, geometry: Optional[Box] = None):
        if geometry is None:
            geometry = self.geometry

        wdc = user32.GetDC(self.window)

        # adjust the bitmap size
        data_bitmap = gdi32.CreateCompatibleBitmap(
            wdc,
            geometry.width,
            geometry.height
        )

        # get the window image data
        dc_object = gdi32.CreateCompatibleDC(None)
        gdi32.SelectObject(dc_object, data_bitmap)
        gdi32.BitBlt(
            dc_object,
            0,
            0,
            geometry.width,
            geometry.height,
            wdc,
            geometry.x - self.geometry.x,
            geometry.y - self.geometry.y,
            SRCCOPY
        )

        # convert the raw data into a format opencv can read
        signed_ints_array = create_string_buffer(
            geometry.width * geometry.height * 4
        )
        gdi32.GetBitmapBits(
            data_bitmap,
            geometry.width * geometry.height * 4,
            signed_ints_array
        )
        img = Image(signed_ints_array, geometry.width, geometry.height)

        # free resources
        gdi32.DeleteObject(data_bitmap)
        gdi32.DeleteDC(dc_object)
        user32.ReleaseDC(self.window, wdc)

        return img

    def send_chr(self, chr: chr) -> None:
        user32.PostMessageW(self.window, WM_CHAR, ord(chr), 0)

    def send_str(self, str: str) -> None:
        for chr in str:
            self.send_chr(chr)

    def warp_pointer(self, x: int, y: int, geometry: Optional[Box] = None) -> None:
        if geometry is None:
            geometry = self.geometry
        user32.SetCursorPos(x + geometry.x, y + geometry.y)

    def send_mouse_click(self, x: int, y: int, button: MouseButtons = MouseButtons.LEFT) -> None:
        # Define constants for mouse button codes
        BUTTON_LEFT = 0x01
        BUTTON_RIGHT = 0x02
        BUTTON_MIDDLE = 0x04
        BUTTON_BACK = 0x05
        BUTTON_FORWARD = 0x06

        # Send the mouse click event
        if button == BUTTON_LEFT:
            # Left button down
            user32.PostMessageW(
                self.window,
                0x201,
                BUTTON_LEFT,
                x | (y << 16)
            )
            # Left button up
            user32.PostMessageW(
                self.window,
                0x202,
                BUTTON_LEFT,
                x | (y << 16)
            )
        elif button == BUTTON_RIGHT:
            # Right button down
            user32.PostMessageW(
                self.window,
                0x204,
                BUTTON_RIGHT,
                x | (y << 16)
            )
            # Right button up
            user32.PostMessageW(
                self.window,
                0x205,
                BUTTON_RIGHT,
                x | (y << 16)
            )
        elif button == BUTTON_MIDDLE:
            # Middle button down
            user32.PostMessageW(
                self.window,
                0x207,
                BUTTON_MIDDLE,
                x | (y << 16)
            )
            # Middle button up
            user32.PostMessageW(
                self.window,
                0x208,
                BUTTON_MIDDLE,
                x | (y << 16)
            )
        elif button == BUTTON_BACK:
            # Backward button down
            user32.PostMessageW(
                self.window,
                0x020D,
                BUTTON_BACK,
                x | (y << 16)
            )
            # Backward button up
            user32.PostMessageW(
                self.window,
                0x020E,
                BUTTON_BACK,
                x | (y << 16)
            )
        elif button == BUTTON_FORWARD:
            # Forward button down
            user32.PostMessageW(
                self.window,
                0x020B,
                BUTTON_FORWARD,
                x | (y << 16)
            )
            # Forward button up
            user32.PostMessageW(
                self.window,
                0x020C,
                BUTTON_FORWARD,
                x | (y << 16)
            )
        else:
            raise ValueError(f"Invalid button code '{button}'.")


class DSI(DSIBase):
    def __init__(self):
        pass

    def get_active_window(self) -> WindowBase:
        # GetDesktopWindow
        return Window(user32.GetForegroundWindow())

    def get_all_windows(self) -> list[WindowBase]:
        windows = []

        @WINFUNCTYPE(BOOL, HWND, LPARAM)
        def callback(hwnd, _unused):
            windows.append(Window(hwnd))
            return True

        user32.EnumWindows(callback)

        return windows
