from mysql.mysql import Mysql_Python as mydb
from hashlib import sha1
class Login:
    '''
    register : 注册模块
    sign_in : 登录模块
    '''
    # 调取数据库对象
    m = mydb()

    # 注册
    def register(self, name, password, id, Tel, Email):
        '''
        :param name: 用户
        :param password: 密码
        :param id: 身份证号
        :param Tel: 电话
        :param Email: 邮箱
        :return:
        '''
        self.name = name
        self.password = password
        self.id = id
        self.Tel = Tel
        self.Email = Email

        # sha1加密方式
        self.encode_passwd = sha1()
        # 指定加密编码
        self.encode_passwd.update(self.password.encode('utf8'))
        # 十六进制加密返回结果
        self.en_password = self.encode_passwd.hexdigest()

        # 数据入库
        self.__class__.m.idu('insert into user values(%s, %s, %s, %s, %s)', L=[self.name,
                                                                   self.en_password,
                                                                   self.id,
                                                                   self.Tel,
                                                                   self.Email])
    # 登录
    def sign_in(self, name, password):
        '''
        :param name: 用户名
        :param password: 密码
        :return:
        '''

        # sha1加密方式
        self.encode_passwd = sha1()
        # 指定加密编码
        self.encode_passwd.update(password.encode('utf8'))
        # 十六进制加密返回结果
        self.en_password = self.encode_passwd.hexdigest()

        # 查询用户是否存在
        self.sql_select = "select password from user where name=%s"
        result = self.__class__.m.sall(self.sql_select, L=[name])

        if len(result) is not 0:
            if self.en_password in result[0]:
                print('登录成功')
                return True
            else:
                print('密码错误')
                return False
        else:
            print('用户不存在')
            return False




















