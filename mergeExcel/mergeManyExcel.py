# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : mergeManyExcel.py.py
# Time       ：24/8/2023 23:43
# Author     ：Allen Wong
# version    ：python 3.10
# Description：to Merge many excel files which have the same format.
# 当合并表头一样时，pandas会自动去除相同的表头
"""

import pandas as pd
import glob
import os

excel_files = glob.glob('./data/*.xls')

# delete output file if exists
if os.path.exists('./data/result.xlsx'):
    os.remove('./data/result.xlsx')
    print('Delete result.xlsx done.')

# crate DataFrame
mergedata = pd.DataFrame()

# define a df list
df_list = []
# go through all the files
for file in excel_files:
    # read excel file
    xls = pd.ExcelFile(file)
    sheets = xls.sheet_names

    # match through all the sheets
    for sheet in sheets:
        df = pd.read_excel(file, sheet_name=sheet)
        df_list.append(df)

# merge data together
mergedata = pd.concat(df_list, ignore_index=False)
# write file
mergedata.to_excel('./data/result.xlsx', index=False)
print('Write result.xlsx done.')
