# 此示例示意用私有属性和私有方法来进行封装
# class A:
#     def __init__(self):
#         self.__p1 = 100     # 创建私有属性，此属性在类外无法访问
#
#     def __m1(self):     # 私有方法
#         print('__m1被被调用')
#
#     def infos(self):
#         print('A类的infos获取到的__p1属性值是:', self.__p1)
#         self.__m1() #调用自己的私有方法
#
#
# a = A()
# a.infos()
# # a.__m1()        # 当前主模块不能调用A类的私有方法



# 练习
class Student:
    def __init__(self, n, a, s):
        self.__name = n
        self.__sage = a
        self.__score = s

    def set_age(self, a):
        if a < 0:
            raise ValueError(a, '< 0')
        elif a > 140:
            raise ValueError(a, '> 140')
        self.__sage = a
        print('修改成功')

    def infos(self):
        print(self.__name, self.__sage, self.__score)

s1 = Student('张三', 20, 94)
# s1.infos()
# s1.set_age(23)
# s1.infos()
print(s1._Student__sage)








