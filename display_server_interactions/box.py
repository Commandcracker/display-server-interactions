#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This module provides a Box class that represents a rectangle with a position and size.
"""


class Box(tuple):
    """
    A Box represents a rectangle with a position and size.
    """

    def __init__(self, x: int, y: int, width: int, height: int):
        """This is just here for autocompletion"""

    def __new__(cls, x: int, y: int, width: int, height: int):
        return tuple.__new__(Box, (x, y, width, height))

    @property
    # pylint: disable-next=invalid-name
    def x(self) -> int:
        """
        Gets the x-coordinate of the box.
        """
        return self[0]

    @property
    # pylint: disable-next=invalid-name
    def y(self) -> int:
        """
        Gets the y-coordinate of the box.
        """
        return self[1]

    @property
    def width(self) -> int:
        """
        Gets the width of the box.
        """
        return self[2]

    @property
    def height(self) -> int:
        """
        Gets the height of the box.
        """
        return self[3]

    def __repr__(self) -> str:
        return f'Box(x={self.x}, y={self.y}, width={self.width}, height={self.height})'


def main() -> None:
    """
    Creates and displays an example Box object.
    """
    try:
        # pylint: disable-next=import-outside-toplevel, redefined-builtin
        from rich import print
    except ImportError:
        pass
    box = Box(100, 200, 300, 400)
    print(box)
    print(f"x={box.x}")
    print(f"y={box.y}")
    print(f"width={box.width}")
    print(f"height={box.height}")


if __name__ == "__main__":
    main()
