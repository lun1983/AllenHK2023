"""
# !/usr/bin/env python
# -*-coding:utf-8 -*-
Description: rename pic from 1 to N
Author     : Allen
Created    : 2024-05-23
"""

import shutil
import os


def copy_files_to_current_folder():
    # current_folder = os.getcwd()  # 获取当前文件夹路径
    workdir="/Users/wanglun/Pictures/14岁"
    for root, dirs, files in os.walk(workdir):
        CNT=0
        for file in files:
            # print(file)
            newName=str(CNT+1)
            src_name = workdir+'/'+file  # 源文件名
            dst_name = workdir+'/'+newName+'.jpg'  # 源文件名
            if  "rename.py" not in src_name:
                shutil.move(src_name, dst_name)  # 执行拷贝操作
            
            CNT+=1

    return


if __name__ == "__main__":
    copy_files_to_current_folder()
