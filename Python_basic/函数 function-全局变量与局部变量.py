# 方法一
# L = []
# def input_number():
#     lst = []
#     while True:
#         # input为空时，使用-1值
#         n = int(input("请输入一个正整数:") or '-1')
#         if n < 0:
#             break
#         lst.append(n)
#     return lst
# L += input_number()    #L += input_number()
# print(L)
# print()
# L += input_number()
# print(L)

# 方法二
# L = []
# def input_number():
#     lst = []
#     while True:
#         # input为空时，使用-1值
#         n = int(input("请输入一个正整数:") or '-1')
#         if n < 0:
#             break
#         # 添加输入内容至列表
#         lst.append(n)
#
#     # 对全局变量列表追加
#     L.extend(lst)
#
#
# input_number()
# print(L)
# input_number()
# print(L)

# 此示例示意globals()函数和locals函数的用法
# a = 1
# b = 2
# c = 3
# def fx(c, d):
#     e = 300
#     # 此次有几个局部变量
#     print('locals()返回', locals())
#     print('globals()返回', globals())
# fx(100, 200)

# 函数名是变量，在创建时绑定一个函数
# def f1():
#     print("hello f1")
# def f2():
#     print("hello f2")
# fx = f1
# fx()

# 一个函数可以作为另一个函数实参传递
# def f1():
#     print("f1被调用")
# def f2():
#     print("f2被调用")
# def fx(fn):
#     print("fn绑定的是", fn)
#     fn()    # 调用fn绑定的函数，此处调用谁看调用者传过来的函数？
# fx(f1)
# fx(f2)

# def myinput(fn):
#     L = []
#     while True:
#         i = int(input("请输入数字:") or '-1')
#         if i < 0:
#             break
#         L.append(i)
#     return fn(L)
# print(myinput(max))

# 此示例示意get_op这个函数可以返回其他的函数
# def get_op():
#     s = input("请输入您要做的操作:")
#     if s == "求最大":
#         return max
#     elif s == "求最小":
#         return min
#     elif s == "求和":
#         return sum
# L = [1,2,3,4]
# fx = get_op()
# print(fx(L))

# 此示例示意函数内部来嵌套定义其他函数
# def fun_outer():
#     print("fun_outer被调用")
#     # 在此处创建另一个函数，并在下面调用
#     def fun_inner():
#         print("fun_inner被调用")
#     fun_inner()     # 调用一次
#     fun_inner()     # 调用二次
#
#     print("fun_outer调用结束")
# fun_outer()

# 此示例示意python的四个作用域
# v = 100
# def fun1():
#     v = 200
#     print("fun1.v = ", v)
#
# fun1()
# print("全局的v = ", v)

# 此示例示意globals声明
# v = 100
# def fn():
#     global v    # 添加全局声明,告诉解释执行器,函数内的变量v为全局变量
#     v = 200     # 绑定全局变量v
# fn()
# print("v = ", v)
#
# s = "ABC"
# print(id(s))
# def fs():
#     global s
#     s += "123"
# fs()
# print(s)
# print(id(s))

# 此示例示意nonlocal声明
# var = 100
# def f1():
#     var = 200
#     print("f1的var = ", var)
#     def f2():
#         nonlocal var    # 声明var为f2以外,全局变量以内
#         var = 300
#     f2()
#     print("f1调用结束时var = ", var)
# f1()
# print("全局var = ", var)

# 此示例示意用lambda创建匿名函数
# def myadd(a, b):
#     return a + b

# myadd = lambda a, b: a + b  # 表达式
# print("10 + 20 = ", myadd(10, 20))



# 练习
# 1.写一个函数
# def hello(name):
#     (...)
#
# count = 0
# hello("小张")
# hello("小李")
# print("函数hello已经被调用%d次" % count)
# hello("小兆")
# print("函数hello已经被调用%d次" % count)

# def hello(name):
#     global count
#     count += 1
#
# count = 0
# hello("小张")
# hello("小李")
# print("函数hello已经被调用%d次" % count)
# hello("小王")
# print("函数hello已经被调用%d次" % count)

# 2.写一个lamdba表达式，判断这个数的2次方+1是否能被5整除，如果能被正整除返回True,否则返回False
# def myadd(x):
#     if (x ** 2 + 1) % 5 == 0:
#         print("True")
#     else:
#         print("False")
# myadd(4)

# fx = lambda a: (a ** 2 + 1) % 5 == 0
# print(fx(3))
# print(fx(4))

# 3.写一个lambda表达式求两个变量的最大值
# def mymax(a, b):
#     # if a > b:
#     #     return(a)
#     # else:
#     #     return(b)
#
#     # 改写
#     return a if a > b else b
#
# print(mymax(200, 150))

# mymax = lambda a, b: a if a > b else b
# print(mymax(100, 200))

# 4.写一个函数mysum(n),给出一个数n，写一个函数来计算1 + 2 + 3 + 4....+ n的和
# （要求用函数实现）
# def mysum(n):
#     Sum = 0
#     for i in range(1, n + 1):
#         Sum += i
#     return Sum
# print(mysum(5))

# 5.写一个函数myfac来计算n!(n的阶乘)
# n! = 1 * 2 * 3 * 4....* n
# def myfac(y):
#     n = 1
#     for x in range(2, y + 1):
#         n *= x
#     return n
# print(myfac(5))

# 6.给出一个n，写一个函数计算:
# 方法一
# 1 + 2**2 + 3**3 + 4**4 ...+ n**n的和
# def myfun(n):
#     Sum = 1
#     for i in range(2, n + 1):
#         print(Sum, "+", i, "**", i)
#         Sum += i**i
#     return Sum
# print(myfun(5))

# 方法二
# def myfun(n):
#     print(n, "**", n)
#     return n ** n
# Sum = sum(map(myfun, range(1,6)))
# print(Sum)

# 7.修改之前的student_info.py 学生信息管理项目
#     1)为项目添加菜单界面
#     +-----------------------+
#     | 1)添加学生信息         |
#     | 2)显示学生信息         |
#     | 3)删除学生信息         |
#     | 4)修改学生成绩         |
#     | q)退出程序             |
#     +-----------------------+
#     请选择:
#     (要求:每个功能至少对应一个函数)
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

def output_student(lst):
    # 获取name键最大长度
    name_len = 2
    for i in lst:
        v = i.get('name')
        if i != {} and len(v) > name_len:
            name_len = len(v)

    # 打印框
    print('+' + '-' * (name_len + 2) + '+' + '-' * 5 + '+' + '-' * 7 + '+')
    print('|' + 'name'.center(name_len + 2) + '|' + 'age'.center(5) + '|' + 'score'.center(7) + '|')
    print('+' + '-' * (name_len + 2) + '+' + '-' * 5 + '+' + '-' * 7 + '+')

    # 循环取出列表中每一个元素
    for i in lst:
        if i != {}:
            print('|' + i.get('name').center(name_len + 2) + '|' + str(i.get('age')).center(5) + '|' + str(i.get('score')).center(7) + '|')

    print('+' + '-' * (name_len + 2) + '+' + '-' * 5 + '+' + '-' * 7 + '+')

def delete_student(data):
    s = input("请输入删除的学生姓名: ")
    for i in data:
        if i['name'] == s:
            i.clear()
            print(s, "删除成功!")
            break
    else:
        print("无此学生信息")

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

def show_menu():
    print("+" + "-----------------------" + "+")
    print("|" + "1)添加学生信息          " + "|")
    print("|" + "2)显示学生信息          " + "|")
    print("|" + "3)删除学生信息          " + "|")
    print("|" + "4)修改学生成绩          " + "|")
    print("|" + "q)退出程序              " + "|")
    print("+" + "-----------------------" + "+")


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
        if Choice == "q":
            break
# main()

# 晨练题
# a = 100
# b = 200
# s = input("请输入字符串:")
# print(eval(s))  # 300
# print(exec(s))  # None

L1 = [x for x in map(lambda a, b: a + b, [1, 2, 3, 4], [5, 6, 8])]
print(L1)
def fun(n):
    return n % 2 == 1
print([x for x in filter(fun, L1)])
# for x in filter(fun, L1):
#     print(x)


