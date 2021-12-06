#此示例函数的定义和调用
# def say_heelo():
#     print("hello world!")
#     print("hello tarena!")

# say_heelo()     #调用函数

#此示例示意带有形成参数的函数的定义
#写一个函数，打印出给定的两个数的最大值
# def mymax(a, b):
#     print('a = ', a)
#     print('b = ', b)
#     if a > b:
#         print(a, "最大")
#     else:
#         print(b, '最大')

# mymax(2, 3)


#此示例示意带有rturn
# def say_heelo():
#     print("hello world!")
#     print("hello tarena!")
#     return  #返回到调用此函数的地方
#     # print("hello world!")
# say_heelo()     #调用函数

#此示例示意位置传参
# def myfun1(a, b, c):
#     #这是一个函数的传参示例，此函数以后不会改变代码
#     print("a的值是：", a)
#     print("b的值是：", b)
#     print("c的值是：", c)
# myfun1(1, 2, 3)

#此示例示意序列传参
# def myfun1(a, b, c):
#     #这是一个函数的传参示例，此函数以后不会改变代码
#     print("a的值是：", a)
#     print("b的值是：", b)
#     print("c的值是：", c)
# s1 = [11, 22, 33]
# myfun1(*s1)     #相当于myfun1(11, 22, 33)

#此示例示意关键字传参
# def myfun1(a, b, c):
#     #这是一个函数的传参示例，此函数以后不会改变代码
#     print("a的值是：", a)
#     print("b的值是：", b)
#     print("c的值是：", c)
# myfun1(c = 22, b = 33, a = 11)

#此示例示意字典关键字传参
# def myfun1(a, b, c):
#     #这是一个函数的传参示例，此函数以后不会改变代码
#     print("a的值是：", a)
#     print("b的值是：", b)
#     print("c的值是：", c)
# d = {'a': 100, 'b': 200, 'c': 300}
# myfun1(**d)      #等同于myfun1(a = 100, b = 200, c = 300)


#+----------------------------------函数形参定义------------------------------------+

# 函数的缺省参数
# def info(name, age=1, address='未知'):
#     print('我叫', name, '我今年', age, '岁', '我家住址:', address)
# info("连余学", 23)

#此示例示意星号元组形参
# def func(*args):
#     print("参数个数是:", len(args))
#     print("args:", args)
#
# func(1, 3, 4, 5, 6)

#此示例示意命名关键字形参
# def fa(*, a, b):
#     print('a=', a)
#     print('b=', b)
# fa(a = 100, b=200)

#此示例示意双星号字典形参
# def fa(**kwargs):
#     print("调用时传的关键字传参的个数是:", len(kwargs))
#     print('kwargs=', kwargs)
#
# fa(**{'a': 100, 'b': 200})
# fa(a=100, b=100)

#此示例示意局部变量
# a = 100
# b = 200
# def fx(c):
#     d = 400
#     print(a, b, c, d)
# fx(300)
# # print("全局内的", a, b, c, d)

# 练习
# 1.写一个函数myadd，此函数中的参数列表里有两个参数x，y此函数的功能打印
# x + y的和。
# def myadd(x, y):
#     print(x + y)

# myadd(100, 300)
# myadd("ABC", "123")

# 2.写一个函数mySum, 传入一个参数x代表终止整数。
# def mySum(x):
#     Sum = 0
#     for i in range(1, x + 1):
#         Sum += i
#     print(Sum)
#
# mySum(4)

# 3.写一个函数mymax，给函数传递两个参数，返回参数中最大的一个
# 方法一
# def mymax (x, y):
#     if x > y:
#         return x
#     else:
#         return y
# # 方法二
# def mymax (x, y):
#     if x > y:
#         return x
#     return y

# v = mymax(27, 27)
# print(v)

# 4.写一个函数input_number
# 此函数用来获取用户循环输入的整数，当用户输入负数时结束输入。
# 将用户输入的数字以列表的形式放回。
# 再将内建函数max，min，sum取出用户输入的最大值，最小值及和
# def input_number():
#     Lists = []
#     while True:
#         i = int(input("请输入一个整数:"))
#         if i < 0:
#             break
#         Lists.append(i)
#     return Lists
#
# def list_max(list):
#     listmax = list[0]
#     i = 0
#     while i < len(list):
#         if list[i] > listmax:
#             listmax = list[i]
#         i += 1
#     return listmax
#
# def list_min(list):
#     listmin = list[0]
#     i = 0
#     while i < len(list):
#         if list[i] < listmin:
#             listmin = list[i]
#         i += 1
#     return listmin
#
# def list_sum(list):
#     listsum = 0
#     i = 0
#     while i < len(list):
#         listsum += list[i]
#         i += 1
#     return listsum
#
# L =  input_number()
# print(L)
# print("用户输入的最大数是:", list_max(L))
# print("用户输入的最小数是:", list_min(L))
# print("用户输入的数和是:", list_sum(L))

# 5.写一个函数，print_odd
#     打印从begin开始，到end结束内的全部奇数(不包含end)
# def print_oadd(begin, end):
#     L = []
#     for i in range(begin, end):
#         if i % 2 == 0:
#             continue
#         L.append(i)
#     return print(L)
#
# print_oadd(1, 10)

# 6.定义两个函数：
# sum3(a, b, c) 用于返回三个数的和
# pow3(x) 用于返回x的三次方

# def list_sum(a, b, c):
#     return a + b + c
# def list_pow(x):
#     return x ** 3

#     用以上的函数计算
#     1)计算1的立方 + 2的立方 + 3的立方的和
#     即：1**3 + 2**3 + 3**3的和
# L1 = list_sum(list_pow(1), list_pow(2), list_pow(3))
# print(L1)

#     2)计算1 + 2 + 3的和的立方
#     即：(1 + 2 + 3) ** 3
# L2 = list_pow(list_sum(1, 2, 3))
# print(list_pow(L2))

# 7.改写之前的学生信息管理程序
# 改为两个函数：
#     1)写一个函数input_student()
#     用于返回学生信息的字典列表
#
#     2)写一个函数output_student(lst)
#     此函数传入一个列表lst，即字典的列表
#     此函数把lst的内容以表格形式打印出来
def input_student():
    list = []
    while True:
        # 录入信息
        name = input("请输入姓名:")
        if name == '':
            break
        age = int(input("请输入年龄:"))
        score = int(input("请输入成绩:"))

        # 每组以字典方式存入
        d = {}
        d['name'] = name
        d['age'] = age
        d['score'] = score

        # 每组字典存入列表中
        list.append(d)
    return list
# data = input_student()
# print(data)
# [{'name': 'zhangsan', 'age': 20, 'score': 98}, {'name': 'lisi', 'age': 24, 'score': 95}, {'name': 'wangwu', 'age': 29, 'score': 100}, {'name': 'zhaoliu', 'age': 19, 'score': 99}]

def output_student(lst):
    # 获取name键最大长度
    name_len = 0
    for i in lst:
        v = i.get('name')
        if len(v) > name_len:
            name_len = len(v)

    # 打印框
    print('+' + '-' * (name_len + 2) + '+' + '-' * 5 + '+' + '-' * 7 + '+')
    print('|' + 'name'.center(name_len + 2) + '|' + 'age'.center(5) + '|' + 'score'.center(7) + '|')
    print('+' + '-' * (name_len + 2) + '+' + '-' * 5 + '+' + '-' * 7 + '+')

    # 循环取出列表中每一个元素
    for i in lst:
        print('|' + i.get('name').center(name_len + 2) + '|' + str(i.get('age')).center(5) + '|' + str(
            i.get('score')).center(7) + '|')

    print('+' + '-' * (name_len + 2) + '+' + '-' * 5 + '+' + '-' * 7 + '+')

# output_student(data)
# print("请再输入学生信息...")
# data += input_student()
# output_student(data)
# +----------+-----+-------+
# |   name   | age | score |
# +----------+-----+-------+
# | zhangsan |  20 |   98  |
# |   lisi   |  24 |   95  |
# |  wangwu  |  29 |  100  |
# | zhaoliu  |  19 |   99  |
# +----------+-----+-------+

# 8.写一个函数minmax(a, b, c)
#     有三个参数，返回这三个参数中最小值和最大值，
#     要求，形成元组，最小值在前，最大值在后
# def minmax(a, b, c):
#     max = a
#     if b > max:
#         max = b
#     if c > max:
#         max = c
#
#     min = a
#     if b < min:
#         min = b
#     if c < min:
#         min = c
#     return (min, max)
# t = minmax(2, 3, 9)
# print(t)

# 9.写一个程序myadd
# 此函数可以计算两个数的和，也可以计算三个数的和
# def myadd(a, b, c=0):
#     return a + b + c
#
# print(myadd(1,2,10))

# 10.写一个函数，print_odd
# 此函数可以传递一个实参，也可以传两个实参，但传递一个实参时代表结束值，
# 当传递两个参数时，第一个实参代表起始值，第二个代表终止值。
#     打印出在此区间内的全部奇数，不包含结束数：
# 方法一
# def prin_odd(start, end=0):
#     li = []
#     if end == 0:
#         for i in range(start):
#             if i % 2 == 1:
#                 li.append(i)
#     else:
#         for i in range(start, end):
#             if i % 2 == 1:
#                 li.append(i)
#     return li
# L = prin_odd(10, 20)
# print(L)

# 方法二
# def prin_odd(start, end=None):
#     if end is None:
#         a = 1
#         b = start
#     else:
#         a = start
#         b = end
#     if a % 2 == 0:
#         a += 1
#     for x in range(a, b, 2):
#         print(x)
#     print()
# prin_odd(5, 0)
# y = prin_odd(10, 29)
# prin_odd(y)
    # else:
    #     start = start
    #     end = end

# 11.写一个函数：
# mysum可以传入任意个实参的数字，返回所有实参的和
# def mysum(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
# L = mysum(1,2,3,4,5,6,7,8,9,10)
# print(L)

# 12.写一个函数，mymax类似于内建的函数max
# 仿造max写一个mymax函数 ，功能与max完全相同
# 要求不允许使用max函数
# def mymax(a, *args):
    # 语法一
    # L = args
    # max1 = 0
    # if len(args) >= 2:
    #     for i in args:
    #         if i > max1:
    #             max1 = i
    # elif len(L[0]) >= 2:
    #     for i in (L[0]):
    #         if i > max1:
    #             max1 = i

    # 语法二
    # if len(args) == 0:
    #     max1 = a[0]
    #     for i in a:
    #         if i > max1:
    #             max1 = i
    # else:
    #     max1 = a
    #     for i in args:
    #         if i > max1:
    #             max1 = i
    #
    #
    # return print(max1)


# mymax([6, 8, 3, 5])
# mymax(300, 200)
# mymax(1, 8, 9, 2, 3, 5, 12, 4)
# mymax(100)        报错

# 13.创建一个全局变量L = []
# 写一个函数：
# def input_number():
#     (...)
# 此函数每次调用将从键盘输入一些数输出追加到列表L中
# L = []
# def input_number():
#     a = input("输入数字:")
#     L.append(a)
#
# input_number()
# print(L)

# 14.写一个函数isprime(x)
#     判断x是否为素数，如果是素数，返回True，否则返回False
# def isprime(x):
#     if x > 1:
#         for i in range(2, x):
#             if x % i == 0:
#                 return False
#         else:
#            return True
#     else:
#         return False
# L = isprime(4)
# print(L)

# 15.写一个函数prime_m2n(m, n)
#     返回从m开始 ，到n结束范围内的素数，返回这些素数的列表并打印
#     如:
#         L = prime_m2n(5, 10)
#         print(L)   [5, 7]
# def prime_m2n(m, n):
#     L = []
#     for i in range(m, n):
#        for x in range(2, i):
#            if i % x == 0:
#                break
#        else:
#            L.append(i)
#     return print(L)
#
# prime_m2n(5, 10)

# 16.写一个函数pimes(n)
#     返回小于n的全部素数的列表，并打印这些素数
#     如:
#         L = pimes(10)
#         print(L)[2, 3, 5, 7]
#     1)打印100以内的全部素数
#     2)打印200以内的全部素数的和
# def pimes(n):
#     L = []
#     if n > 1:
#         for i in range(2, n):
#             for x in range(2, i):
#                 if i % x == 0:
#                     break
#             else:
#                 L.append(i)
#     else:
#         print("有误")
#     return L
# L = pimes(100)
# L1 = pimes(200)
# print(L)
# print(sum(L1))


# 17.编写函数fn()此函数返回下列级别的和:
#     fn(n) = 1/(1*2) + 1/(2*3) + 1/(n*(n - 1))的和
#     print(fn(100))
# def fn(n):
#
# fn(10)
#
# i = 1
# sum = 0
# while i < 100:
#     # print(i)
#     L = 1 / (i * (i + 1))
#     # print(1 / (i * (i + 1)))
#     sum += L
#     i += 1
# print(sum)
# # return print(sum)

# 18.已知全班学生的名单，存于集合中 names
#     写一个点名签到程序
#         随机输入学生的姓名，让用户输入:"y"代表已到，输入"n"或其他代表未到。
#         当点名结束后，打印未到者的名单
names = {"zhangsan", "lisi", "wangwu", "xiaohon", "xiaoming", "xiaolian"}
def clock(*args):
    L = list(args[0])
    L1 = []
    for i in L:
        name = input("姓名:%s【输入'y已到/x未到】:" % i)
        if name == 'y':
            pass
        else:
            L1.append(i)
    return print("未到名单:", L1)
    # return print("未到名单:", ' '.join(L1))
# clock(names)

# 19.写一个函数print_even，传入一个参数n代表终止数，此函数调用将打印2 4 6 8 .....n 之间所有的偶数
# def print_even(n):
    # 方法一
    # L = []
    # for i in range(2, n, 2):
    #     L.append(i)
    # return L

    # 方法二
#     L = []
#     i = 2
#     while i < n:
#         L.append(i)
#         i += 2
#     return L
# L = print_even(8)
# print(L)

# for i in L:
#     print(i, end=' ')
# [2, 4, 6]
# 2 4 6


# 练习
# 1. 1元一瓶水，喝完后两个空瓶换一瓶，问:你有20元钱，最多可以喝到几瓶汽水？
# def sum(n):
#     sum = 0
#     for i in range(1, n + 1):
#         sum += 1
#         if sum % 2 == 0:
#             sum += 1
#     return print(sum)
#
# sum(20)

# 2.用字典的方式完成下面一共小型的学生管理系统。
#     1.学生有以下属性：姓名，年龄，考试分数包括：语文，数学，英语得分。
#     2.给学生添加一门python课程成绩，李明60，张强80；
#     3.把张强的数学成绩由82改为89：
#     4.删除张强同学的年龄数据
#     5.对张强同学的课程分数按照从低到高排序输出
# def input_name():
#     L = []
#     while True:
#         name = input("姓名:")
#         if name == '':
#             break
#         age = input("年龄:")
#         yw = input("语文:")
#         sx = input("数学:")
#         yy = input("英语:")
#         d = {}
#         d["name"] = name
#         d["age"] = age
#         d["yw"] = yw
#         d["sx"] = sx
#         d["yy"] = yy
#         L.append(d)
#     return L
# data = input_name()
# print(data)
L = [{'name': 'liming', 'age': '25', 'yw': '80', 'sx': '75', 'yy': '85'}, {'name': 'zhangqiang', 'age': '23', 'yw': '75', 'sx': '82', 'yy': '78'}]

# 2.给学生添加一门python课程成绩，李明60，张强80；
# L[0]["python"] = 60
# L[1]["python"] = 80
# print(L)

# 3.把张强的数学成绩由82改为89：
# L[1]["sx"] = 89
# print(L)

# 4.删除张强同学的年龄数据
# del L[1]["age"]
# print(L)

# 5.对张强同学的课程分数按照从低到高排序输出
# for k in L:
#     if k["name"] == "zhangqiang":
#         L = []
#         for k, v in k.items():
#             if k == "yw":
#                 L.append(v)
#             elif k == "sx":
#                 L.append(v)
#             elif k == "yy":
#                 L.append(v)
#         print(sorted(L))


# 3.写一共myrange函数，参数可以传1~3个,世界意义同range函数规则相同，此函数返回符合range()函数规则的列表
# 如：
#     L = myrange(4)
#     print(L)    #[0,1,2,3]
#     L = myrange(4, 6)
#     print(L)   #[4,5]
#     L = myrange(1,10, 3)
#     print(L)   #[1, 4, 7]

# 方法一
# def myrange(start, *args):
#     L = []
#     if len(args) == 0:
#         i = 0
#         while i < start:
#             L.append(i)
#             i += 1
#     elif len(args) == 1:
#         i = start
#         while i < args[0]:
#             L.append(i)
#             i += 1
#     else:
#         i = start
#         while i < args[0]:
#             L.append(i)
#             i += args[1]
#     return print(L)
# myrange(1,100,12)

# 方法二
# def myrange(start, stop=None, step=1):
#     r_lst = []
#     if stop is None:
#         stop = start
#         start = 0
#     if step > 0:
#         while start < stop:
#             r_lst.append(start)     # 把当前数加入到列表中
#             start += step           # 让start向后移动，准备下次判断
#     else:   # 当步长小于0的情况
#         for x in range(start, stop, step):
#             r_lst.append(x)
#     return r_lst
# 方法三
# def myrange(start, stop=None, step=1):
#     if stop is None:
#         stop = start
#         start = 0
#
#     return list(range(start, stop, step))
# L1 = myrange(10)
# print(L1)
# L2 = myrange(1, 10)
# print(L2)
# L3 = myrange(1, 10, 2)
# print(L3)
# L4 = myrange(10, 1, -2)
# print(L4)

# 4.print函数的参数列表定义
# def myprint(*args, sep=' ', end='\n'):
#     L = [str(x) for x in args]  #把所有元素转为字符串列表
#     s = sep.join(L)
#     s += end
#     print(s)
# myprint(1,2,3,4)

# def myprint(*args, sep=' ', end='\n'):
#     print(*args, sep=sep, end=end)
# myprint(1,2,3,4)

# 5.算出100~999之间的水仙花数（Narcissistic numver）水仙花数是指百位的3次方，加上十位的3次方，加上个位的3次方等于原数的整数
# 例如：153 = 1**3 + 5**3 + 3**3
#     建议，先写一个函数is_narcissistic（n）
#     来判断n是否为水仙花数，如果是返回True，否则返回False
#     再调用此函数进行判断
def is_narcissistic(n):
    b = n // 100        # 百位
    s = n % 100 // 10    # 十位
    g = n % 10          # 个位
    if n == b**3 + s**3 + g**3:
        return True
    else:
        return False
# i = is_narcissistic(154)
# print(i)

# for i in range(100, 1000):
#     x = is_narcissistic(i)
#     if x is True:
#         print(i)

