# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test.py.py
# Time       ：23/9/2023 17:30
# Author     ：Allen Wong
# version    ：python 3.10
# Description：
"""

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
#1.svglib方法
pic = svg2rlg('BARCODE_0010900010000814.svg')
renderPM.drawToFile(pic,'BARCODE_0010900010000814.png')