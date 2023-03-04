#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Exceptions for DSI."""


class DisplayServerNotSupportedError(Exception):
    """Exception raised when the display server is not supported."""


class OSNotSupportedError(Exception):
    """Exception raised when the operating system is not supported."""
