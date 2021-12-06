from class_student.config_Human import Human
# -*- coding:utf-8 -*-
import os
class Student:
    # __L = [{'name': '张三', 'age': 20, 'score': 94, 'state': True},
    #         {'name': '王五', 'age': 25, 'score': 85, 'state': True},
    #         {'name': '赵六', 'age': 27, 'score': 99, 'state': True},
    #         {'name': '马三', 'age': 21, 'score': 91, 'state': True},
    #         {'name': '马超', 'age': 26, 'score': 76, 'state': True},
    #         {'name': '赵云', 'age': 26, 'score': 89, 'state': True},
    #         {'name': '周瑜', 'age': 24, 'score': 97, 'state': True},
    #         {'name': '貂蝉', 'age': 18, 'score': 100, 'state': True},
    #         {'name': '小巧', 'age': 18, 'score': 99, 'state': True}]
    __L = []
    __count = 0
    def __repr__(self):
        return 'Student(%r)' % self.__L

    # 初始化用户
    def create_user(self):
        user = input('请输入姓名:')
        if not user:
            return -1
        it = self.iteration_data(user)
        if it:
            return print('该用户已存在')
        age = int(input('请输入年龄:'))
        score = int(input('请输入成绩:'))
        try:
            u = Human(user, age, score)
            self.__class__.__L.append(u.get_Human())
            self.__class__.__count += 1
        except ValueError as err:
            print(err)

    # 遍历访问
    def iteration_data(self, user):
        for i in self.__class__.__L:
            if i['name'] == user and i['state'] == True:
                line = self.__class__.__L.index(i)
                return self.__class__.__L[line]
        else:
            return False

    # 查询用户
    def select_user(self, data=__L):
        if not data:
            print('无学生数据')
            return -1
        for i in data:
            if i['state'] == True:
                print(i)
        print('总人数:%d' % self.__count)

    # 修改成绩
    def update_user_score(self):
        user = input('请输入修改学生姓名:')
        it = self.iteration_data(user)
        if it:
            score = int(input('请输入修改成绩:'))
            if 0 <= score <= 100:
                it['score'] = score
                print('%s成绩修改成功' % user)
                return -1
            else:
                return print('成绩超出范围')
        else:
            print('无该学生信息')

    # 删除用户
    def delete_user(self):
        user = input('请输入删除学生姓名:')
        it = self.iteration_data(user)
        if it:
            it['state'] = False
            self.__class__.__count -= 1
            print('%s用户删除成功' % user)
            return -1
        else:
            print('无该学生信息')

    # 成绩排序
    # 默认降序，当order=False 升序
    def desc_score(self, order=True):
        self.select_user(sorted(self.__L, key=lambda d: d['score'], reverse=order))

    # 年龄排序
    # 默认降序，当order=False 升序
    def desc_age(self, order=True):
        self.select_user(sorted(self.__L, key=lambda d: d['age'], reverse=order))

    # 存储数据
    def save_user(self, file='data/data_student.txt'):
        self.file = file
        try:
            # 打开文件
            data_read = open(file, 'wb')
            for i in self.__L:
                n = i.get('name')
                a = i.get('age')
                s = i.get('score')
                t = i.get('state')

                # 拼接格式
                par = n + ' ' + str(a) + ' ' + str(s) + ' ' + str(t) + '\n'
                # 转义字节串
                byte = par.encode('utf-8')
                # 写入文件
                data_read.write(byte)
            # 关闭文件
            data_read.close()
            # 返回存储文件绝对路径
            print("文件存放至:", os.path.abspath(file))
        except OSError:
            print('打开文件失败')

    # 读取数据
    def read_user(self):
        try:
            # 打开文件
            file = open(self.file, 'rb')

            while True:
                # 读取数据
                data = file.readline()
                if not data:
                    break
                # 二进制解码
                t = data.decode('utf-8')
                # 去掉左右空格
                t1 = t.strip()
                # 分割形成列表
                t2 = t1.split()
                # 序列赋值
                n, a, s, t = t2
                print('姓名:%s 年龄:%d 成绩:%d 状态:%s' % (n, int(a), int(s), t))

            # 关闭文件
            file.close()

        except OSError:
            print('打开文件失败')
        except AttributeError:
            print('打开文件失败或不存在')












