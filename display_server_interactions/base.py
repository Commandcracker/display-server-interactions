#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This module holds the main DSI class
"""


# built-in modules
from abc import ABCMeta, abstractmethod
from platform import system

# local modules
from .window import WindowBase


class DSIBase(metaclass=ABCMeta):
    """
    Main DSI class
    """
    @abstractmethod
    def get_active_window(self) -> WindowBase:
        """
        Gets the active window.
        Returns None if no window is active.
        """

    @abstractmethod
    def get_all_windows(self) -> list[WindowBase]:
        """
        Returns a list of all Windows.
        """

    def get_window_by_pid(self, pid: int) -> WindowBase:
        """
        Get window by pid.
        Returns None if no window found.
        """
        all_window = self.get_all_windows()

        for window in all_window:
            if window.pid == pid:
                return window
        return None

    def get_window_by_name(self, name: str) -> WindowBase:
        """
        Get a window by name.
        Returns None if no window with that name is found.
        """
        all_window = self.get_all_windows()

        for window in all_window:
            if window.name is not None and name in window.name:
                return window
        return None

    @property
    def platform(self) -> str:
        """
        Returns the platform name.
        """
        return system().lower()

    @property
    def linux(self) -> bool:
        """
        Returns True if the platform is linux.
        """
        return self.platform == "linux"

    @property
    def windows(self) -> bool:
        """
        Returns True if the platform is windows.
        """
        return self.platform == "windows"

    @property
    def mac(self) -> bool:
        """
        Returns True if the platform is mac.
        """
        return self.platform == "darwin"

    # Allow dsi to be called with ’with’

    def __enter__(self):
        return self

    def __exit__(self, *_):
        pass
