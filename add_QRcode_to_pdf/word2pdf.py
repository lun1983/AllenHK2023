# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : word2pdf.py
# Time       ：8/9/2023 09:11
# Author     ：Allen Wong
# version    ：python 3.10
# Description：
"""

from docx2pdf import convert

file1='./temp_replace.docx'
file2='./temp_replace.pdf'

convert(file1,file2)
print('convert finished.')
