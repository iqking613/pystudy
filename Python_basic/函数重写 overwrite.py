# 此示例示意repr函数和str函数的不同
s = "I' m Teacher"

# print(str(s))   # I' m Teacher      人阅读
#
# print(repr(s))  # "I' m Teacher"    机器阅读


# 此示例示意repr(obj)和str(obj)的函数重写
class MyNumber:
    def __init__(self, value):
        self.data = value

    def __str__(self):
        print('正在调用__str__方法，转换为普通字符串')
        return '自定义:%d' % self.data

    def __repr__(self):
        return 'MyNumber(%d)' % self.data

n1 = MyNumber(100)
# print(str(n1))
# print(repr(n1))
# print(len(repr(n1)))

# 此示例示意 abs 和 len方法的重写方法
class MyInteger:
    def __init__(self, v):
        self.data = v

    def __repr__(self):
        return 'MyInterger(%d)' % self.data

    def __abs__(self):
        '''此方法用于制定abs（obj）函数取值时返回的结果'''
        if self.data < 0:
            # 用-self.data 创建一个新的对象返回 回去
            return MyInteger(-self.data)
        return MyInteger(self.data)

# i1 = MyInteger(-100)
# print(i1)       # 等同于print(str(i1))
# n = abs(i1)     # MyInterger(100)
# print(n)
#
# i2 = MyInteger(200)
# print(i2)
# print(abs(i2))  # MyInterger(200)

# 此示例示意自定义对象转为python内建的数字数值
class MyNumber:
    def __init__(self, v):
        self.data = v

    def __repr__(self):
        return 'MyNumber(%d)' % self.data

    def __int__(self):
        return int(self.data)
# n1 = MyNumber(100.5)
# n = int(n1)     # 自定义类型转为整数，出错
# print(n)

# 此示例示意__bool__方法布尔测试函数重写
# class MyList:
#     def __init__(self, iterable=()):
#         self.data = [x for x in iterable]
#
#     def __repr__(self):
#         return "MyList(%s)" % self.data
#
#     def __len__(self):
#         print('__len__被调用')
#         return len(self.data)
#
#     def __bool__(self):
#         '''此方法用来制定bool(x)返回的规则'''
#         # 如果没有任何元素返回False
#         print('__bool__被调用')
#         if len(self.data) == 0:
#             return False
#         for x in self.data:
#             if x:
#                 return True
#         return False


# myl = MyList([1, -2, 3, 4])
# myl = MyList()
# print(myl)
# print(bool(myl))
# print(len(myl))

# 此示例示意用自定义的类MyRange实现可迭代对象
# 用自定义的类MyRangeIterator实现迭代器
# class MyIterator:
#     def __init__(self, start, stop, step):
#         # self.start 此处用来记录迭代器的起始位置和当前位置
#         self.start = start
#         self.stop = stop
#         self.step = step
#
#     def __next__(self):
#         '''此方法用来实现迭代器协议'''
#         print('MyIterator.__next__被调用')
#         if self.start >= self.stop:
#             raise StopIteration('错误')
#         r = self.start      # 先将要返回的数存于变量r中
#         self.start += self.step     # 迭代器后移
#         return r            # 返回next(it) 调用
#
# class MyRange:
#     def __init__(self, start, stop=None, step=1):
#         if stop is None:
#             stop = start
#             start = 0
#         self.start = start
#         self.stop = stop
#         self.step = step
#
#     def __repr__(self):
#         return "MyRange(%d, %d, %d)" % (self.start, self.stop, self.step)
#
#     def __iter__(self):
#         '''此方法用于把MyRange类型创建的对象当做可迭代对象'''
#         print('MyRange.__iter__被调用')
#         return MyIterator(self.start, self.stop, self.step)  # <<< 此处必须返回迭代器



# L = MyRange(1, 10)
# print(L.__iter__())
# for i in L:
#     print(i)
# L2 = MyIterator(10, 20, 1)


# 练习:
# 写一个类Mylist实现和list内几乎一样的功能
# 在Mylist内用列表存储数据
# class MyList:
#     def __int__(self,iterable=()):
#         self.data = iterable
#
#     def append(self,v):
#         ...用于添加数据
#
# L = MyList("ABCD")
# print(L)        # MyList(['A','B','C','D'])
# L.append('E')
# print(L)        # MyList(['A','B','C','D','E'])
#
# for x in L:
#     print(x)
#
# print("列表L的长度是:", len(L))   # 5

class MyIterator:
    i = 0
    def __init__(self, iterable=()):
        self.data = iterable
        print(iterable)

    def __next__(self):
        if self.i == len(self.data):
            raise StopIteration('错误')
        s = self.data[self.__class__.i]
        self.__class__.i += 1
        return s

class MyList:
    L = []
    i = 0
    def __init__(self, iterable=()):
        self.__class__.L += [x for x in iterable]
        self.data = self.__class__.L

    def __repr__(self):
        return 'MyList(%s)' % self.L

    def __iter__(self):
        return MyIterator(self.L)

    def __len__(self):
        return len(self.__class__.L)

    def append(self, v):
        self.__class__.L += v


L = MyList("ABCD")
print(L)
L.append('E')
print(L)
for i in L:
    print(i, end=' ')

print("长度为:", len(L))

