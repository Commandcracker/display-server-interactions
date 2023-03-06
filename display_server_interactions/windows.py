#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
All Windows specific DSI functions
"""

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
WM_KEYDOWN = 0x0100
WM_KEYUP = 0x0101
# pylint: disable=too-few-public-methods

# https://learn.microsoft.com/de-de/windows/win32/inputdev/virtual-key-codes
vk_map = {
    "lbutton": 0x01,  # VK_LBUTTON
    "rbutton": 0x02,  # VK_RBUTTON
    "cancel": 0x03,  # VK_CANCEL
    "mbutton": 0x04,  # VK_MBUTTON
    "xbutton1": 0x05,  # VK_XBUTTON1
    "xbutton2": 0x06,  # VK_XBUTTON2
    # - 0x07
    "back": 0x08,  # VK_BACK
    "tab": 0x09,  # VK_TAB
    # - 0x0A-0B
    "clear": 0x0C,  # VK_CLEAR
    "return": 0x0D,  # VK_RETURN
    # - 0x0E-0F
    "shift": 0x10,  # VK_SHIFT
    "control": 0x11,  # VK_CONTROL (STRG)
    "menu": 0x12,  # VK_MENU (ALT)
    "pause": 0x13,  # VK_PAUSE
    "capital": 0x14,  # VK_CAPITAL (caps lock)
    "kana": 0x15,  # VK_KANA
    "hangul": 0x15,  # VK_HANGUEL
    "ime_on": 0x16,  # VK_IME_ON
    "junja": 0x17,  # VK_JUNJA
    "final": 0x18,  # VK_FINAL
    "hanja": 0x19,  # VK_HANJA
    "kanji": 0x19,  # VK_KANJI
    "ime_off": 0x1A,  # VK_IME_OFF
    "escape": 0x1B,  # VK_ESCAPE
    "convert": 0x1C,  # VK_CONVERT
    "nonconvert": 0x1D,  # VK_NONCONVERT
    "accept": 0x1E,  # VK_ACCEPT
    "modechange": 0x1F,  # VK_MODECHANGE
    "space": 0x20,  # VK_SPACE
    "prior": 0x21,  # VK_PRIOR
    "next": 0x22,  # VK_NEXT
    "end": 0x23,  # VK_END
    "home": 0x24,  # VK_HOME
    "left": 0x25,  # VK_LEFT
    "up": 0x26,  # VK_UP
    "right": 0x27,  # VK_RIGHT
    "down": 0x28,  # VK_DOWN
    "select": 0x29,  # VK_SELECT
    "print": 0x2A,  # VK_PRINT
    "execute": 0x2B,  # VK_EXECUTE
    "snapshot": 0x2C,  # VK_SNAPSHOT
    "insert": 0x2D,  # VK_INSERT
    "delete": 0x2E,  # VK_DELETE
    "help": 0x2F,  # VK_HELP
    # 0-9 0x30-0x39
    # - 0x3A-40
    # A-Z 0x41-0x5A
    "lwin": 0x5B,  # VK_LWIN
    "rwin": 0x5C,  # VK_RWIN
    "apps": 0x5D,  # VK_APPS
    # - 0x5E
    "sleep": 0x5F,  # VK_SLEEP
    "numpad0": 0x60,  # VK_NUMPAD0
    "numpad1": 0x61,  # VK_NUMPAD1
    "numpad2": 0x62,  # VK_NUMPAD2
    "numpad3": 0x63,  # VK_NUMPAD3
    "numpad4": 0x64,  # VK_NUMPAD4
    "numpad5": 0x65,  # VK_NUMPAD5
    "numpad6": 0x66,  # VK_NUMPAD6
    "numpad7": 0x67,  # VK_NUMPAD7
    "numpad8": 0x68,  # VK_NUMPAD8
    "numpad9": 0x69,  # VK_NUMPAD9
    "multiply": 0x6A,  # VK_MULTIPLY
    "add": 0x6B,  # VK_ADD
    "separator": 0x6C,  # VK_SEPARATOR
    "subtract": 0x6D,  # VK_SUBTRACT
    "decimal": 0x6E,  # VK_DECIMAL
    "divide": 0x6F,  # VK_DIVIDE
    "f1": 0x70,  # VK_F1
    "f2": 0x71,  # VK_F2
    "f3": 0x72,  # VK_F3
    "f4": 0x73,  # VK_F4
    "f5": 0x74,  # VK_F5
    "f6": 0x75,  # VK_F6
    "f7": 0x76,  # VK_F7
    "f8": 0x77,  # VK_F8
    "f9": 0x78,  # VK_F9
    "f10": 0x79,  # VK_F10
    "f11": 0x7A,  # VK_F11
    "f12": 0x7B,  # VK_F12
    "f13": 0x7C,  # VK_F13
    "f14": 0x7D,  # VK_F14
    "f15": 0x7E,  # VK_F15
    "f16": 0x7F,  # VK_F16
    "f17": 0x80,  # VK_F17
    "f18": 0x81,  # VK_F18
    "f19": 0x82,  # VK_F19
    "f20": 0x83,  # VK_F20
    "f21": 0x84,  # VK_F21
    "f22": 0x85,  # VK_F22
    "f23": 0x86,  # VK_F23
    "f24": 0x87,  # VK_F24
    # - 0x88-8F
    "numlock": 0x90,  # VK_NUMLOCK
    "scroll": 0x91,  # VK_SCROLL
    # OEM 0x92-96
    # - 0x97-9F
    "lshift": 0xA0,  # VK_LSHIFT
    "rshift": 0xA1,  # VK_RSHIFT
    "lcontrol": 0xA2,  # VK_LCONTROL
    "rcontrol": 0xA3,  # VK_RCONTROL
    "lmenu": 0xA4,  # VK_LMENU
    "rmenu": 0xA5,  # VK_RMENU
    "browser_back": 0xA6,  # VK_BROWSER_BACK
    "browser_forward": 0xA7,  # VK_BROWSER_FORWARD
    "browser_refresh": 0xA8,  # VK_BROWSER_REFRESH
    "browser_stop": 0xA9,  # VK_BROWSER_STOP
    "browser_search": 0xAA,  # VK_BROWSER_SEARCH
    "browser_favorites": 0xAB,  # VK_BROWSER_FAVORITES
    "browser_home": 0xAC,  # VK_BROWSER_HOME
    "volume_mute": 0xAD,  # VK_VOLUME_MUTE
    "volume_down": 0xAE,  # VK_VOLUME_DOWN
    "volume_up": 0xAF,  # VK_VOLUME_UP
    "media_next_track": 0xB0,  # VK_MEDIA_NEXT_TRACK
    "media_prev_track": 0xB1,  # VK_MEDIA_PREV_TRACK
    "media_stop": 0xB2,  # VK_MEDIA_STOP
    "media_play_pause": 0xB3,  # VK_MEDIA_PLAY_PAUSE
    "launch_mail": 0xB4,  # VK_LAUNCH_MAIL
    "launch_media_select": 0xB5,  # VK_LAUNCH_MEDIA_SELECT
    "launch_app1": 0xB6,  # VK_LAUNCH_APP1
    "launch_app2": 0xB7,  # VK_LAUNCH_APP2
    # - 0xB8-B9
    "oem_1": 0xBA,  # VK_OEM_1
    "oem_plus": 0xBB,  # VK_OEM_PLUS
    "oem_comma": 0xBC,  # VK_OEM_COMMA
    "oem_minus": 0xBD,  # VK_OEM_MINUS
    "oem_period": 0xBE,  # VK_OEM_PERIOD
    "oem_2": 0xBF,  # VK_OEM_2
    "oem_3": 0xC0,  # VK_OEM_3
    # - 0xC1-D7
    # - 0xD8-DA
    "oem_4": 0xDB,  # VK_OEM_4
    "oem_5": 0xDC,  # VK_OEM_5
    "oem_6": 0xDD,  # VK_OEM_6
    "oem_7": 0xDE,  # VK_OEM_7
    "oem_8": 0xDF,  # VK_OEM_8
    # - 0xE0
    # OEM 0xE1
    "oem_102": 0xE2,  # VK_OEM_102
    # OEM 0xE3-E4
    "processkey": 0xE5,  # VK_PROCESSKEY
    # OEM 0xE6
    "packet": 0xE7,  # VK_PACKET
    # - 0xE8
    # OEM 0xE9-F5
    "attn": 0xF6,  # VK_ATTN
    "crsel": 0xF7,  # VK_CRSEL
    "exsel": 0xF8,  # VK_EXSEL
    "ereof": 0xF9,  # VK_EREOF
    "play": 0xFA,  # VK_PLAY
    "zoom": 0xFB,  # VK_ZOOM
    "noname": 0xFC,  # VK_NONAME
    "pa1": 0xFD,  # VK_PA1
    "oem_clear": 0xFE,  # VK_OEM_CLEAR
}


class RECT(Structure):
    """
    A structure that defines the coordinates of a rectangle.
    """
    _fields_ = [
        ("left", c_long),
        ("top", c_long),
        ("right", c_long),
        ("bottom", c_long)
    ]

# pylint: enable=too-few-public-methods


class Window(WindowBase):
    """
    An class for interacting with a window on Windows.
    """

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

    def send_chr(self, character: chr) -> None:
        vk = vk_map.get(character.lower())
        if vk is None:
            user32.PostMessageW(self.window, WM_CHAR, ord(character), 0)
        else:
            user32.PostMessageW(self.window, WM_KEYDOWN, vk, 0)
            user32.PostMessageW(self.window, WM_KEYUP, vk, 0)

    def send_str(self, string: str) -> None:
        for character in string:
            self.send_chr(character)

    def warp_pointer(self, x: int, y: int, geometry: Optional[Box] = None) -> None:
        if geometry is None:
            geometry = self.geometry
        user32.SetCursorPos(x + geometry.x, y + geometry.y)

    def send_mouse_click(self, x: int, y: int, button: MouseButtons = MouseButtons.LEFT) -> None:
        # Send the mouse click event
        if button == MouseButtons.LEFT:
            # Left button down
            user32.PostMessageW(
                self.window,
                0x201,
                0,
                x | (y << 16)
            )
            # Left button up
            user32.PostMessageW(
                self.window,
                0x202,
                0,
                x | (y << 16)
            )
        elif button == MouseButtons.RIGHT:
            # Right button down
            user32.PostMessageW(
                self.window,
                0x204,
                0,
                x | (y << 16)
            )
            # Right button up
            user32.PostMessageW(
                self.window,
                0x205,
                0,
                x | (y << 16)
            )
        elif button == MouseButtons.MIDDLE:
            # Middle button down
            user32.PostMessageW(
                self.window,
                0x207,
                0,
                x | (y << 16)
            )
            # Middle button up
            user32.PostMessageW(
                self.window,
                0x208,
                0,
                x | (y << 16)
            )
        elif button == MouseButtons.BACKWARD:
            # Backward button down
            user32.PostMessageW(
                self.window,
                0x020D,
                0,
                x | (y << 16)
            )
            # Backward button up
            user32.PostMessageW(
                self.window,
                0x020E,
                0,
                x | (y << 16)
            )
        elif button == MouseButtons.FORWARD:
            # Forward button down
            user32.PostMessageW(
                self.window,
                0x020B,
                0,
                x | (y << 16)
            )
            # Forward button up
            user32.PostMessageW(
                self.window,
                0x020C,
                0,
                x | (y << 16)
            )
        else:
            raise ValueError(f"Invalid button code '{button}'.")


class DSI(DSIBase):
    """
    Main DSI class
    """

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
