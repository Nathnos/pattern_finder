#! /usr/bin/env python3
# coding: utf-8

"""
A simple show() function
"""

import os

def show(path, file, counter):
    """Prints on the terminal"""
    if counter > 0:
        print(os.path.join(path, file), ": Nombre d'occurences :", counter)
