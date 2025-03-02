'''
# !/usr/bin/env python
# -*-coding:utf-8 -*-
Description: Split excel according to colomn A
Author     : 
Created    : 2024-09-13
'''

import pandas as pd

# 读取 Excel 文件
file_path = './input.xlsx'  # 替换为您的 Excel 文件路径
df = pd.read_excel(file_path)

# 按照第一列的值进行分组
grouped = df.groupby(df.iloc[:, 0])

# 将每个组保存为单独的 Excel 文件
for key, group in grouped:
    output_file = f'{key}.xlsx'  # 使用第一列的值作为文件名
    group.to_excel(output_file, index=False)

print("拆分完成！")