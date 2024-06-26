"""
# !/usr/bin/env python
# -*-coding:utf-8 -*-
Description: use jieba to cut sentence
Author     : allen
Created    : 2024-05-28
"""

import jieba

if __name__ == "__main__":
    s = "来了八十八个把式要在巴老爷八十八棵芭蕉树下住。"
    print(type(jieba.cut(s)))
    print(list(jieba.cut(s)))
