# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : PDF2EXCEL.py
# Time       ：13/10/2023 20:40
# Author     ：Allen Wong
# version    ：python 3.10
# Description：
"""

import tabula
import os
import camelot.io as camelot
import pandas

PDF_FILE_LIST = []


def readCheckfileName():
    for filename in os.listdir('./'):
        if filename.endswith('.pdf') or filename.endswith('.PDF'):
            PDF_FILE_LIST.append('./' + filename)
    return PDF_FILE_LIST


def pdf2excel(pdffile):
    print('input1:' + pdffile)
    # output filename
    output_file = '.' + pdffile.split('.')[1] + '.csv'
    output_file_xlsx = '.' + pdffile.split('.')[1] + '.xlsx'

    print('output:' + output_file)

    # use camelot to transform
    # tablex = camelot.read_pdf(pdffile, pages='1', flavor='stream')
    # tablex[0].df
    # tablex.export(output_file, f='csv')

    # use tabula
    tabula.convert_into(pdffile, output_file, output_format='csv', pages='all')


    return


def main():
    print('PDF2EXCEL start')
    # 当前文件夹下的所有doc和docx文件名读到 CHECK_FILE[]
    PDF_FILE_LIST = readCheckfileName()

    # 处理每一个PDF文件
    for pdffile in PDF_FILE_LIST:
        pdf2excel(pdffile)


if __name__ == "__main__":
    main()
