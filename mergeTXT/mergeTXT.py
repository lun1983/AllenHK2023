# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : mergeTXT.py
# Time       ：10/1/2024 16:04
# Author     ：CBIC-IT-TEAM
# version    ：python 3.11
# Conda Env  : base v23.9.0
# Description：
"""

import os


def mergetxt():
    # 获取当前文件夹路径
    folder_path = os.getcwd()

    # 合并后的文件名和路径
    merged_file = "merged.txt"
    merged_file_path = os.path.join(folder_path, merged_file)

    # 获取当前文件夹下的所有txt文件
    txt_files = [file for file in os.listdir(folder_path) if file.endswith(".txt")]

    # 打开合并后的文件，使用 'a' 模式以追加的方式写入内容
    with open(merged_file_path, 'a', encoding='utf-8') as merged:
        # 遍历每个txt文件并写入内容
        for txt_file in txt_files:
            file_path = os.path.join(folder_path, txt_file)
            with open(file_path, 'r') as file:
                content = file.read()
                merged.write(content)
                merged.write('\n')  # 在每个文件的内容后加上换行符

    print("合并完成！")

    return


def main():
    print('****** mergeTXT start *****')
    mergetxt()
    print('****** mergeTXT end *****')


if __name__ == "__main__":
    main()
