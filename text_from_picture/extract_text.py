#! /usr/bin/env python3
# coding: utf-8

"""
Extracts text using tesseract
"""

import os

from PIL import Image
import pytesseract
import cv2

def extract_text(image):
    """Create a temp gray image, the extract text out of it, with tesseract"""
    image = cv2.imread(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 3)
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    return text.lower()
