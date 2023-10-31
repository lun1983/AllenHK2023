# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : genBarDocs.py
# Time       ：29/10/2023 21:27
# Author     ：Allen Wong
# version    ：python 3.11
# Conda Env  : CBIC v23.9.0
# Description：
"""

import PySimpleGUI as sg
import qrcode
import os
from create_doc import create_doc_with_bar
from barcode import Code128
import barcode.writer
import cairosvg
import shutil
import re


def create_txt_selection_gui() -> str:
    """Create a PySimpleGUI window for user to select file to import."""
    file_path = ""
    layout = [[sg.Text('Select .txt file')],
              [sg.InputText(disabled=True, do_not_clear=True),
               sg.FileBrowse()],
              [sg.Text('Expiring Date（DD/MM/YYYY）')],
              [sg.InputText()],
              [sg.Submit()]]

    window = sg.Window('Input your text', layout)

    while True:
        event, values = window.read()

        match event:
            case sg.WIN_CLOSED:
                break
            case 'Submit':
                file_path = values[0]  # Extract file path in string
                bar_valid_date = values[1]

                #  判断选择的文件格式
                pattern = r"^(0[1-9]|1[0-9]|2[0-9]|3[0-1])/(0[1-9]|1[0-2])/([0-9]{4})$"
                if not file_path.endswith('.txt'):
                    sg.popup('Please select file with .txt extension!')
                # 判断录入的日期
                elif not re.match(pattern, bar_valid_date):
                    sg.popup('Expiring Date must be: DD/MM/YYYY format!')
                else:
                    break

    window.close()

    return file_path, bar_valid_date


def main():
    print('****** genBarDocs start *****')
    file_path, bar_valid_date = create_txt_selection_gui()

    # # FOR TEST
    # file_path = './testing_code.txt'
    # bar_valid_date = '31/12/2025'

    bar_folder_path = './OUT_BAR'
    doc_folder_path = './OUT_DOCX'
    pdf_folder_path = './OUT_PDF'

    if not file_path:
        print("no file selected.")
        exit()

    with open(file_path) as f:
        lines = f.readlines()

        if os.path.exists(bar_folder_path):
            shutil.rmtree(bar_folder_path)
        if os.path.exists(doc_folder_path):
            shutil.rmtree(doc_folder_path)
        if os.path.exists(pdf_folder_path):
            shutil.rmtree(pdf_folder_path)

        os.makedirs(bar_folder_path)
        os.makedirs(doc_folder_path)
        os.makedirs(pdf_folder_path)

        svgCNT = 0
        for line in lines:
            # Check if empty line
            if line == "\n":
                continue
            line = line.replace('\n', '')

            # 产生SVG文件
            svgFile_list = [svgfile for svgfile in os.listdir(bar_folder_path) if svgfile.endswith('.svg')]
            outitem = f'{bar_folder_path}/barcode_{len(svgFile_list) + 1}'
            img = barcode.generate('code128',
                                   line,
                                   output=outitem)
            # 将SVG转换成PNG
            inputSVG = f'{bar_folder_path}/barcode_{len(svgFile_list) + 1}.svg'
            img_file_path = f'{bar_folder_path}/barcode_{len(svgFile_list) + 1}.png'
            # word looks fine but pdf not
            cairosvg.svg2png(url=inputSVG, write_to=img_file_path, dpi=800, scale=1,output_width=450,output_height=300,background_color='white')
            # 将PNG插入word模板
            create_doc_with_bar(bar_path=img_file_path,
                                save_path=f"{doc_folder_path}/barcode_{(len(os.listdir(doc_folder_path)) + 1)}.docx",
                                pdf_path=f"{pdf_folder_path}/barcode_{(len(os.listdir(pdf_folder_path)) + 1)}.pdf",
                                bar_valid_date=bar_valid_date)

        print(f"BAR codes created: {len(os.listdir(doc_folder_path))}")
    print('****** genBarDocs end *****')


if __name__ == "__main__":
    main()
