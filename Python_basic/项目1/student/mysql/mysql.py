from pymysql import *
import mysql.mysql_config as mydb
class Mysql_Python:
    '''
    pymysql数据库连接
    '''
    def __open(self):
        '''
        mydb.c_host : 主机名
        mydb.c_port : 端口号
        mydb.c_user : 用户名
        mydb.c_password : 密码
        mydb.c_database : 库名
        mydb.c_charset : 字符集
        :return:
        '''
        # pymysql.connect传参
        self.__db = connect(host=mydb.c_host,
                     port=mydb.c_port,
                     user=mydb.c_user,
                     password=mydb.c_password,
                     database=mydb.c_database,
                     charset=mydb.c_charset)
        self.__cur = self.__db.cursor()

    def __close(self):
        self.__cur.close()
        self.__db.close()

    def idu(self, sql, L=[]):
        try:
            self.__open()
            self.__cur.execute(sql, L)
            self.__db.commit()
            print('OK')
        except Exception as err:
            self.__db.rollback()
            print('错误，已回滚:', err)
        self.__close()

    def sall(self, sql, L=[]):
        try:
            self.__open()
            self.__cur.execute(sql, L)
            self.__result = self.__cur.fetchall()
            return self.__result
        except Exception as err:
            print('错误:', err)
        self.__close()





