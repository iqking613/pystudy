#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import MySQLdb
import pymysql
import random
import string
conn = pymysql.connect("127.0.0.1", "root", "260820211iI", "zdemo", charset='utf8' )
sql ='insert into student (stu_id,stu_name) values (%s,%s)'
for time in range(1,110):
        data = [],
        for r in range(1,9001):
                data.append((
                        time * 1000 + r ,
                        ['zhang', 'liu', 'hu','lu','han'][random.randint(0, 4)] + str(r)
                ))
        conn.cursor().executemany(sql, data)
        conn.commit()
        time.sleep(5)
        print("9000 inserted.")
conn.close()