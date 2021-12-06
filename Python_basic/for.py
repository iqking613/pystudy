# s = "ABCD"
#
# for ch in s:
#     print('ch======>>', ch)
#
# print("当for语句结束后，ch绑定的是:", ch)


# s = 'ABCDEF'
# for i in s:
#     print('i===>>', i)
#     if i == 'D':
#         break
# else:
#     print("结束")


# 练习
# 任意输入一段字符串
# 1.计算输入的字符'A'的个数，并打印出来
# 2.计算出空格的个数，并打印出来
# 要求用for语句，不允许用，S.count方法

# 思考用while语句能否实现上述功能
# s = input("请输入字符串:")
# a = 0
# k = 0
# for i in s:
#     if i == 'A':
#         a += 1
#     if i == ' ':
#         k += 1
# print("字符'A'的个数是:", a)
# print("空格的个数是:", k)

# i = 0
# A = 0
# K = 0
# while i < len(s):
#     sSum = s[i]
#     if sSum == 'A':
#         A += 1
#     if sSum == ' ':
#         K += 1
#     i += 1
# print("字符'A'的个数是:", A)
# print("空格的个数是:", K)

# for x in range(1, 21):
#     print(x, end=' ')

# 练习
# 求100以内有哪些整数与自身+1的乘积再对11求余的结果等于8
# x * (x+1) % 11 == 8
# for x in range(100):
#     i = x * (x + 1) % 11
#     # print(i)
#     if i == 8:
#         print(x)

# 练习
# 1.写程序计算1 + 3 + 5 + 7 +....99的和
#   要求用for语句和while语句两种方式实现
# Sum = 0
# for i in range(1, 100, 2):
#     Sum += i
# print(Sum)

# i = 1
# Sum1 = 0
# while i <= 99:
#     if i % 2 == 1:
#         Sum1 += i
#     i += 1
# print(Sum1)

# i = 1
# s = 0
# while i < 100:
#     s += i
#     i += 2
# print(s)

# 2.用while顺实现打印
# 1 3 5 7 9....19
# 打印在一行内
# i = 1
# while i <= 19:
#     if i % 2 == 1:
#         print(i, end=' ')
#     i += 1
# print()

# i = 1
# while i <= 19:
#     print(i, end=' ')
#     i += 2
# else:
#     print()

# 3.将上题用for语句来实现
# a = 0
# for i in range(1, 100, 2):
#     a += i
#     if i <= 19:
#         print(i, end=' ')
# print()
# print(a)

# for x in range(5):
#     for y in range(10):
#         print(x, "---", y)

# 练习
# 用for语句实现以下：
# 1.输入一个数代表正方形的宽度，打印如下
#     1 2 3 4 5
#     1 2 3 4 5
#     1 2 3 4 5
#     1 2 3 4 5
#     1 2 3 4 5
# s = int(input("输入一个数字:"))
#
# for i in range(1, s + 1):
#     for y in range(1, s + 1):
#         print(y, end=' ')
#     print()

# 2.写程序来改写上题
#     1 2 3 4 5
#     2 3 4 5 6
#     3 4 5 6 7
#     4 5 6 7 8
#     5 6 7 8 9

# s = int(input("输入一个数字:"))

# 方法一
# for i in range(1, s + 1):
#     for y in range(i, i + s):
#         print(y, end=' ')
#     print()

# 方法二
# for i in range(s):
#     for line in range(i + 1, i + 1 + s):
#         print(line, end=' ')
#     print()

# 方法三
# def print_a_line(line, n):
#     for i in range(line + 1, line + 1 + n):
#         print("%2d" % i, end=' ')
#     # 换行
#     print()
#
# s = int(input("输入一个数字:"))
# for line in range(s):
#     print_a_line(line, s)
