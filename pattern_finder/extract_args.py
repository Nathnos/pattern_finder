#! /usr/bin/env python3
# coding: utf-8

"""
Contains the extract_args function
"""

import os
import logging as lg

from pattern_finder.parse_arguments import parse_arguments

def ask_path(full_path=None):
    """Defines a correct path"""
    if full_path is None: #If it's not the first run of ask_path()
        full_path = input()
    try:
        os.chdir(full_path) #Setting up for search
    except FileNotFoundError as error:
        lg.error("%s\nPlease enter a valid path", error)
        ask_path()
    except NotADirectoryError as error:
        lg.error("%s\nPlease enter a valid path", error)
        ask_path()
    except TypeError:
        lg.error("%s\nPlease enter a valid path", error)
        ask_path()
    return full_path

def extract_args():
    """Extract arguments, and tries to go to specified folder"""
    args = parse_arguments()
    if args.ignore is not None:
        forbidden_folders_and_files = args.ignore.split("/")
    else:
        forbidden_folders_and_files = []
    full_path = args.path
    if full_path is not None:
        full_path = ask_path(full_path)
    else:
        full_path = "."
        os.chdir(full_path)
    if args.pattern is None:
        print("Please enter the pattern (you can also use -p argument) :")
        pattern = input()
    else:
        pattern = args.pattern
    return (full_path, pattern.lower(), args.pdf, args.subfolders,
            args.image, forbidden_folders_and_files)
