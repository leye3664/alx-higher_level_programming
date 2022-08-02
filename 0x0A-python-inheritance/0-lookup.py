#!/usr/bin/python3
"""
File: 0-lookup.py
Desc: This module contains one function; lookup(obj)
Author: Oluleye Olumide (leye)
Date Created: 01 Aug 2022
"""


def lookup(obj):
    """
    Returns the list of available attributes and
    methods of an object
    """
    return dir(obj)
