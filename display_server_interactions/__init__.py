#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This module initializes DSI
"""

# built-in modules
from platform import system as __system

# local modules
from .exceptions import (
    DisplayServerNotSupportedError as __DisplayServerNotSupportedError,
    OSNotSupportedError as __OSNotSupportedError
)

__version__ = "0.0.dev10"
__author__ = "Commandcracker"

__os_name = __system().lower()

if __os_name == "linux":
    from .util import detect_linux_display_server as __detect_linux_display_server
    from .util import LinuxDisplayServer as __LinuxDisplayServer
    __linux_display_server = __detect_linux_display_server()

    if __linux_display_server is __LinuxDisplayServer.X11:
        from .linux import DSI
    elif __linux_display_server is __LinuxDisplayServer.WAYLAND:
        raise NotImplementedError("Wayland is not yet implemented.")
    else:
        raise __DisplayServerNotSupportedError(
            "Your display server is not supported."
        )

elif __os_name == "windows":
    from .windows import DSI

elif __os_name == "darwin":
    raise NotImplementedError("MacOS is not yet implemented.")

else:
    raise __OSNotSupportedError("Your OS is not supported.")

__all__ = ["DSI"]
