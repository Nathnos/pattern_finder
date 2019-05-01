#! /usr/bin/env python3
# coding: utf-8

"""
Contains the argparse function
"""

import argparse

def parse_arguments():
    """Denfines and returns arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--pattern",
                        help="""Pattern to find - spaces not allowed""")
    parser.add_argument("--path", help="""Search in a specific folder""")
    parser.add_argument("-sf", "--subfolders", action="store_true",
                        help="""Search also in subfolders. Can be long.""")
    parser.add_argument("-pdf", "--pdf", action="store_true",
                        help="""Search also in PDF documents. Can be long.""")
    parser.add_argument("-i", "--ignore",
                        help="""Ignore all folders and files with a specific
                        name. To define multiples forbidden folder and file
                        names, put a slash between each : 
                        fold1/fold2/readme.md""")
    parser.add_argument("--image", action="store_true",
                        help="""Also search the pattern in images. You'll need
                        tesseract to use this option. Don't work very well,
                        anyways. Can be quite long. Extensions allowed : png,
                        jpg, jpeg, bmp and webp""")
    return parser.parse_args()
