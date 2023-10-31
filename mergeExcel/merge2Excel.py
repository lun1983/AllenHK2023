# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : merge2Excel.py.py
# Time       ：24/8/2023 23:21
# Author     ：Allen Wong
# version    ：python 3.10
# Description：to merge 2 excel files which have the same format
"""

import pandas as pd

file1 = './data/1.xls'
file2 = './data/2.xls'


def main():
    # read file
    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)

    # merge
    merge_file = pd.concat([df1, df2])

    # save file
    merge_file.to_excel('./data/result.xlsx', index='False')

    return

if __name__ == '__main__':
    main()
