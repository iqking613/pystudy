# for x in range(5):
#     if x == 2:
#         # print(x)
#         continue
#     print(x)
# 输出
# 0
# 1
# 3
# 4

# for i in range(10):
#     if i % 2 == 1:
#         continue
#     print(i)

# 练习
# 输入一个整数begin绑定
# 在输入一个整数用end绑定
# 打印从begin开始，到end结束内的全部奇数（不包含end）

# begin = int(input("begin:"))
# end = int(input("end:"))
# for语句实现
# for i in range(begin, end):
#     if i % 2 == 0:
#         continue
#     print(i)

# while语句实现
# while begin < end:
#     if begin % 2 == 0:
#         begin += 1
#     print(begin)
#     begin += 1

# 用while循环打印10以内的奇数
# i = 0
# while i < 10:
#     if i % 2 == 0:
#         i += 1
#         continue
#     print(i)
#     i += 1

# 求1~100之间所有不被5，7，11整除的和
# 可以考虑用cmtinue实现
# Sum = 0
# for i in range(1, 100):
#     if i % 5 == 0 or i % 7 == 0 or i % 11 == 0:
#         continue
#     Sum += i
    # if i % 5 == 0:
    #     continue
    # elif i % 7 == 0:
    #     continue
    # elif i % 11 ==0:
    #     continue
    # else:
    #     Sum += i
print(Sum)

Sum1 = 0
i = 1
while i <= 100:
    if i % 5 == 0:
        i += 1
        continue
    elif i % 7 == 0:
        i += 1
        continue
    elif i % 11 == 0:
        i += 1
        continue
    else:
        Sum1 += i
    i += 1

print(Sum1)



