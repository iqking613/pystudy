# 此示例示意自定义的类通过运算符重载实现运算符操作
# class MyNumber:
#     def __init__(self, v):
#         self.data = v
#
#     def __repr__(self):
#         return 'MyNumber(%d)' % self.data
#
#     def __add__(self, rhs):
#         '''实现加法操作，生成一个新的对象并返回给调用者'''
#         return MyNumber(self.data + rhs.data)
#
#     def __sub__(self, rhs):
#         return MyNumber(self.data - rhs.data)
#
# n1 = MyNumber(100)
# n2 = MyNumber(200)
# n3 = n1 + n2    # 等同于n1.__add__(n2)
# n3 = n1.__add__(n2)
# print(n3)
#
# n4 = n2 - n1
# print(n4)
#
# n5 = n2 + MyNumber(100)
# print(n5)

# 此示例示意复合赋值算术运算符的重载，对函数全局变量的影响
# class MyList:
#     def __init__(self, iterable=()):
#         self.data = [x for x in iterable]
#
#     def __repr__(self):
#         return 'MyList(%r)' % self.data
#
#     def __add__(self, rhs):
#         return MyList(self.data + rhs.data)
#
#     # 赋值重载
#     def __iadd__(self, rhs):
#         return self.data.extend(rhs.data)

# L = MyList([1, 2, 3])
# def f(lst):
#     lst += MyList([4, 5, 6])
# f(L)
# print(L)

# 此示例示意比较运算符的重载
# class MyList:
#     def __init__(self, iterable=()):
#         self.data = [x for x in iterable]
#
#     def __repr__(self):
#         return 'MyList(%r)' % self.data
#
#     def __gt__(self, rhs):
#         '''只比较第一个元素'''
#         if self.data[0] > rhs.data[0]:
#             return True
#         return False
#
# L1 = MyList(range(2, 4))
# L2 = MyList(range(1, 4))
# print(L1, '>', L2, '=', L1 > L2)

# 此示例示意一元运算符的重载
# class MyList:
#     def __init__(self, iterable=()):
#         self.data = [x for x in iterable]
#
#     def __repr__(self):
#         return 'MyList(%r)' % self.data
#
#     def __neg__(self):
#         '''规则 正变负，负变正'''
#         # 用生成器表达式，减少内存消耗
#         L = (-x for x in self.data)
#         return MyList(L)

# L1 = MyList([1, -2, 3, -4, 5])
# L2 = -L1
# print(L2)

# 此示例示意in/ not in方法的重载
# class MyList:
#     def __init__(self, iterable=()):
#         self.data = [x for x in iterable]
#
#     def __repr__(self):
#         return 'MyList(%r)' % self.data
#
#     # 重载in方法
#     def __contains__(self, item):
#         return item in self.data
#
# L1 = MyList([1, -2, 3, -4, 5])
# if 3 in L1:
#     print(True)
# else:
#     print(False)

# 此示例示意索引/切片的重载
# class MyList:
#     def __init__(self, iterable=()):
#         self.data = [x for x in iterable]
#
#     def __repr__(self):
#         return 'MyList(%r)' % self.data
#
#     # 索引取值
#     def __getitem__(self, i):
#         print('i = ', i)
#         if isinstance(i, slice):
#             print('正在执行切片取值操作')
#             print('起始值:', i.start)
#             print('终止值:', i.stop)
#             print('步长值:', i.step)
#         return self.data[i]
#
#     # 索引赋值
#     def __setitem__(self, key, value):
#         self.data[key] = value
#
#     # 索引删除
#     def __delitem__(self, key):
#         del self.data[key]
# L1 = MyList([1, -2, 3, -4, 5])
# x = L1[0]       # 调用 L1.__getitem__
# print(x)
# L1[1] = 2
# print(L1[1])
# del L1[4]
# print(L1)
# x = L1[::2]     # python重新构造i =  slice(None, None, 2)
# print(x)

# 此示例示意特性属性的用法
class Student:
    def __init__(self, score):
        self.__score = score
    # 写法二
    @property
    def score(self):
        '''实现getter'''
        return self.__score

    @score.setter
    def score(self, s):
        '''实现setter'''
        if 0 <= s <= 100:
            self.__score = s
        else:
            raise ValueError('值超出范围')
    # 写法一
    # 虚拟属性，仿真类属性
    # score = property(get_score, set_score)

c = Student(59)
# print(c.score)  # 出错
# print(c.get_score())
# c.score = 97
# print(c.score)

# 练习
# 1.修改MyList 实现两个自定义的列表相加
# class MyList:
#     class MyIterator:
#         def __init__(self, lst):
#             self.data = lst
#             self.index = 0
#
#         def __next__(self):
#             if self.index >= len(self.data):
#                 raise StopIteration('ERROR:索引超出范围')
#             s = self.data[self.index]
#             self.index += 1
#             return s
#
#     def __init__(self, iterable=()):
#         self.data = [x for x in iterable]
#
#     def __repr__(self):
#         return 'MyList(%r)' % self.data
#
#     def __iter__(self):
#         return MyList.MyIterator(self.data)
#
#     def __len__(self):
#         return len(self.data)
#
#     # 算术运算符
#     def __add__(self, rhs):
#         return MyList(self.data + rhs.data)
#
#     # 算术运算符
#     def __mul__(self, rhs):
#         return MyList(self.data * rhs)
#
#     # 反向算术运算符
#     def __rmul__(self, lhs):
#         return MyList(self.data * lhs)
#
#     # 复合赋值算术运算符
#     def __iadd__(self, rhs):
#         # 原id不变，进行列表追加
#         self.data.extend(rhs.data)
#         return self
#
#     def append(self, v):
#         self.data += v


# L = MyList("ABCD")
# print(L)
# L.append('E')
# print(L)
# for i in L:
#     print(i, end=' ')
# print("长度为:", len(L))
#
# L1 = MyList([1, 2, 3])
# print(L1)
# L2 = MyList([4, 5, 6])
# print(L1, L2)
# L3 = L2 + L1
# print(L3)
# L4 = MyList([1, 2, 3])
# print(type(L4))
# L5 = L4 * 2
# L6 = 2 * L4
# print(L5)
# print(L6)

# L1 = MyList([1, 2, 3])
# L2 = MyList([4, 5, 6])
# print('id(L1)=', id(L1))
# L1 += L2
# print('L1=', L1)
# print('id(L1)=', id(L1))

# 2.实现有序集合类OrderSet 能实现两个集合的
# 交集 &
# 全集 |
# 并集 -
# 对称补集 ^
# == / !=
# in / not in 等集合操作
# 要求内部用list存储
# s1 = OrderSet([1, 2, 3, 4])
# s2 = OrderSet([3, 4, 5])
class OrderSet:
    def __init__(self, iterable=()):
        self.data = []
        # 升序
        iterable.sort()
        # 去重
        for i in iterable:
            if i not in self.data:
                self.data.append(i)

    def __repr__(self):
        return 'OrderSet(%r)' % self.data

    # 交集
    def __and__(self, rhs):
        s = set(self.data) & set(rhs.data)
        return OrderSet(list(s))

    # 并集
    def __or__(self, rhs):
        s = set(self.data) | set(rhs.data)
        return OrderSet(list(s))

    # 补集
    def __xor__(self, rhs):
        s = set(self.data) ^ set(rhs.data)
        return OrderSet(list(s))

    # 等于
    def __eq__(self, rhs):
        if self.data == rhs.data:
            return True
        return False

    # in
    def __contains__(self, rhs):
        return rhs in self.data

# s1 = OrderSet([4, 3, 2, 1, 5, 2, 1])
# s2 = OrderSet([3, 4, 5])
# print('交集', s1 & s2)
# print('并集', s1 | s2)
# print('补集',s1 ^ s2)
# if OrderSet([1, 2, 3]) != OrderSet([1, 2, 3, 4, 5]):
#     print('不相等')
# if s2 == OrderSet([3, 4, 5]):
#     print('等于')
# if 2 in s1:
#     print('2,在s1内')






