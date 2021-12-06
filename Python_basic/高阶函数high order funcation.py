
# map函数示例示意说明
# 生成一个可迭代对象，此可迭代对象生成1~9的自然数的平方
# def power2(x):
#     return x ** 2
# for x in map(power2, range(1, 10)):
#     print(x)

# 生成一个可迭代对象，此可迭代对象生成的如下
# 1**5 2**6 3**7 4**8 5**9
# L1 = [1, 2, 3, 4]
# L2 = [5, 6, 7, 8]
# def power_x_y(x, y):
#     return x ** y
#
# for i in map(power_x_y, L1, L2):
#     print(i)

# filter函数示例示意说明
# def isodd(x):
#     return x % 2 == 1
# for i in filter(isodd, range(41, 53)):
#     print(i)

# sorted函数示例示意说明
# L = [5, -2, -4, 0, 3, 1]
# L2 = sorted(L)
# print(L2)
#
# L3 = sorted(L, key=abs)
# print(L3)
# # [0, 1, -2, 3, -4, 5]
#
# names = ['Tom', 'Tyke', 'Jerry', 'Spike']
# L4 = sorted(names, key=len)
# print(L4)

# names = ['Tom', 'Jerry', 'Spike', 'Tyke']
# def get_key(n):
#     '''
#     n用来绑定参数中每个元素，n绑定名字（字符串）
#     此函数需要返回一个能比较大小的依据
#     '''
#     return n[::-1]
#
# L5 = sorted(names, key=get_key)
# L6 = sorted(names, key=lambda a: a[::-1])
# print(L5)
# print(L6)

# 递归函数示例示意说明
# 超过1000条报错
# def fn(n):
#     print("递归进入第", n, '层')
#     if n == 3:  # 当递归进入第三层时，将不再向下走，开始回归
#         return
#     fn(n + 1)
#     print("递归退出第", n, '层')
# fn(1)
# print("程序结束")
# 递归进入第 1 层
# 递归进入第 2 层
# 递归进入第 3 层
# 递归退出第 2 层
# 递归退出第 1 层
# 程序结束

# 闭包函数示例示意说明
# 写一个函数，让此函数能通过调用参数y就能够生成x的y次方函数
# def make_power(y):
#     def fn(x):
#         return x ** y
#     return fn
# power1 = make_power(2)
# print("5的平方", power1(5))

# 闭包来创建任意
# f(x) = a*x**2 + b*x**1 + c函数
# def get_fx(a, b, c):
#     def fx(x):
#         return a*x**2 + b*x**1 + c
#     return fx
# f123 = get_fx(1, 2, 3)
# print(f123(20))

# 装饰器函数示例示意说明
# 示例一
def mydeco(fn):
    def fx():
        print("fx函数被调用")
    return fx

# myfunc加了mydeco装饰器，等同于在myfunc创建之后调用myfunc = fydeco(myfunc)
@mydeco
def myfunc():
    print("函数myfunc被调用")

# myfunc = mydeco(myfunc)   # 写法可以用装饰器代替  等同于  @mydeco
# myfunc()

# 示例二
def mydeco(fn):
    def fx():
        print("-------myfunc调用之前-------")
        fn()    # 调用被装饰函数
        print("-------myfunc调用之后-------")
    return fx

@mydeco
def myfunc():
    print("函数myfunc被调用")

# myfunc()

# 此示例示意装饰器在不改变原函数和调用者行为情况下 来改变原有函数

# 写一个操作数据的函数（此函数用来示意存钱操作）

def send_massage(fn):
    def fx(name, x):
        fn(name, x)     # 先调用办理
        print("尊敬的", name, ": 您取出", x, "元")
    return fx
def privillage_check(fn):
    def fx(name, x):
        print("正在权限验证......")
        fn(name, x)
    return fx

@privillage_check

def savemoney(name, x):
    print(name, "存钱", x, "元")

@send_massage
@privillage_check
def withdraw(name, x):
    print(name, "取钱", x, "元")

print("---------调用者------------")
savemoney("小张", 200)
print()
withdraw("小李", 300)

# 练习
# 1.求1**2 + 2**2 + 3**2 +...9**2的和
# 用函数式和高阶函数map实现
# def L1(x):
#     return x ** 2
# print(sum(map(lambda x: x**2, range(1, 10))))

# 2.求1**3 + 2**3 + 3**3 + ...9**3的和
# def L2(x):
#     return x ** 3
# print(sum(map(lambda x: x**3, range(1, 10))))

# 3.求1**9 + 2**8 + 3**7...+9**1的和
# print(sum(map(pow, range(1, 10), range(9, 0, -1))))

# 4.把之前写的is_prime(x)
# 判断x是否为素数的函数复制过来
# def is_prime(x):
#     if x > 1:
#         for i in range(2, x):
#             if x % i == 0:
#                 return False
#         else:
#             return True
#     else:
#         return False
# 1.用filter函数，把100到200的全部素数求出来，放入列表L中
# L = list(filter(is_prime, range(100, 201)))
# print(L)

# 2.求300 ~ 400之间全部素数的和
# print(sum(filter(is_prime, range(300, 401))))

# 5.写一个函数求n的阶乘（递归实现）
    # 1*2*3*4*5
    # 等同于
    # 5*4*3*2*1
    # 5! = 5 * 4!
    # 4! = 4 * 3!
    # 3! = 3 * 2!
    # 2! = 2 * 1!

    # 回归
    # 5! = 5 * 4 * 3 * 2
    # 5! = 5 * 4 * 6
    # 5! = 5 * 24
    # 5! = 120
def myfac(n):
    if n == 1:
        return 1
    print(n, '*', n - 1)
    return n * myfac(n - 1)
print("5的阶层是:", myfac(5))

# 6.写一个函数mysum（n）,用递归方法求
# 1+2+3+4...+n的和
# # def mysum(n):
# #     if n == 1:
# #         return 1
# #     print(n, '+', n - 1)
# #     return n + mysum(n - 1)
# #
# # print(mysum(100))

# 7.已知
#     第五个人比第四个人大2岁
#     第四个人比第三个人大2岁
#     第三个人比第二个人大2岁
#     第二个人比第一个人大2岁
#     第一个人说他10岁
#
#     编写程序算出第5个人几岁？
#     (可以使用递归和循环实现)
# def score(n):
#     if n == 1:
#         return 10
#     return score(n - 1) + 2
# print(score(5))
# print(score(5))

# 8.已知有列表
#     L = [[3, 5, 8], [[13, 14], 15, 18], 20]
#
#     1).写一个函数print_list(lst)打印出列表内的所有元素
#         print_list(L) = 3, 5, 8, 10, 13, 14....
#     2).写一个函数sum_list(L) #96
#     注:
#         type(x) 可以返回一个变量的类型
#     如:
#         >>>type(20) is int #True
#         >>>type([3, 5, 8]) is list #True
# L = [[3, 5, 8], [[13, 14], 15, 18], 20]
# def print_list(lst):
#     for i in lst:
#         if type(i) is list:
#             print_list(i)   # 递归处理内部的列表
#         elif type(i) is int:
#             print(i, end=' ')
# print_list(L)
# print()

# def sum_list(lst):
#     s = 0       # 累加lst中的所有数字和
#     for i in lst:
#         if type(i) is int:
#             s += i
#         else:
#             s += sum_list(i)
#     return s
# print(sum_list(L))

# 9.改写之前的学生信息管理程序
#     要求添加四个功能:
#         |5) 按学生成绩高-低显示学生信息 |
#         |6) 按学生成绩低-高显示学生信息 |
#         |7) 按学生年龄高-低显示学生信息 |
#         |8) 按学生年龄低-高显示学生信息 |

# 1)添加学生信息
def input_student():
    list = []
    while True:
        # 录入信息
        name = input("请输入姓名:")
        if name == '':
            break
        age = int(input("请输入年龄:") or 0)
        score = int(input("请输入成绩:") or 0)

        # 每组以字典方式存入
        d = {}
        d['name'] = name
        d['age'] = age
        d['score'] = score

        # 每组字典存入列表中
        list.append(d)
    return list

# 2)显示学生信息
def output_student(lst):
    # 获取name键最大长度
    name_len = 2
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
            print('|' + i.get('name').center(name_len + 2) + '|' + str(i.get('age')).center(5) + '|' + str(i.get('score')).center(7) + '|')

    print('+' + '-' * (name_len + 2) + '+' + '-' * 5 + '+' + '-' * 7 + '+')

# 3)删除学生信息
def delete_student(data):
    s = input("请输入删除的学生姓名: ")
    for i in data:
        if i['name'] == s:
            data.pop(data.index(i))
            print(s, "删除成功!")
            break
    else:
        print("无此学生信息")

# 4)修改学生成绩
def update_student_score(data):
    s = input("请输入要修改的学生姓名: ")
    for i in data:
        if i['name'] == s:
            update = int(input("请输入修改后的成绩: "))
            i['score'] = update
            print(s, "成绩修改成功!")
            break
    else:
        print("无此学生信息")

# 5) 按学生成绩高-低显示学生信息
def drop_score_student(data):
    def key_drop(n):
        return n['score']
    output_student(sorted(data, key=key_drop, reverse=True))

# 6) 按学生成绩低-高显示学生信息
def rise_score_student(data):
    def key_drop(n):
        return n['score']
    output_student(sorted(data, key=key_drop))

# 7) 按学生年龄高-低显示学生信息
def drop_age_student(data):
    def key_drop(n):
        return n['age']
    output_student(sorted(data, key=key_drop, reverse=True))

# 8) 按学生年龄低-高显示学生信息
def rise_age_student(data):
    def key_drop(n):
        return n['age']
    output_student(sorted(data, key=key_drop))

def show_menu():
    print("+" + "----------------------------" + "+")
    print("|" + "1)添加学生信息               " + "|")
    print("|" + "2)显示学生信息               " + "|")
    print("|" + "3)删除学生信息               " + "|")
    print("|" + "4)修改学生成绩               " + "|")
    print("|" + "5)按学生成绩高-低显示学生信息 " + "|")
    print("|" + "6)按学生成绩低-高显示学生信息 " + "|")
    print("|" + "7)按学生年龄高-低显示学生信息 " + "|")
    print("|" + "8)按学生年龄低-高显示学生信息 " + "|")
    print("|" + "q)退出程序                   " + "|")
    print("+" + "----------------------------" + "+")


def main():
    datas = []
    while True:
        show_menu()
        Choice = input("请选择:")
        if Choice == "1":
            datas += input_student()
        if Choice == "2":
            output_student(datas)
        if Choice == "3":
            delete_student(datas)
        if Choice == "4":
            update_student_score(datas)
        if Choice == "5":
            drop_score_student(datas)
        if Choice == "6":
            rise_score_student(datas)
        if Choice == "7":
            drop_age_student(datas)
        if Choice == "8":
            rise_age_student(datas)
        if Choice == "q":
            break
# main()


