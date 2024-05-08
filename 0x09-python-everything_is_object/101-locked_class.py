#!/usr/bin/python3
"""This creates a class that prevents dynamic attributes"""


class LockedClass:
    """This object prevents dynamic attribute"""

    __slots__ = ['first_name']
