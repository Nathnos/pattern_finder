#! /usr/bin/env python3
# coding: utf-8

"""
Contains the pdf_analysis function
"""

import sys

import PyPDF2

from pattern_finder.show import show
from pattern_finder.pdf_image_extractor import extract_images_from_pdf


if not sys.warnoptions:#Ignore PdfReadWarning
    import warnings
    warnings.simplefilter("ignore")

def pdf_analysis(file_name, pattern, path, in_img):
    """Finds the pattern in text (and images) for .pdf files"""
    counter = 0
    with open(file_name, "rb") as file:
        read_pdf = PyPDF2.PdfFileReader(file)
        for i in range(read_pdf.getNumPages()):
            text = read_pdf.getPage(i).extractText().lower()
            counter += text.count(pattern)
        if in_img:
            counter += extract_images_from_pdf(file).count(pattern)
    show(path, file_name, counter)
