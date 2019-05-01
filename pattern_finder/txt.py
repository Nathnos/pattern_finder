#! /usr/bin/env python3
# coding: utf-8

"""
Contains the txt_analysis function
"""

from pattern_finder.show import show

def txt_analysis(file_name, pattern, path):
    """Tries to finds the pattern in the text of UTF-8 encocded files"""
    try:
        with open(file_name, "r") as file:
            text = file.read().lower()
            counter = text.count(pattern)
            show(path, file_name, counter)
    except UnicodeDecodeError:
        pass
