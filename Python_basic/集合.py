# 1.集合练习
# 经理有：曹操，刘备，孙权
# 技术员有：曹操，孙权，张飞，关羽
# 用集合求：
#     1）即是经理，也是技术员的有谁？
#     2）是经理，但不是技术员的人员有谁？
#     3）是技术员，不是经理的有谁？
#     4）张飞是经理吗？
#     5）身兼一职的有谁？
#     6）经理和技术员共有几个人？

# manager = {"曹操", "刘备", "孙权"}
# Technician = {"曹操", "孙权", "张飞", "关羽"}

# 1）即是经理，也是技术员的有谁？
# s1 = manager & Technician
# print(s1)

# 2）是经理，但不是技术员的人员有谁？
# s2 = manager - Technician
# print(s2)

# 3）是技术员，不是经理的有谁？
# s3 = Technician - manager
# print(s3)

# 4）张飞是经理吗？
# s4 = "张飞" in manager
# print(s4)

# 5）身兼一职的有谁？
# s5 = manager ^ Technician
# print(s5)

# 6）经理和技术员共有几个人？
# s6 = manager | Technician
# print(s6)

# 2.任意输入一些数字，存于列表L中，当输入负数时结束输入
#     1)打印这些数的和
#     2）打印这些数有多少种（去重复）
#     3）去除重复的数字后，打印这些剩余数字的和
# L = []
# while True:
#     s = int(input("请输入数字:"))
#     if s < 0:
#         break
#     else:
#         L.append(s)

# 1)打印这些数的和
# print(sum(L))

# 2）打印这些数有多少种（去重复）
# s2 = set(L)
# print(s2)
# print(len(s2))

# 3）去除重复的数字后，打印这些剩余数字的和
# print(sum(s2))

# 3.写一个程序，任意输入一篇英文文章（可能多行），当输入空行时结束输入
#     1)判断出现英文单词的种类数。
L = []
while True:
    s = input("请输入:")
    if s == '':
        break
    L.append(s)

L2 = []
# 替换特殊符合
for x in L:
    x = x.replace(',', '')
    x = x.replace('“', '')
    x = x.replace('’', '')
    x = x.replace('”', '')
    x = x.replace('.', '')
    x = x.replace('—', '')
    for i in '0123456789-':
        x = x.replace(i, '')
    L2.append(x)

# 定义集合
words_set = set()
for i in L2:
    # 字符串切片
    words = i.split()

    # 遍历添加到集合中
    for s in words:
        words_set.add(s)

print("单词个数%d" % len(words_set))









