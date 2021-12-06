#练习
# 1.已知有列表:
#     L = [3, 5]
#     1)用索引和切片等操作，将原列表改变为:
#     L = [1, 2, 3, 4, 5, 6]
# L = [3, 5]
# L[1:1] = [4]
# L[0:0] = [1, 2]
# L[5:5] = [6]
# print(L)
#     2)将列表反转，删除最后一个元素后打印此列表
#         print(L)
#         [6, 5, 4, 3, 2, 1]
#反转
# L[:] = L[::-1] #L = L[::-1]
# del L[-1]
# print(L)

# 2.写程序,让用户输入一些整数，当输入-1时结束输入，将这些数存于列表L中
#     1)打印用户共输入了几个数？
#     2)打印您输入的数最大数是多少
#     3)打印您输入的数最小数是多少
#     4)打印您输入的数平均值是多少
# L = []
# while True:
#     s = int(input("请输入整数:"))
#     if s == -1:
#         break
#     L += [s]
# print(L)
# print("总数", len(L))
# print("最大", max(L))
# print("最小", min(L))
# print("平均", (sum(L)/len(L)))

# 3.输入多行文字，存入列表中，每次输入回车后算一行，任意输入多行，当输入回车（即输入空格时结束输入）
#     1)按原输入内容在屏幕上输出内容
#     2)打印出您输入了多少行文字
#     3)打印出您共输入了多少个字符
# L = []
# Sum = 0
# while True:
#     s = input("请输入:")
#     if s == '':
#         break
#     L.append(s)     #等同于L += [s]
#     Sum += len(s)
#
# for i in L:
#     print(i)
# print("行数", len(L))
# print("字符数", Sum)

# 4.有字符串'hello',请用此字符串生成:
#     'h e l l o' 和 'h-e-l-l-o'
# s = "hello"
# a = ' '.join(s)
# b = '-'.join(s)

# s = 'hello'
# for i in [s]:
#     L1 = list(i)
#     L2 = ' '.join(L1)
#     print(L2)
#     L3 = '-'.join(L1)
#     print(L3)

# 5.写一个程序，让用户输入很多正整数，当输入小于零的数时结束输入。
#     1)打印这些数中最大的一个数
#     2)打印这些数中第二大的一个数
#     3)删除最小的一个数
#     4)打印剩余数的和
# L = []
# while True:
#     s = int(input("请输入整数:"))
#     if s < 0:
#         break
#     L.append(s)
# L.sort(reverse=True)
# print("最大数为:", max(L))
# print("最大数为:", L[0])
# print("第二大数为:", L[1])
# print("删除最小的数为:", L.pop())
# print("剩余和为:", sum(L))
# print(L)

# 6.用列表推导式生成1~100内奇数的列表
#     结果为:[1, 3, 5, 7,...99]
# L = [x for x in range(1, 100, 2)]
# print(L)
# L = [x for x in range(1, 100) if x % 2 == 1]
# print(L)

# 7.列表推导式生成一个数值为1~9的平方的列表，去掉所有的奇数的平方
# L = [x**2 for x in range(1, 10) if x % 2 == 0]
# print(L)

# 8.已知有一个字符串s = '100,200,300,500,800'
#     将其转换为整数的列表存于L列表中L = [100, 200, 300, 500, 800]
# s = '100,200,300,500,800'
# s1 = s.split(',')
# L = []
# for x in s1:
#     L.append(int(x))
# print(L)

# 例如列表推导式
# s1 = s.split(',')
# L = [int(x) for x in s1]
# print(L)

# 9.生成前40个斐波那契数(Fibonacci)
#     1 1 2 3 5 8 13....
#     要求将这些数保存在列表中
#     打印这些数

# f0 = 1
# f1 = 1
# c = [f0, f1]
# for i in range(1, 40):
#     f0, f1 = f1, f0 + f1
#
#     if len(c) < 40:
#         c.append(f1)
# print(c)

# 例如写法二
# a = 0   #当前数的前一位
# b = 1   #当前数
# L = []
# while len(L) < 40:
#     #此处拿到斐波那契数数，放入列表中
#     # L.append(b)
#     # a, b = b, a + b #序列赋值
#     # c = a + b
#     # a = b
#     # b = c

#或者
# L = [1, 1]
# while len(L) < 40:
#     L.append(L[-1] + L[-2])
# print(L)


# 10.有一些数存于列表中:L = [1, 3, 2, 1, 6, 4, 2,....98, 82]
#     将列表中出现的数字存入到另一个列表L2中
#     要求：重复出现多次的数字在L2列表中只保留一份（去重复）

# res = []
# for each in num:
#     if each not in res:
#         res.append(each)
#
# print(res)

# L = []
# while True:
#     s = input("请输入:")
#     if s == '':
#         break
#     L.append(s)
# print("L1 = ", L)
#
# import copy
# L2 = copy.deepcopy(L)
# L2.sort()
# i = 1
# x = L2[0]
# L3 = [L2[0]]
# while i < len(L2):
#     if x != L2[i]:
#         print(x + '!=' + L2[i])
#         L3.append(L2[i])
#     x = L2[i]
#     i += 1
# print('L3 = ', L3)

# 11.s1 = "Welcome to China"
#     请生成列表 L 为 ['Welocom','to','china']
#     s2 = ['hello', 'tar', 'gz']
#     请生成字符串 S 为 "hello.tar.gz"
# s1 = "Welcome to China"
# L1 = s1.split(' ')
# L = [x for x in L1]
# print(L)
#
# s2 = ['hello', 'tar', 'gz']
# S = '.'.join(s2)
# print(S)


