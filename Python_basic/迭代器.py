# def get_list(it):
#     datait = iter(it)
#     while True:
#         try:
#             x = next(datait)
#             print(x)
#         except StopIteration:
#             break
#
# L = [x for x in range(10)]
# get_list(L)

# 练习
# 有一个集合
# xiyou = {'唐僧', '悟空', '八戒', '沙僧'}
# 用for语句来遍历所有元素:
#     for x in xiyou:
#         print(x)
#     else:
#         print("遍历结束")
# 请将上面的for语句改写为while语句机迭代器实现

def get_list(list):
    datait = iter(list)
    while True:
        try:
            x = next(datait)
            print(x)
        except StopIteration:
            print("遍历结束")
            break

# xiyou = {'唐僧', '悟空', '八戒', '沙僧'}
# get_list(xiyou)


# 练习
# lst = [1, [2, 3], [4, 5, 6, [7, 8, 9, 10]]]

# def type_list(n):
#     for i in n:
#         if isinstance(i, list):
#             print(i)
#             type_list(i)

# type_list(lst)

lst = [3, 5, 8]

# def my(n):
#     cont = 1
#     def my_list(index):
#         print('_________________')
#         print('index = ', index)
#         print('_________________')
#         print('进入判断')
#         if index == len(n):
#             nonlocal cont
#             # cont += 1
#             # print(index, len(n))
#             # lst = [3, 5, 8]
#             print('第', cont, '次', n)
#             cont += 1
#             print('|_________________|')
#             print()
#         #     #             0       2
#         #     #             1       2
#         #     #             2       2
#         print('进入循环')
#         print('前for 循环index = ', index, 'len(n)=', len(n))
#         for i in range(index, len(n)):
#             # 3, 5, 8
#             print('后for 循环index = ', index, 'len(n)=', len(n))
#             print('i = ', i)
#
#             print('for 循环**********************')
#             print('for 循环n[index], n[i]', n[index], n[i], '--->>>n[i], n[index]', n[i], n[index])
#             n[index], n[i] = n[i], n[index]
#             # 第一次 3，3 = 3， 3
#             # 第二次 5，5 = 5， 5
#             # 第三次 8，8 = 8， 8
#
#             print('调用my_list', index, my_list(index + 1))
#             print(index, '+', 1, '=', index + 1)
#             # print('调用my_list(index + 1), index=', index, 'index + 1=', index + 1, my_list(index + 1))
#             # n[index], n[i] = n[i], n[index]
#     print('调用my_list')
#     ret = my_list(0)
#     # # return ret
#
#
#
# my(lst)
# [print(x) for x in my(lst)]



