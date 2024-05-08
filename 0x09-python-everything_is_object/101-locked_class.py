#!/usr/bin/python3
"""Difirne a locked class"""

    class Lockedclass:
    """
    Prevent the user from initiating a new locked class 
    except if the new instance attribute is called first_name.
    """

    _slots_ = ['first_name']
