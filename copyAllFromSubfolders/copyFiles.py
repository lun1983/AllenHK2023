# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : genBarcodeOrQRcode.py
# Time       ：23/9/2023 09:46
# Author     ：Allen Wong
# version    ：python 3.10
# Description：
"""

import os
import glob
import PySimpleGUI as sg  # 图形选择窗口
import shutil


def create_pdf_select_gui():
    return


# 产生一个图形窗口，供用户选择要添加的PDF文件
def create_pdf_select_gui() -> str:
    file_path = ''

    # define layout
    layout = [
        [sg.Text('Select the PDF file to add QR:')],
        [sg.InputText(disabled=True, do_not_clear=False), sg.FolderBrowse()],
        [sg.Submit()]
    ]

    window = sg.Window('Copy files from foler&subfolder', layout)
    # 获取事件

    event, values = window.read()

    match event:
        case sg.WINDOW_CLOSED:
            exit()
        case "Submit":
            folerpath = values['Browse']
            print('Source folder:' + str(folerpath))

    window.close()

    return folerpath


def main():
    print('Program start')
    # UI界面确定选择PDF文件
    headpath = create_pdf_select_gui()

    filepaths = glob.glob(headpath + '/**/*', recursive=True)

    for filepath in filepaths:
        print('***Copying:'+filepath)
        if not os.path.isdir(filepath):
            shutil.copy2(filepath,'./')

    return


if __name__ == "__main__":
    main()
