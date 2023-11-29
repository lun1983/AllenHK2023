# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test.py.py
# Time       ：8/11/2023 22:08
# Author     ：Allen Wong
# version    ：python 3.11
# Conda Env  : CBIC v23.9.0
# Description：
"""


def func(i):
    return i * 2

def main():
    print('******test.py start*****')
    a,b=1,2
    l1 = [func(i) for i in range(10)]
    l2 = [list('abc')]

    print(l1)
    print(l2)
    print('******test.py end*****')


if __name__ == "__main__":
    main()
