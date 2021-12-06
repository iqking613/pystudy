# -*- coding: utf-8 -*-
import time
# 此示例示意定义一个Dog类,并让Dog创建的对象有相同的行为
# 并可以用help(Dog)查询类的文档字符串
# 吃， 睡， 玩

# class Dog():
#     '''这个类用来描述一种小动物的行为和属性'''
#     def eat(self, food):
#         '''描述小狗正在吃饭的行为'''
#         print("小狗正在吃%s" % food)
#
#     def sleep(self, hour):
#         print('小狗睡了%d小时' % hour)
#
#     def play(self, obj):
#         print("小狗正在玩%s" % obj)
# Dog1 = Dog()    # 创建一个新的Dog类的对象
# Dog1.eat('骨头')
# Dog1.sleep(1)
# Dog1.play('足球')
# print(id(Dog1))     # 打印这个对象的ID

# 此示例示意为每个对象添加示例属性，并提供对象的方法访问
# class Dog():
#     def infos(self):
#         print(self.color, '的', self.kinds)
#
#     def eat(self, food):
#         print(self.color, '的', self.kinds, '正在吃', food)
#
#         # 绑定food属性
#         self.food = food    # 当Dog类型对象吃东西时，用food属性记住此对象吃的是什么
#
#     def food_info(self):
#         print(self.color, '的', self.kinds, "上一次吃的", self.food)
# dog1 = Dog()
# dog1.kinds = '京巴'   # 为dog1绑定的Dog对象添加kinds属性
# dog1.color = '白色'   # 创建color实例变量
# dog1.color = '黄色'   # 改变实例变量的color的绑定关系
#
# dog1.infos()
# dog1.eat('骨头')
# dog1.food_info()
# print(dog1.color, '的', dog1.kinds)  # 获取属性数据

# 此示例示意对象初始化方法使用
# class Car:
#     def __init__(self, clr, brand, model):
#         self.color = clr
#         self.brand = brand
#         self.model = model
#         # print('Car的初始化方法被调用')
#
#     def run(self, speed):
#         print(self.color, '的', self.brand, self.model, '正在以', speed, '公里/小时的速度行驶')

# c1 = Car('红色', '奥迪', 'A6')
# c1.run(200)

# 此示例示意对象析构方法使用
# class Car():
#     def __init__(self, name):
#         self.name = name
#         print('汽车', name, '对象被调用')
#
#     def __del__(self):
#         print('汽车', self.name, '对象被销毁')

# c1 = Car('BYD E6')
# L = []
# L.append(c1)
# del c1
# time.sleep(5)
# del L
# while True:
#     pass
# print("程序结束")

# 此示例示意类变量的用法，及类和对象的关系
# class Human:
#     total_count = 0     # 类变量，此变量用来记录所有对象的个数
#     def __init__(self, n):
#         self.name = n
#         # 每创建 Human total_count加1
#         # 做记录当前对象的个数
#         self.__class__.total_count += 1
#     def Dog(self):
#         pass
#
#     def __del__(self):
#         # 当销毁时，自动将类变量做减1操作
#         self.__class__.total_count -= 1
# s1 = Human('小张')
# s2 = Human('小张')
# print("Human, total_count = ", Human.total_count)

# 类变量可以通过类直接访问
# Human.total_count += 1
# print("Human, total_count = ", Human.total_count)

# 类变量可以通过类的实例直接访问
# h1 = Human('小张')
# print("Human, total_count = ", h1.total_count)
# h1.total_count = 100    # 此实例是为实例添加一个变量，并不是修改类变量
# print("Human, total_count = ", Human.total_count)   # 1

# 类变量可以通过此类的对象的__class__属性间接访问
# h1.__class__.total_count = 200
# print("Human, total_count = ", Human.total_count)   # 200


# 此示例示意__slots__属性的用法和说明
# class Student:
#     # 此列表让Student创建的对象只能用name和age属性
#     # 不能有其他属性
#     __slots__ = ['name', 'age']
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# s1 = Student('Tarena', 15)
# print(s1.__dict__)
# print(s1.age)
# s1.Age = 16   #报错，不允许添加__slots__列表以外的属性 异常 AttributeError
# print(s1.age)

# 此示例示意用类方法的使用
# class A:
#     v = 0   #<<<---类变量
#
#     def __init__(self):
#         self.my_v = 10000
#
#     @classmethod
#     def get_v(cls):
#         '''此方法为类方法，cls用于绑定调用此方法的类
#         此方法用于返回类变量的值
#         '''
#         return cls.v
#         # return cls.my_v   报错，类方法无法访问类对象定义的属性
#
#     @classmethod
#     def set_v(cls, value):
#         cls.v = value


# print(A.get_v())    # 0
# A.set_v(100)        # 直接调用类方法
# print(A.get_v())    # 200   返回类方法值
#
# a = A()
# print(a.get_v())    # 0
# a.set_v(200)        # 间接通过类对象调用类方法
# print(a.get_v())    # 200
#
# print(a.my_v)       # 10000
# print(a.get_v())    # 200   无法用类方法访问调用此对象的a的my_v实例变量


# 此示例示意静态方法的使用
# class A:
#     @staticmethod
#     def myadd(x, y):
#         return x + y

# print(A.myadd(100, 200))    # 300
# a = A()
# print(a.myadd(300, 400))    # 700

# 此示例示意单继承的语句及定义方法:
# class Human:
#     '''此类用于描述人类的共性行为'''
#     def say(self, what):
#         print('说', what)
#
#     def walk(self, distance):
#         print('走了', distance, '公里')

# 当前Student类，继承自Human类
# class Student(Human):
#     def study(self, subject):
#         print('学习', subject)

# 当前Teacher类，继承自Human类
# class Teacher(Human):
#     def tech(self, course):
#         print('教', course)
# h1 = Human()
# h1.say('今天天气真好')
# h1.walk(5)
#
# print('-------------------------')
# h2 = Student()
# h2.walk(10)
# h2.say('走得有点累')
# h2.study('python')
#
# print('-------------------------')
# t1 = Teacher()
# t1.say('今天晚上吃什么')
# t1.walk(3)
# t1.tech('继承/派生')

# 此示例示意用super构造函数来间接调用父类的覆盖版本的方法
class A:
    def work(self):
        print('A.work被调用')

class B(A):
    def work(self):
        print('B.work被调用')

    def super_work(self):
        '''此方法先调用一下 子类的work，
        在调用一下父类的work'''
        self.work()     # 调用自己的work
        super(B, self).work()   # 调用父类的work
        # 匿名调用父类覆盖方法
        super().work()  # 调用父类的work

# 此示例示意调用基类的构造方法
class Human:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def infos(self):
        print('姓名:', self.name)
        print('年龄:', self.age)

class Student(Human):
    __slots__ = ['socre']
    def __init__(self, n, a, s):
        # 父类和子类 操作的属性各自独立，  以降低各类之间的耦合性
        super().__init__(n, a)      # 显式调用父类的初始化方法
        # self.name = n
        # self.age = a
        self.score = s

    def info_score(self):
        # 父类覆盖版本
        super().infos()
        print('成绩:', self.score)

h1 = Human('小张', 18)
h1.infos()
s1 = Student('小薇', 23, 98)
s1.info_score()

# b = B()
# b.work()    # B.work()
# super(B, b).work()  # A.work()
# b.super_work()  # A.work()

# 此示例示意类函数issubclass
# class A:
#     pass
# class B(A):
#     pass
# class C(B):
#     pass
#
# print(issubclass(C, B))     # True
# print(issubclass(B, C))     # False
# print(issubclass(bool, (C, B, A, int)))     # True



# 练习
# 1.定义一个描述人的信息类:Human
# class Human():
#     def set_info(self, name, age, address='未知'):
#         '''此方法为 '人'，
#         添加:
#             姓名属性
#             年龄属性
#             家庭住址属性
#         '''
#         self.name = name
#         self.age = age
#         self.address = address
#     def show_info(self):
#         '''此处显示此人的信息'''
#         print('姓名:%s 年龄:%d 住址:%s' % (self.name, self.age, self.address))
#         print(self.__dict__)

# h1 = Human()
# h1.set_info('小张', 19, '北京市')
# h1.show_info()
#
# h2 = Human()
# h2.set_info('小丽', 20)
# h2.show_info()

# 2.写一个学生类，用来描述学生信息
# 要求:
#     1)为该类添加初始化方法，实现在创建对象时自动设置'姓名','年龄','成绩'属性
#     2)添加set_core方法能为对象修改成绩信息，并限制成绩在0~100之间
#     3)添加show_info方法打印学生对象的信息
# class Student:
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score
#
#     def set_score(self, score):
#         if 0 <= score <= 100:
#             self.score = score
#         else:
#             # 通知调用者，调用实参不合法
#             raise ValueError('值不在相应的范围内')
#
#     def show_info(self):
#         print('姓名:%s 年龄:%d 成绩:%d' % (self.name, self.age, self.score))
#
#     def get_score(self):
#         return self.score

# try:
#     s1 = Student('小张', 20, 60)
#     s1.show_info()
#     s1.set_score(90)
#     s1.show_info()
#     print('s1绑定的成绩是:', s1.get_score())
# except ValueError as error:
#     print(error)

# 3. 有两个人 Human:
#     1. 姓名: 张三
#        年龄: 35岁
#     2. 姓名: 李四
#        年龄: 10岁
#     行为:
#         1.教别人学东西 teach
#         2.工作赚钱 work
#         3.借钱 borrow
#     用程序描述如下事情:
#         张三  教   李四  学   python
#         李四  教   张三  学   滑冰
#         张三  上班  赚了  1000元钱
#         李四  向   张三  借了  200元钱
#
#         显示李四的全部信息
#         显示张三的全部信息
# class Human():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.Skill = []
#         self.money = 0
#
#     def teach(self, other, ski):
#         other.Skill.append(ski)
#         print(self.name, '教', other.name, '学', ski)
#
#     def work(self, money):
#         self.money += money
#         print(self.name, '上班赚了', money)
#
#     def borrow(self, other, money):
#         if other.money >= money:
#             self.money += money
#             other.money -= money
#             print(self.name, '向', other.name, '借了', money)
#         print(other.name, "没借给", self.name)
#         return False
#
#     def show_Human(self):
#         print('姓名:%s 年龄:%d 技能:%s money:%d' % (self.name, self.age, self.Skill, self.money))

# zhangsan = Human('张三', 35)
# lisi = Human('李四', 10)
#
# zhangsan.teach(lisi, 'python')
# lisi.teach(zhangsan, '滑冰')
# zhangsan.work(1000)
# lisi.borrow(zhangsan, 200)

# zhangsan.show_Human()
# lisi.show_Human()

# 4.用类来描述一个学生的信息（可以修改之前写的Student类）
# class Student:
#     ...此处自己实现
#
#     学生信息有：
#         姓名,年龄,成绩
#
#     将这些学生对象存于列表中，可以任意添加和删除学生信息
#         1)打印学生的个数
#         2)打印出所有学生的平均成绩
#         3)打印出所有学生的平均年龄
#         (建议用类变量存储学生信息)
# class Student:
#     L = []
#     count = 0
#     __slots__ = ['name', 'age', 'score']
#
#     def __init__(self, name, age, score):
#         self.name = name
#         if not name:
#             return
#         self.age = age
#         self.score = score
#         line = {}
#         line['name'] = name
#         line['age'] = age
#         line['score'] = score
#         self.__class__.L.append(line)
#         self.__class__.count += 1
#
#     # 类方法
#     @classmethod
#     def get_data(cls):
#         return cls.L
#
#     @classmethod
#     def aver(cls, t='score'):
#         Sum = 0
#         for i in cls.L:
#             Sum += i[t]
#         return Sum / cls.count
#
# L1 = Student('zhangsan', 20, 74)
# L2 = Student('lisi', 23, 68)
# L3 = Student('wangwu', 23, 96)
# print(Student.get_data())
# print(Student.aver('age'))
# while True:
#     Choice = int(input("请选择:"))
#     if Choice == 1:
#         while True:
#             n = input('请输入姓名:')
#             if not n:
#                 break
#             a = input('请输入年龄:')
#             s = input('请输入成绩:')
#             li = Student(n, a, s)
#     elif Choice == 2:
#         Student.get_data()
#     elif Choice == 3:
#         co = Student.aver(Student.get_data())
#         print('平均成绩是', co)
#     elif Choice == 0:
#         break

