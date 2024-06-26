"""
# !/usr/bin/env python
# -*-coding:utf-8 -*-
Description: Query Mysql
Author     : Allen                       
Created    : 2024-06-26
"""

import time
import mysql.connector


def Qmysql(sql):

    print(f"SQL: {sql}")

    # create connection
    # db = mysql.connector.Connect(host="localhost", user="root", password="Infy_2011")
    db = mysql.connector.Connect(host="localhost", user="myuser", password="123@Abcab")
    # create cursor
    cursor = db.cursor()
    # run sql
    cursor.execute(sql)
    # get results
    results = cursor.fetchall()

    return results


if __name__ == "__main__":
    sql = """
        select * from demo.user;
    """
    results = Qmysql(sql)
    for i in results:
        print(i)
