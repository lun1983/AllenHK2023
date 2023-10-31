# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : svg_to_png.py
# Time       ：29/10/2023 11:48
# Author     ：Allen Wong
# version    ：python 3.10
# Description：
"""

import cairosvg



def main():
    print('svg_to_png start')
    inputfile = './barcode_1.svg'
    outputfile = './barcode_1.png'
    # cairosvg.svg2png(url=inputfile, write_to=outputfile, scale=2.0)
    cairosvg.svg2png(url=inputfile, write_to=outputfile, dpi=200)

if __name__ == "__main__":
        main()
