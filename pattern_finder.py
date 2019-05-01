#! /usr/bin/env python3
# coding: utf-8

"""
Contains main function, launches the analysis
"""

from pattern_finder.launch_analysis import launch_analysis


def main():
    """
    Launches the analysis, for docx, odt, pdf and other UTF8-encocded files
    """
    launch_analysis()

if __name__ == "__main__":
    main()
