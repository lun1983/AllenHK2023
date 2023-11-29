# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : genRenewalPolicy.py
# Time       ：28/11/2023 23:04
# Author     ：Allen Wong
# version    ：python 3.11
# Conda Env  : CBIC v23.9.0
# Description：
"""

import os
import PyPDF2

pdf_list = []


def mkdir_out():
    if not os.path.exists('./output'):
        os.mkdir('./output')
    return


# 读取当前目录下的pdf文件到PDF_LIST[]
def read_pdf_to_list():
    for filename in os.listdir('./'):
        if (filename.endswith('.pdf') or filename.endswith('.PDF')) and '~$' not in filename:
            pdf_list.append('./' + filename)
    return


def main():
    print('******genRenewalPolicy start*****')
    read_pdf_to_list()
    mkdir_out()
    cnt = 0
    for xfile in pdf_list:
        print(str(cnt + 1) + ':' + xfile)
        pdf_pswd = ''
        pdf_filename = ''
        with open(xfile, 'rb') as pdffile:
            pdf_reader = PyPDF2.PdfFileReader(pdffile)
            pdf_writer = PyPDF2.PdfWriter()
            # 总页数
            numpages = pdf_reader.numPages

            # 逐页读取
            for pagenum in range(numpages):
                page = pdf_reader.getPage(pagenum)
                text = page.extractText()

                # 将text按行分割
                lines = text.split()
                # print(lines)

                # 找到保单号
                for word in lines:
                    if 'CCI/' in word:
                        print(word)
                        pdf_pswd = word.split('/')[-1]
                        pdf_filename = '-'.join(word.split('/')[1:4])

                # 写PDF
                pdf_writer.add_page(page)
            # 如果找到了,则写结果文件
            if pdf_pswd != '' and pdf_filename != '':
                output_filename = f'./output/{pdf_filename}.pdf'
                # set password : %pdf_pswd%
                pdf_writer.encrypt(pdf_pswd)
                # write pdf
                pdf_writer.write(output_filename)

        cnt += 1
    print('******genRenewalPolicy end*****')


if __name__ == "__main__":
    main()
