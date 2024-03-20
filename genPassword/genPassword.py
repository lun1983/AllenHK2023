# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : genPassword.py
# Time       ：20/11/2023 11:07
# Author     ：CBIC-IT-TEAM
# version    ：python 3.11
# Conda Env  : base v23.9.0
# Description：
"""

import random
import string

RESULTFILE = './PASSWORD.TXT'


def main():
    print('****** genPassword start *****')


    characters = string.ascii_letters  + string.digits
    pswd = ''.join(random.choice(characters) for _ in range(8))
    print('pswd1: ' + pswd)

    index = random.randint(1, len(pswd) - 1)
    mydigits = ['@', '_', '#']

    pswd = pswd[:index]+random.choice(mydigits)+pswd[index:]

    print('pswd: ' + pswd)
    with open(RESULTFILE, 'w') as file:
        file.writelines(pswd)
    return

    print('****** genPassword end *****')


if __name__ == "__main__":
    main()
