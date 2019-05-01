#! /usr/bin/env python3
# coding: utf-8

"""
Contains the odt_analysis function
"""

from odf.opendocument import load
from odf import text, teletype

from pattern_finder.show import show
from pattern_finder.odt_doxc_to_zip import extact_img_from_odt_docx

def odt_analysis(file, pattern, path, in_img):
    """Finds the pattern in text (and images) for .odt files"""
    counter = 0
    textdoc = load(file)
    all_paragraphs = textdoc.getElementsByType(text.P)
    for paragraph in all_paragraphs:
        counter += teletype.extractText(paragraph).lower().count(pattern)
    if in_img:
        counter += extact_img_from_odt_docx(file).lower().count(pattern)
    show(path, file, counter)
