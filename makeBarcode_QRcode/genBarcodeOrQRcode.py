# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : genBarcodeOrQRcode.py
# Time       ：23/9/2023 09:46
# Author     ：Allen Wong
# version    ：python 3.10
# Description：
"""
import barcode.writer

from barcode import Code128
from barcode.writer import ImageWriter
import qrcode
import os
import re

inputFile = './input.txt'


def genBarcode(inputFileToList):
    for stritem in inputFileToList:
        stritem_filename = re.sub(r'[^a-zA-Z0-9]', '', stritem)
        outitem = 'BARCODE_' + stritem_filename

        barcode.generate('code128',
                         stritem,
                         # writer=ImageWriter,
                         output=outitem)

    return


def genQRcode(inputFileToList):
    for stritem in inputFileToList:
        stritem_filename = re.sub(r'[^a-zA-Z0-9]', '', stritem)
        outitem = 'QRCODE_' + stritem_filename
        img = qrcode.make(stritem)
        img.save(f"{outitem}.png")

    return


def readfile(inputFile):
    inputFileToList = []
    file = open(inputFile, 'r')
    inputFileToList = file.readlines()
    inputFileToList = [item.strip() for item in inputFileToList]
    # print(inputFileToList)
    file.close()

    return inputFileToList


def main():
    while True:
        if not os.path.exists(inputFile):
            print('\'input.txt\' not found in current DIR,please check!')
            input('Press any key to continue...')
            exit(1)
        print('Start \n Please input your choice: \n 1: Generate BARcode \n 2: Generate QRcode ')
        choice = input()
        if choice == '1':
            print('1')
            inputFileToList = readfile(inputFile)
            genBarcode(inputFileToList)
            break
        elif choice == '2':
            print('2')
            inputFileToList = readfile(inputFile)
            genQRcode(inputFileToList)
            break
        else:
            print('Invalid choice,plsease rechoose')
    print('End')

    return


if __name__ == "__main__":
    main()
