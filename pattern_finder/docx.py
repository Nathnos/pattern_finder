#! /usr/bin/env python3
# coding: utf-8

"""
Contains the docx_analysis function
"""

import docx

from pattern_finder.show import show
from pattern_finder.odt_doxc_to_zip import extact_img_from_odt_docx

def docx_analysis(file, pattern, path, in_img):
    """Finds the pattern in text (and images) for .docx files"""
    document = docx.Document(file)
    counter = 0
    for para in document.paragraphs:
        counter += para.text.lower().count(pattern)
    if in_img:
        counter += extact_img_from_odt_docx(file).lower().count(pattern)
    show(path, file, counter)
