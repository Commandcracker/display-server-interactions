#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This module provides a class for interacting with windows
"""

# built-in modules
from abc import ABCMeta, abstractmethod
from typing import Optional

# local modules
from .image import Image
from .buttons import MouseButtons
from .box import Box


class WindowBase(metaclass=ABCMeta):
    """
    An abstract base class that defines the interface for interacting with a window.
    """
    @property
    @abstractmethod
    def name(self) -> str:
        """
        Returns the name of the window.
        Returns None if no name is available.
        """

    @property
    @abstractmethod
    def pid(self) -> int:
        """
        Returns the process id of the window.
        Returns None if no pid is available.
        """

    @property
    @abstractmethod
    def active(self) -> bool:
        """
        Returns True if the window is active.
        Returns False if the window is not active.
        """

    @property
    @abstractmethod
    def geometry(self) -> Box:
        """
        Returns: tuple: (x, y, width, height)
        """

    @abstractmethod
    def get_image(self, geometry: Optional[Box] = None) -> Image:
        # pylint: disable=line-too-long
        """
        Returns an Image of the window.
        With the geometry parameter you can specify a sub-region of the window that will be captured.
        """
        # pylint: enable=line-too-long

    @abstractmethod
    def send_chr(self, character: chr) -> None:
        """
        send the keystroke of the given character to the window.
        """

    @abstractmethod
    def send_str(self, string: str) -> None:
        """
        Send keystrokes equivalent to the string you pass to the window.
        """

    @abstractmethod
    # pylint: disable-next=invalid-name
    def warp_pointer(self, x: int, y: int, geometry: Optional[Box] = None) -> None:
        """
        Moves the pointer relative to the window to the given coordinates.
        """

    @abstractmethod
    # pylint: disable-next=invalid-name
    def send_mouse_click(self, x: int, y: int, button: MouseButtons = MouseButtons.LEFT) -> None:
        """
        Send a mouse click to the window at the given coordinates.
        On some windows/applications you need to move the pointer with warp_pointer() first.
        """

    def __repr__(self) -> str:
        # pylint: disable=line-too-long
        name = self.name
        if name:
            return f'Window(name="{self.name}", pid={self.pid}, active={self.active}, geometry={self.geometry})'
        return f'Window(pid={self.pid}, active={self.active}, geometry={self.geometry})'
        # pylint: enable=line-too-long
