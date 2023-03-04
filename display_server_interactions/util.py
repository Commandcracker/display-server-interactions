#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os import getenv
from enum import Enum


class LinuxDisplayServer(Enum):
    WAYLAND = "wayland"
    X11 = "x11"
    UNKNOWN = "Unknown"


def detect_linux_display_server() -> LinuxDisplayServer:
    xdg_session_type = getenv("XDG_SESSION_TYPE")
    if xdg_session_type == "wayland":
        return LinuxDisplayServer.WAYLAND

    if xdg_session_type == "x11":
        return LinuxDisplayServer.X11

    if getenv("WAYLAND_DISPLAY") is not None:
        return LinuxDisplayServer.WAYLAND

    if getenv("DISPLAY") is not None:
        return LinuxDisplayServer.X11

    # maby check if a process is called "Xwayland" or "Xorg"

    return LinuxDisplayServer.UNKNOWN
