#!/usr/bin/python3
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
from .window import WindowBase
#from . import __os_name


class DSIBase(object, metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def get_active_window() -> WindowBase:
        """
        Gets the active window.
        Returns None if no window is active.
        """
        pass

    @staticmethod
    @abstractmethod
    def get_all_windows() -> list:
        """
        Returns a list of all Windows.
        """
        pass

    @classmethod
    def get_window_by_pid(cls, pid: int) -> WindowBase:
        """
        Get window by pid.
        Returns None if no window found.
        """
        all_window = cls.get_all_windows()

        for window in all_window:
            if window.pid == pid:
                return window

    @classmethod
    def get_window_by_name(cls, name: str) -> WindowBase:
        """
        Get a window by name.
        Returns None if no window with that name is found.
        """
        all_window = cls.get_all_windows()

        for window in all_window:
            if window.name is not None and name in window.name:
                return window

    # @property
    # def platform(self) -> str:
    #    """
    #    Returns the platform name.
    #    """
    #    return __os_name

    # @property
    # def linux(self) -> bool:
    #    """
    #    Returns True if the platform is linux.
    #    """
    #    return self.platform == "linux"

    # @property
    # def windows(self) -> bool:
    #    """
    #    Returns True if the platform is windows.
    #    """
    #    return self.platform == "windows"

    # @property
    # def mac(self) -> bool:
    #    """
    #    Returns True if the platform is mac.
    #    """
    #    return self.platform == "darwin"
