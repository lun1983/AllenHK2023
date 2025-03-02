'''
# !/usr/bin/env python
# -*-coding:utf-8 -*-
Description: Query Sqlite
Author     : Allen
Created    : 2024-09-07
'''

import sqlite3
# 连接到 SQLite 数据库
conn = sqlite3.connect('demoX')  # 假设数据库文件名为 demo.db
cursor = conn.cursor()

# 查询 FETABC 表的数据
cursor.execute("SELECT * FROM FETFEIN")
rows = cursor.fetchall()

# 打印查询结果
for row in rows:
    print(row)

# 关闭游标和连接
cursor.close()
conn.close()