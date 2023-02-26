#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Box(tuple):
    def __init__(self, x: int, y: int, width: int, height: int):
        """This is just here for autocompletion"""
        pass

    def __new__(self, x: int, y: int, width: int, height: int):
        return tuple.__new__(Box, (x, y, width, height))

    @property
    def x(self) -> int:
        return self[0]

    @property
    def y(self) -> int:
        return self[1]

    @property
    def width(self) -> int:
        return self[2]

    @property
    def height(self) -> int:
        return self[3]

    def __repr__(self) -> str:
        return f'Box(x={self.x}, y={self.y}, width={self.width}, height={self.height})'


def main() -> None:
    try:
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
