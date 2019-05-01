#! /usr/bin/env python3
# coding: utf-8

"""
Contains the extact_img_from_odt_docx function
"""

import os
import zipfile
import shutil

from text_from_picture.extract_text import extract_text


def extact_img_from_odt_docx(file):
    """Extract image from odt and docx files, by transforming them
    into zip files"""
    _, ext = os.path.splitext(file)
    #odt to zip, then open "Pictures"
    name, _ = os.path.splitext(file)
    zip_file = "{}.{}".format(name, "zip")
    extract_dir_name = "temp_dir_{}".format(os.getpid())
    text = ""
    try:
        os.mkdir(extract_dir_name)
        shutil.copyfile(file, extract_dir_name + "/" + zip_file)
        os.chdir(extract_dir_name)
        zip_ref = zipfile.ZipFile(zip_file, 'r')
        zip_ref.extractall(".")
        zip_ref.close()
        if ext == ".odt":
            try:
                os.chdir("Pictures")
                for img_name in os.listdir("."):
                    text += extract_text(img_name)
                os.chdir("../..")
            except FileNotFoundError:
                pass
        elif ext == ".docx":
            try:
                os.chdir("word/media")
                for img_name in os.listdir("."):
                    text += extract_text(img_name)
                os.chdir("../../..")
            except FileNotFoundError:
                pass
        shutil.rmtree(extract_dir_name)
    except FileExistsError:
        pass
    return text
