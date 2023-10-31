# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : docx2pdf.py
# Time       ：29/10/2023 15:48
# Author     ：Allen Wong
# version    ：python 3.10
# Description：
"""
import os
import sys
from docx import Document
from docx.shared import Inches
from docx2pdf import convert


def main():
    print('docx2pdf start')
    inputfile = './OUT_DOCX/barcoce_1.docx'
    outputfile = './OUT_PDF/barcoce_1.pdf'
    convert(inputfile, outputfile)


if __name__ == "__main__":
    main()
