# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : mergePDF2.py
# Time       ：2/11/2023 19:39
# Author     ：Allen Wong
# version    ：python 3.11
# Conda Env  : CBIC v23.9.0
# Description：
"""

import PyPDF2
import os


def mergePDF():
    # 获取当前目录下的所有 PDF 文件
    pdf_files = [xfile for xfile in os.listdir('./') if (xfile.endswith('.pdf') or xfile.endswith('.PDF'))]

    if len(pdf_files) == 0:
        print('error: no .pdf file found.')
        exit(1)
    # # 按文件名排序
    pdf_files.sort()

    # 创建一个 PDFWriter 对象
    pdf_writer = PyPDF2.PdfWriter()
    # show files to be merged
    # print(pdf_files)

    if not os.path.exists('./output'):
        os.mkdir('./output')
    # 合并 PDF 文件
    cnt = 0
    for yfile in pdf_files:
        print(str(cnt + 1) + ':' + yfile)
        with open(yfile, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            # 将每个文件的所有页面添加到 PDFWriter 对象中
            for page_num in range(pdf_reader.numPages):
                pagex = pdf_reader.getPage(page_num)
                pdf_writer.addPage(pagex)
            # 将合并后的 PDF 保存到文件 ( 特别要注意： pdf_writer.W
            # RITE这里的缩进要和上面的pdf_writer.addPage在一个缩进上，否则会报错。）
            output_filename = './output/merged.pdf'
            with open(output_filename, 'wb') as output_file:
                pdf_writer.write(output_file)
        cnt += 1
    return


def main():
    print('******mergePDF2 start*****')
    mergePDF()
    print('******mergePDF2 end*****')
    return


if __name__ == "__main__":
    main()
