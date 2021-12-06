
# i = 1   #先定义一个变量，用于控制循环条件
#
# while i <= 10:
#     print("这是第%d行" % i)
#     i += 1

# 练习
#1.输入一行字符串，将字符串中Unicode编码值最大的一个字符打印出来（不允许用max函数）
# W = input("请输入一个字符串:")
# x = 1
# y = W[0]
# while x < len(W):
#     m = W[x]
#     if ord(m) > ord(y):
#         y = m
#     x += 1
# print("最大Unicode值是:", y)

#2.打印从0开始的浮点数，每个数增加0.5，打印出10以内的这样的数:
#0.0 0.5 1.0 1.5......
# x = 0.0
# while x < 10:
#     print(x)
#     x += 0.5


# 练习
# 1.打印1~20整数
# i = 1
# while i <= 20:
#     print(i)
#     i += 1

# 2.打印从10开始到0（不包含0）之间的整数
# i = 10
# while i > 0:
#     print(i)
#     i -= 1

# 3.打印1~20的整数，打印在一行内
# i = 1
# while i <= 20:
#     print(i, end=' ')   #end默认为\n为换行
#     i += 1

# 4.打印1~20的整数，每行打印5给，打印四行
# i = 1
# while i <= 20:
#     print(i, end=' ')
#     # print(i / 5)
#     if i % 5 == 0:
#         print()
#     i += 1

# 5.输入一个整数n，打印出一个长方形 n代表长方形的宽度的字符数和高的行数
# s = int(input("请输入一个数字:"))
# i = 1
# print("#" * s)
# while i <= (s // 2):
#     print("#" + ' ' * (s - 2) + "#")
#     i += 1
# print("#" * s)

#练习while-else

# x = 1
# while x <= 10:
#     i = 1
#     while i <= 20:
#         print(i, end=' ')
#         i += 1
#     else:
#         print()
#     x += 1
# else:
#     print()

# 练习
# 输入一个数，打印指定宽度的正方形
# s = int(input("请输入一个数:"))
# i = 1
# while i <= s:
#     j = 1
#     while j <= s:
#         print(j, end=" ")
#         j += 1
#     else:
#         print()
#     i += 1

# 练习
# 1.写程序，计算1+2+3+4+...100的和
# i = 1
# s = 0
# while i <= 100:
#     s += i
#     i += 1
# print(s)

# 2.写程序，任意输入一个数n，计算1+2+3+4...+(n-1) + n
# s = int(input("请输入应该数:"))
# i = 1
# Sum = 0
# while i <= s:
#     Sum += i
#     i += 1
# print(Sum)

# 练习
# 1.输入任意一个数，当输入负数时结束输入，当输入完成后，打印所输入的这些数的和是多少？
# s = int(input("请输入一个数字:"))
#
# i = 1
# if s > 0:
#     Sum = 0
#     while i <= s:
#         Sum += i
#         i += 1
#     print("数字和:", Sum)
# else:
#     print("您输入的数字不能小于等于0")

# while True:
#     s = int(input("请输入一个数字:"))
#
#     i = 1
#     if s > 0:
#         Sum = 0
#         while i <= s:
#             Sum += i
#             i += 1
#         print("数字和:", Sum)
#         break
#     else:
#         print("您输入的数字不能小于等于0")

# he = 0
# while True:
#     s = int(input("请输入一个数字:"))
#     if s < 0:
#         break
#     he += s
# print("合计:", he)

# 2.写程序求:
#     Sn = 1 + 1/2 + 1/4 + 1/8 + .....1/(2**n)
#     求当前n等同于100时，sn的值是多少？
# sn = 0
# n = 0
# while n <= 100:
#     a = 1/(2**n)
#     sn += a
#     n += 1
# print("和是:", sn)

# 错误做法
# i = 1
# y = 1
# Sn = 0
# while i <= 100:
#     i *= 2
#
# print(i)

# 3.用while语句实现打印三角形，输入一个整数，表示三角形的宽度和高度，打印出相应的直角三角形:
#   如：
#     请输入三角形的宽度：4
#     1）打印如下
#         *
#         **
#         ***
#         ****
# s = int(input("请输入三角形的宽度:"))

# *
# **
# ***
# ****

# i = 1
# while i <= s:
#     print("*" * i)
#     i += 1
# print("---------------")

#    *
#   **
#  ***
# ****

# i = 1
# while i <= s:
#     print(' ' * (s - i) + "*" * i)
#     i += 1
# print("---------------")

# ****
# ***
# **
# *

# i = 1
# Sum = s
# while i <= s:
#     print("*" * Sum)
#     Sum -= 1
#     i += 1
# print("---------------")

# stars = s
# while stars > 0:
#     print("*" * stars)
#     stars -= 1
# print("---------------")

# ****
#  ***
#   **
#    *

# i = 1
# Sum = s
# while i <= s:
#     print(' ' * (s - Sum) + "*" * Sum)
#     Sum -= 1
#     i += 1

# 4.输入任何行文字，存于列表L中，当不输入任何内容直接回车后结束输入
#     1).打印L列表中的内容
#     2).计算您共输入了几行内容
#     3).计算您共输入了多少个字符
# L = []
# Sum = 0
# i = 0
# while True:
#     s = input("请输出文字:")
#     if s == '':
#         break
#     L += [s]
#     Sum += len(s)
#     i += 1
#
# print("列表内容:", L)
# print("总行数:", len(L))
# print("总字符:", Sum)

# 5.输入一个整数（代表树干的高度）
#     打印出如下一棵树
#     输入:2
#     打印:
#         *
#        ***
#         *
#         *
#     输入:3
#     打印:
#         *
#        ***
#       *****
#         *
#         *
#         *
# s = int(input("输入一个字符串:"))
# #
# x = 1
# o = 1
# i = 1
# while o <= s:
#     while i <= s:
#         S1 = "*" * x
#         print(S1.center(s + s - 1))
#         x += 2
#         i += 1
#     S2 = "*"
#     print(S2.center(s + s - 1))
#     o += 1
# print()
# #树叶部分
# for i in range(1, s + 1):
#     starts = i * 2 - 1  #算出星号部分
#     blank = s - i       #算出左侧空格的个数
#     print(' ' * blank + '*' * starts)
#
# #树干部分
# for x in range(s):
#     print(' ' * (s - 1) + '*')

# 6.写一个程序，任何输入一个整数，判断这个数是不是素数（prime）
# 素数（也叫质数）只能被1和自身整除的正整数：
#     如2 3 5 7 11等
#     提示:
#     用排除法:当判断x是否是素数时，只能让x分别处以:
#     2, 3, 4, 5, .....x-1,
#     只要整除了，那x不是素数，否则x是素数
#公式：
# x % range(2, x )== 0  #不是素数
# x % range(2, x ) != 0  #x是素数

# s = int(input("请输入一个整数:"))
# if s > 1:
#     for i in range(2, s - 1):
#         if s % i == 0:
#             print(i, "*", s//i, "=", s, "不是素数")
#             break
#     else:
#         print(s, "是素数")
# else:
#     print(s, "不是素数")
#     print(s, "不是素数")

# 7.算出100~1000以内的水仙花数(Naricissistic Number)
# 水仙花数是指百位的3次方 加上 十位的3次方 加上 个位的3次方等于原数的数
#     如:
#         153 = 1**3 + 5**3 + 3**3
#     答案:
#         153, 370,....

# 方法一
# for i in range(100, 100000):
    # #取个位
    # a = i % 10
    # #取十位
    # b = (i % 100 - a) // 10
    # #取百位
    # c = (i % 1000 - a - b) // 100
    # if i == (a ** 3) + (b ** 3) + (c ** 3):
    #     print(i)
# 方法二
#     c = i // 100
#     b = i // 100 % 10
#     a = i // 10 % 10
#     e = i % 10
#     if i == c ** 3 + b ** 3 + a ** 3 + e ** 3:
#         print(i)

# 方法三
for i in range(100, 1000):
    y = str(i)
    # 例如
    # b = y[0]
    # s = y[1]
    # g = y[2]
    # if i == int(b) ** 3 + int(s) ** 3 + int(g) ** 3:
    #     print(i)

    # x = 0
    # Sum = 0
    # while x < len(y):
    #     Sum += int(y[x]) ** 3
    #     x += 1
    # if Sum == i:
    #     print(y)





