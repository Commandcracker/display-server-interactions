#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
The Image module contains a class to hold the raw data of an image.
"""

from typing import Tuple


class Image:
    """
    A class to that holds the raw data of an image.
    Use np.array(Image) to get a numpy array of the image.
    """

    def __init__(self, data, width, height):
        self.data = data
        self.width = width
        self.height = height

    @property
    def __array_interface__(self) -> dict:
        """
        A property method that returns an interface
        for the numpy array interface.
        https://docs.scipy.org/doc/numpy/reference/arrays.interface.html
        """
        return {
            "version": 3,
            "shape": (self.height, self.width, 4),
            "typestr": "|u1",
            "data": self.data,
        }

    def __repr__(self) -> str:
        return f"Image(width={self.width}, height={self.height})"

    # pylint: disable-next=invalid-name
    def get_pixel(self, x: int, y: int) -> Tuple[int, int, int, int]:
        """
        This function retrieves the RGBA values of the pixel,
        located at the specified coordinates
        and returns them as a 4-tuple integer.
        """
        pixel_start_index = (y * self.width + x) * 4
        pixel_data = self.data[pixel_start_index:pixel_start_index + 4]
        return tuple(pixel_data)
