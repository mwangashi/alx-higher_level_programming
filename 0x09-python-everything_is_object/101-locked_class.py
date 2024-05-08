#!/usr/bin/python3
"""Difirne a locked class"""

class LockedClass:
    """
    Prevent the user from initiating a new locked class 
    except if the new instance attribute is called first_name.
    """

    __slots__ = ['first_name']
