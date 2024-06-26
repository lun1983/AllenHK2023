"""
# !/usr/bin/env python
# -*-coding:utf-8 -*-
Description: Clean File Name ,Leave only A-Za-z and Chinese characters
Author     : Allen
Created    : 2024-05-24
"""

import shutil
import os
import re


def renameFile():
    workdir = "/Users/wanglun/downloads"
    outputdir = workdir + "/output"
    if not os.path.exists(outputdir):
        os.mkdir(outputdir)
    for root, dirs, files in os.walk(
        workdir
    ):  # os.walk功能很好用，返回root、dirs、files

        for file in files:
            if "wav" in file.lower():

                newfile = re.sub(r"[^a-zA-Z\u4e00-\u9fa5\s]", "", file)
                newfile = newfile.replace("wav", ".wav").replace("q群", "")

                src_name = workdir + "/" + file  # 源文件名
                dst_name = outputdir + "/" + newfile  # 目标文件名

                print(file + "===> " + newfile)

                shutil.copy(src_name, dst_name)  # 执行拷贝操作

    return


if __name__ == "__main__":
    renameFile()
