from pymysql import *
import student.mysql.mysql_config as mydb
db = connect(host=mydb.c_host,
             port=mydb.c_port,
             user=mydb.c_user,
             password=mydb.c_password,
             database=mydb.c_database,
             charset=mydb.c_charset)

cur = db.cursor()
sql = "select * from sheng;"
cur.execute(sql)
result = cur.fetchall()
print(result)
cur.close()
db.close()






