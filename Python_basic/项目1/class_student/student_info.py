# -*- coding:utf-8 -*-
import os
class Student:
    # 定义类变量（类属性）
    data = [{'name': '张三', 'age': 20, 'score': 94},
            {'name': '王五', 'age': 25, 'score': 85},
            {'name': '赵六', 'age': 27, 'score': 99},
            {'name': '马三', 'age': 21, 'score': 91},
            {'name': '马超', 'age': 26, 'score': 76},
            {'name': '赵云', 'age': 26, 'score': 89},
            {'name': '周瑜', 'age': 24, 'score': 97},
            {'name': '貂蝉', 'age': 18, 'score': 100},
            {'name': '小巧', 'age': 18, 'score': 99}]
    count = 9

    # 定义固定属性
    __slots__ = ['name', 'age', 'score', 'line']

    # 初始化数据
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
        if 0 <= score <= 100:
            self.line = {}
            self.line['name'] = self.name
            self.line['age'] = self.age
            self.line['score'] = self.score
            self.__class__.data.append(self.line)
            self.__class__.count += 1
            print('初始化数据已生成')
        else:
            print('成绩大于0~100范围')

        # __dict__ 获取数据字典
        # self.__class__.data.append(self.__dict__)

    # 定义类方法
    # 查询类
    @classmethod
    def get_data(cls, datas=data):
        if cls.count != 0:
            print('---------------')
            print('姓名', '年龄', '成绩')
            print('---------------')
            for i in datas:
                print(i.get('name') + ' ' * 2 +
                      str(i.get('age')) + ' ' * 2 +
                      str(i.get('score'))
                      )
            print('---------------')
            print('用户个数:%d' % cls.count)
        else:
            print('暂无学生信息')

    # 修改类
    @classmethod
    def set_data(cls, user, value):
        if 0 <= int(value) <= 100:
            for i in cls.data:
                if i['name'] == user:
                    i['score'] = value
                    print(user, '【修改成功】')
                    break
        else:
            print('超出范围')



    # 个人用户查询验证
    def user_query_student(self, user):
        for i in self.data:
            if i['name'] == user:
                print(user, '【验证成功】')
                return True
        else:
            print('无用户信息')
            return False

    # 管理员用户查询
    def admin_query_student(self, data='defalut'):
        print('---------------')
        print('姓名', '年龄', '成绩')
        print('---------------')
        if data == 'defalut':
            data = self.data
        for i in data:
            print(i.get('name') + ' ' * 2 +
                  str(i.get('age')) + ' ' * 2 +
                  str(i.get('score'))
                  )
        print('---------------')
        print('用户个数:%d' % self.count)

    # 用户删除
    def user_delete_student(self, user):
        for i in self.data:
            if i['name'] == user:
                self.data.pop(self.data.index(i))
                self.__class__.count -= 1
                print(user, '【删除成功】')
                break

    # 成绩修改
    def user_updata_score_student(self, user, score):
        if 0 <= int(score) <= 100:
            for i in self.data:
                if i['name'] == user:
                    i['score'] = score
                    print(user, '【修改成功】')
                    break
        else:
            print('超出范围')
    # 成绩排序
    # 默认降序，当order=False 升序
    def desc_score_student(self, order=True):
        self.admin_query_student(sorted(self.data, key=lambda d: d['score'], reverse=order))

    # 年龄排序
    # 默认降序，当order=False 升序
    def desc_age_student(self, order=True):
        self.admin_query_student(sorted(self.data, key=lambda d: d['age'], reverse=order))

    # 存储数据
    def save_student(self, file='data/data_student.txt'):
        self.file = file
        try:
            # 打开文件
            data_read = open(file, 'wb')
            for i in self.data:
                n = i.get('name')
                a = i.get('age')
                s = i.get('score')

                # 拼接格式
                par = n + ' ' + str(a) + ' ' + str(s) + '\n'
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
    def read_student(self):
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
                n, a, s = t2
                print('姓名:%s 年龄:%d 成绩:%d' % (n, int(a), int(s)))

            # 关闭文件
            file.close()

        except OSError:
            print('打开文件失败')
        except AttributeError:
            print('打开文件失败或不存在')

# 初始化数据
# s1 = Student('张三', 20)
# s2 = Student('李四', 23)
# s3 = Student('王五', 10)
# admin = Student('admin', 0)

# 修改成绩
# s1.user_updata_score_student(s1, 78)
# s2.user_updata_score_student(s2, 98)
# s3.user_updata_score_student(s3, 100)

# 查询信息
# s1.user_query_student(s1)
# s1.user_query_student(s2)
# s1.user_query_student(s3)

# 删除信息
# admin.user_delete_student(s1)

# 查询所有
# admin.admin_query_student()

# 成绩降序
# admin.desc_score_student()

# 成绩升序
# admin.desc_score_student(order=False)

# 年龄降序
# admin.desc_age_student()

# 年龄升序
# admin.desc_age_student(order=False)

# 存储数据
# admin.save_student()

# 读取数据
# admin.read_student()




