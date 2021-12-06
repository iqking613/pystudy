# x = int(input("请输入矩形宽度:"))
# print("#" * x)
# s = "#" + " " * (x - 2) + "#"
# print(s)
# print(s)
# print("#" * x)
#

# x = input("请输入一个字符串:")
#
# print("第一个字符串为:", x[0], "最后一个字符串为:", x[-1])
#
# if len(x) % 2 == 1:
#     print(len(x), "当前为奇数")
#     y = len(x) // 2
#     print("中间的字符为:", x[y])
# else:
#     print(len(x), "当前为偶数")

# x = input("请输入一个字符串:")
#
# s = x[1:-1]
# print("去掉前后字符串为:", s)
#
# if x == x[::-1]:
#     print("回文数")
# else:
#     print("不是回文数")


# x = str(input("请输入字符串:"))
#
# if x != '':           #或者if len(x) != 0:
#     l = x[0]
#     print(ord(l))
# else:

#     print("字符串为空")
#
# x = int(input("请输入整数值（0~65535）:"))
# if x < 65535:
#     print(chr(x))
# else:
#     print("该值大于65535")

#输入三行文字，让这三行文字依次以20给字符的宽度右对齐输出
S1 = input("请输入第1行:")
S2 = input("请输入第2行:")
S3 = input("请输入第3行:")
# S4 = len(S1)
# print("%20s" % S1)
# print("%20s" % S2)
# print("%20s" % S3)

#最长字符串长度进行右对齐
# 方法一
# if len(S2) > S4:
#     S4 = len(S2)
# if len(S3) > S4:
#     S4 = len(S3)
# print("最长的字符串长度为", S4)
# print(' ' * (S4 - len(S1)) + S1)
# print(' ' * (S4 - len(S2)) + S2)
# print(' ' * (S4 - len(S3)) + S3)

# 方法二
S4 = max(len(S1), len(S2), len(S3))
fmt = '%' + str(S4) + 's'   #'%%%ds' % S4
print(fmt)
print(fmt % S1)
print(fmt % S2)
print(fmt % S3)

