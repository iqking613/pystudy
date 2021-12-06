from mysql.mysql import Mysql_Python as mydb

class Message:
    '''
    info : 我的信息模块
    course : 课程信息
    s_score : 查看成绩
    '''
    # 调取数据库对象
    m = mydb()
    # 我的信息
    def info(self, name):
        sql_select = "select name, id, Tel, Email from user where name=%s;"
        result = self.__class__.m.sall(sql_select, L=[name])
        return result

    # 课程信息
    def course(self, name):
        sql_select = "select kc_name,kc_plan from course where id=(select id from user where name=%s);"
        result = self.__class__.m.sall(sql_select, L=[name])
        return result

    # 查看成绩
    def s_score(self, name):
        sql_select = "select kc_name, kc_score from course where id=(select id from user where name=%s);"
        result = self.__class__.m.sall(sql_select, L=[name])
        return result






