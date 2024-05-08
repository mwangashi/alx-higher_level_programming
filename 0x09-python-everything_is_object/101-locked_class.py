#!/usr/bin/python3
"""Difirne a locked class"""


class LockedClass:
    """
    Prevent initiating a dynamic attribute
    """

    __slots__ = ['first_name']
