# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 23:30:25 2021

@author: tramk
"""

## Python code to connect to Oracle database using python lib

import cx_Oracle
dsn = cx_Oracle.makedsn(
    'localhost', 
    '1521', 
    service_name='XE'
)
conn = cx_Oracle.connect(
    user='system', 
    password='oracle', 
    dsn=dsn
)
c = conn.cursor()
c.execute('SELECT * FROM emp WHERE ROWNUM <= 10')
for row in c: print(row)
conn.close()
