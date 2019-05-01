#! /usr/bin/env python3
# coding: utf-8

"""
Contains the launch_analysis function
"""

import os

from pattern_finder.txt import txt_analysis
from pattern_finder.docx import docx_analysis
from pattern_finder.odt import odt_analysis
from pattern_finder.pdf import pdf_analysis
from pattern_finder.extract_args import extract_args
from pattern_finder.show import show
from text_from_picture.extract_text import extract_text


def launch_analysis(next_dir=None, full_path=None, pattern=None,
                    search_options=None, forbidden_folders_and_files=None):
    """Launches analysis ; calls itself for subfolders"""
    if next_dir is None: #First run
        (full_path, pattern, in_pdf, in_subfolders, in_img,
         forbidden_folders_and_files) = extract_args()
        search_options = in_subfolders, in_pdf, in_img
    else: #Subfolders runs
        os.chdir(next_dir)
        in_subfolders, in_pdf, in_img = search_options
    image_extensions = [".png", ".jpg", ".jpeg", ".bmp", ".webp"]
    for file_or_dir in os.listdir("."):
        if(os.path.isfile(file_or_dir) and
           file_or_dir not in forbidden_folders_and_files):
            file = file_or_dir
            _, ext = os.path.splitext(file)
            if ext == ".docx":
                docx_analysis(file, pattern, full_path, in_img)
            elif ext == ".odt":
                odt_analysis(file, pattern, full_path, in_img)
            elif ext == ".pdf" and in_pdf:
                pdf_analysis(file, pattern, full_path, in_img)
            elif in_img and ext in image_extensions:
                text = extract_text(file)
                counter = text.count(pattern)
                show(full_path, file, counter)
            else: #Tries to open othe files encoded with UTF-8
                txt_analysis(file, pattern, full_path)
        elif(os.path.isdir(file_or_dir) and in_subfolders
             and file_or_dir not in forbidden_folders_and_files):
            next_dir = file_or_dir
            launch_analysis(os.path.join(".", next_dir),
                            os.path.join(full_path, next_dir),
                            pattern, search_options,
                            forbidden_folders_and_files)
    os.chdir("..") #Once a subfolder to totally done
