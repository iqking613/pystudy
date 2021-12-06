# 此示例示意try-except语句的用法
# def div_apple(n):
#     print("%d个苹果您想分给几个人?" % n)
#     s = input("请输入人数: ")
#     cnt = int(s)    # <-- 此处可能触发ValueError类型错误
#     result = n / cnt    # <-- 此处可能触发ZeroDivisionError类型错误
#     print("每个人分了%d个苹果" % result)
# try:
#     div_apple(10)   # 此函数可能会触发错误，分苹果失败
# except ValueError as e:
#     print("分苹果失败: 程序已捕获ValueError错误通知并转为正常状态")
#     print("错误类型的值是: ", e)
# except ZeroDivisionError:
#     print("分苹果失败: 程序已捕获ZeroDivisionError错误通知并转为正常状态")
# except:
#     print("其他类型的错误已捕获")
#
# print("程序正常退出")

# 此示例示意try-except-else语句的用法
# def div_apple(n):
#     print("%d个苹果您想分给几个人?" % n)
#     s = input("请输入人数: ")
#     cnt = int(s)    # <-- 此处可能触发ValueError类型错误
#     result = n / cnt    # <-- 此处可能触发ZeroDivisionError类型错误
#     print("每个人分了%d个苹果" % result)
# try:
#     div_apple(10)   # 此函数可能会触发错误，分苹果失败
# except ValueError as e:
#     print("分苹果失败: 程序已捕获ValueError错误通知并转为正常状态")
#     print("错误类型的值是: ", e)
# except ZeroDivisionError:
#     print("分苹果失败: 程序已捕获ZeroDivisionError错误通知并转为正常状态")
# except:
#     print("其他类型的错误已捕获")
# else:
#     print("苹果分完，程序没有发生异常")
#
# print("程序正常退出")

# 此示例示意try-except-else-finally语句的用法
# def div_apple(n):
#     print("%d个苹果您想分给几个人?" % n)
#     s = input("请输入人数: ")
#     cnt = int(s)    # <-- 此处可能触发ValueError类型错误
#     result = n / cnt    # <-- 此处可能触发ZeroDivisionError类型错误
#     print("每个人分了%d个苹果" % result)
# try:
#     div_apple(10)   # 此函数可能会触发错误，分苹果失败
# except ValueError as e:
#     print("分苹果失败: 程序已捕获ValueError错误通知并转为正常状态")
#     print("错误类型的值是: ", e)
# except ZeroDivisionError:
#     print("分苹果失败: 程序已捕获ZeroDivisionError错误通知并转为正常状态")
# except:
#     print("其他类型的错误已捕获")
# else:
#     print("苹果分完，程序没有发生异常")
# finally:
#     print("我是最后的，都要执行")
# print("程序正常退出")

# 此示例示意try-finally语句的用法
# def fry_egg():
#     try:
#         print("打开天然气....")
#         try:
#             count = int(input("请输入鸡蛋个数:"))
#             print("共煎了%d个鸡蛋" % count)
#         finally:
#             print("关闭天然气")
#     except:
#         pass
# fry_egg()

# 此示例示意用raise语句来触发异常
# def make_exception():
#     print("begin")
#
#     # 触发ValueError类型的异常进入异常状态
#     # raise ValueError  # 定义异常类型
#
#     err = ValueError("这是我自己定义的一个错误")
#     raise err
#
#     print("end")
# try:
#     make_exception()
#     print("make_exception调用结束")
# except ValueError as e:
#     print("try里出现了值错误通知，已捕获！！！")
#     print("接收的异常通知为:", e)

# 此示例示意用assert语句来触发异常
# def get_score():
#     s = int(input("请输入学生成绩:"))
#     # 用assert语句来断言s是否在0~100之间
#     assert 0 <= s <= 100, "用户输入的整数不在0~100之间"
#     return s
#
# try:
#     score = get_score()
#     print("学生成绩为:", score)
# except ValueError:
#     print("用户输入的成绩无法转换为整数")
# except AssertionError as err:
#     print("发生了断言错误，原因是:", err)

# 练习
# 1.写一个函数:
#     def get_score():
#         ....
#     此函数来获取用户输入的学生成绩信息（0~100的整数）
#     如果用户输入出现异常则此函数返回0，否则返回用户输入的成绩
#     score = get_score()
#     print("您输入的成绩：", score)
# def get_score():
#     n = input("请输入(0~100)成绩:")
#     try:
#         score = int(n)
#     except ValueError:
#         return 0
#
#     if 0 <= score <= 100:
#         return score
#     else:
#         return 0
#
# score = get_score()
# print("您输入的成绩: ", score)

# 2.写一个函数get_age()用来获取一个人的年龄信息
# 此函数规则只能够输入1~140之间的整数，如果用户输入其它的数则触发ValueError类型的错误！
# def get_age():
#     s = input("请输入(1~140)年龄:")
#     age = int(s)
#     if 0 < age < 140:
#         return age
#     raise ValueError("您输入的不在1~140之间")

# try:
#     age = get_age()
#     print("用户输入的年龄是%d" % age)
# except ValueError as err:
#     print("用户输入的不是1~140的整数！！！ 获取失败")

# 3.一个球从100米高空落下，每次落地后反弹高度为原高度的一半，再落下
#     写程序
#     1)算出皮球在第10次落地后反弹多高
#     2)打印出皮球经历了多少米路程

# 方法一
# def ball(height, times):
#     for i in range(times):
#         height /= 2
#     return height
# print(ball(100,10))

# def get_distance(height, times):
#     m = 0
#     for _ in range(times):
#         m += height + height / 2
#         height /= 2
#     return m
# print(get_distance(100, 10))

# 方法二
# def ball(height,times):
#     if times == 0:
#         return 100
#     return ball(height, times - 1) / 2
# print(ball(100, 10))

# print("皮球在第10次落地后反弹高度为:", hi[0])
# print("皮球经历了%f米路程" % hi[1])

# 4.分解质因数，输入一个正整数，分解质因数
#     如输入:90则打印:
#     90 = 2*3*3*5
#     (质因数是指最小能被原数整除的素数(不包含1))

# 方法一
# 判断是否为素数
def Prime(i):
    if i < 2:
        return False
    for x in range(2, i):
        if i % x == 0:
            return False
    return True

L = []
def get_yinshu_list(L, s):
    '''
        循环实现
    '''
    # 用来存放所有的质因数
    # L = []
    # x = s   # x代表未分解的质因数
    # while not Prime(x):     # 当x不是素数时开始循环
    #     for i in range(2, x):
    #         print("%d %% %d == %d" % (x, i, x % i))
    #         if x % i == 0 and Prime(i):  # 已经被整除，i是质因数
    #             L.append(i)
    #             print("%d / %d == %d" % (x, i, x / i))
    #             x = int(x / i)
    #             break
    # L.append(x)
    # return L

    '''
        递归方式
    '''
    x = s
    if Prime(x):
        L.append(x)
        return L
    for i in range(2, x):
        if x % i == 0:
            L.append(i)
            x = int(x / i)
            break
    return get_yinshu_list(L, x)

s = int(input("请输入一个正整数:"))

# zys = get_yinshu_list(L, s)
# S = ' * '.join([str(x) for x in zys])
# print(s, '=', S)


# 5.写程序打印杨辉三角(只打印6层)
#             1
#           1   1
#         1   2   1
#       1   3   3   1
#      1  4   6   4    1
#     1  5  10   10  5   1
def get_yanghui_list(n):    # n代表层数
    '''此函数用于返回每一层的列表的列表'''
    layers = []     # 用于存储每一行的数据
    L = [1]
    for _ in range(n):  # 循环，每次加入layers中每一行
        layers.append(L)    # 先第一行加入
        # 算出下一行，再用L重新绑定
        one_line = [1]  # 最左边的1
        # 算出中间的数字
        for i in range(len(L) - 1):
            one_line.append(L[i] + L[i + 1])
        one_line.append(1)  # 加入最右边的1
        L = one_line    # 让L绑定新算出的一行
    return layers
print(get_yanghui_list(6))

# [1]
# [1,1]
# [1,2,1]
# [1,3,3,1]

# def triangles():
#     p = [1]
#     while True:
#         yield p#generator函数与普通函数的差别：在执行过程中，遇到yield就中断，下次又继续执行
#         p = [1] + [p[i] + p[i+1] for i in range(len(p)-1)] + [1]
# n = 0
# for t in triangles():
#     print(t)
#     n = n + 1
#     if n == 10:
#         break