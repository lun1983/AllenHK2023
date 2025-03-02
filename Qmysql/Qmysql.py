'''
# !/usr/bin/env python
# -*-coding:utf-8 -*-
Description: Query mySQL
Author     : Allen
Created    : 2024-09-07
'''

import mysql.connector
import time

def query():
    db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Infy_2011",
        database="demo"
    )
    
    #cursor
    cursor=db.cursor()
    
    #sql
    sql='''
        SELECT * from user;
    '''
    #excute sql
    cursor.execute(sql)
    #result of sql
    results= cursor.fetchall()
    print(type(results))
    # show results
    for i in results:
        print(i) 

    # close mysql connection
    db.close()

    return

if __name__ == "__main__":
    query()