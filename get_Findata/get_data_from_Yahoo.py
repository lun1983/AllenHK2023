# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test.py
# Time       ：23/9/2023 23:58
# Author     ：Allen Wong
# version    ：python 3.10
# Description：
"""
import yfinance as yf


def main():
    print('program start')
    mystock = yf.Ticker("AAPL")
    # apple.info
    print(mystock.balance_sheet)


if __name__ == "__main__":
    main()
