#!/usr/bin/python3
# -*- coding: utf-8 -*-
# TODO: add way to get pixel from image

class Image(object):
    """
    A class to that holds the raw data of an image.
    Use np.array(Image) to get a numpy array of the image.
    """

    def __init__(self, data, width, height):
        self.data = data
        self.width = width
        self.height = height

    @property
    def __array_interface__(self):
        """
        https://docs.scipy.org/doc/numpy/reference/arrays.interface.html
        """
        return {
            "version": 3,
            "shape": (self.height, self.width, 4),
            "typestr": "|u1",
            "data": self.data,
        }
