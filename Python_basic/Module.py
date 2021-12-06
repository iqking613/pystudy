
# 此示例示意__name属性使用
# print("Module模块内的__name__属性绑定", __name__)

# 此示例示意隐藏属性使用
# 以'_'开头的变量名在from xxx  import * 语句导入时将不被导入
def f():
    print("f函数被调用")
def _f():
    print("f函数被调用")
def __f():
    print("f函数被调用")

# 练习
# 1.写一个程序，输入您的出生日期
#     1.算出你已经出生多少天
#     2.算出你出生的那天是星期几
import time, math, random
# s = input("请输入您的出生日期:")
# L = s.split(sep=',')
# week = {
#     0: "星期一",
#     1: "星期二",
#     2: "星期三",
#     3: "星期四",
#     4: "星期五",
#     5: "星期六",
#     6: "星期日"
# }
# age = time.mktime((int(L[0]), int(L[1]), int(L[2]), 0, 0, 0, 0, 0, 0))
# local = time.time()
# print("您的年龄%d岁" % ((local - age) // 60 // 60 // 24 // 365))
# print("您已经出生了", round((local - age) // 60 // 60 // 24), "天")
# print("您出生当天", week[time.localtime(age)[6]])

# 2.写一个程序，以电子时间个数显示时间:
#     HH:MM:SS
def run_clock():
    while True:
        local = time.localtime()
        hms = local[3:6]
        print("%02d:%02d:%02d" % hms)
        time.sleep(1)
# run_clock()
# 3.编写一个闹钟程序，启动时设置定时时间，到时候会打印"时间到"，然后推出
def alarm(hour, minute):
    while True:
        local = time.localtime()
        hms = local[3:5]
        if hms == (hour, minute):
            return print("时间到   ")
        # 倒计时
        # print("剩余:%02d:%02d:%02d" % (hour - hms[0], minute - hms[1] - 1, 59 - local[5]), end='\r')
        print("%02d:%02d:%02d" % local[3:6], end='\r')
        time.sleep(0.5)

# s = int(input("请设定闹钟时:"))
# f = int(input("请设定闹钟分:"))
# alarm(s, f)

# s = int(input("定时时间:"))
# time.sleep(s)
# print("时间到")

# 4.编写函数fun，其功能是求下列多项式的和:
# Sn = 1 + 1/1! + 1/2! + 1/3! + 1/4! + 1/5!.....+ 1/n!
# 建议用数学模块中的math.factorial来求
# 当n为50时,Sn的值

# def func(n):
    # 方法一
    # Sum = 0
    # for i in range(0, n + 1):
    #     Sum += 1 / math.factorial(i)
    # return Sum

    # 方法二
    # return sum(map(lambda x: 1/math.factorial(x), range(n + 1)))

# s = func(50)
# print(s)

# 5.模拟'斗地主'发牌
# 共54张牌
# 花色:
#     黑桃('\u2660')
#     梅花('\u2663')
#     方片('\u2665')
#     红桃('\u2666')
# 大小王
# 数字:
#     A0-10JQK
# 1)生成54张牌
# 2)三个人玩牌，默认发17张，底牌留三张
#     输入回车，打印第一个人的17张牌
#     输入回车，打印第二个人的17张牌
#     输入回车，打印第三个人的17张牌
#     输入回车，打印3张底牌
# 生成扑克方法一
def puke():
    #     黑桃('\u2660')
    #     梅花('\u2663')
    #     方片('\u2665')
    #     红桃('\u2666')
    L = ['大王', '小王']
    for i in range(1, 14):
        if i == 1:
            i = "A"
        elif i == 11:
            i = "J"
        elif i == 12:
            i = "Q"
        elif i == 13:
            i = "K"
        L.append(str(i) + ('\u2660'))
        L.append(str(i) + ('\u2663'))
        L.append(str(i) + ('\u2665'))
        L.append(str(i) + ('\u2666'))
    return L
data = puke()

# 生成扑克方法二
# L = ['A'] + [str(x) for x in range(2, 11)] + list("JQK")
# kinds = [('\u2660'), ('\u2663'), ('\u2665'), ('\u2666')]
# poke = ['大王', '小王']
# for k in kinds:
#     for n in L:
#         poke.append(n + k)
# print(len(poke))

# 方法一
# 需求根据牌型进行排序
def Calculation(L):
    s1 = input("第一个人:")
    if s1 == '':
        s1 = random.sample(L, 17)
        print(s1)
        for i in s1:
            L.remove(i)

    s2 = input("第二个人:")
    if s2 == '':
        s2 = random.sample(L, 17)
        print(s2)
        for i in s2:
            L.remove(i)

    s3 = input("第三个人:")
    if s3 == '':
        s3 = random.sample(L, 17)
        print(s3)
        for i in s3:
            L.remove(i)

    print("底牌", L)
# Calculation(data)

# 方法二
# L = list(data)
# random.shuffle(L)
# print(L)
# print()
# print("第一个人牌型:", L[:17])
# print()
# print("第二个人牌型:", L[17:34])
# print()
# print("第三个人牌型:", L[34:51])
# print()
# print("底牌:", L[51:])

# 6.将学生信息管理程序拆分成相应的模块:
#     建议:
#         main.py         # 放主程序循环
#         menu.py         # 放菜单相应的函数
#         student_info.py # 放学生信息操作相关的函数

# 7.猜数字游戏
#     随机生成一个0~100的整数，用变量x绑定
#     让用户输入一个数，输出才数字的结果
#         1)如果x等于y，则提示“恭喜您猜对了！”，退出程序
#         2)如果y大于x，同提示“您猜大了”
#         3)如果y小于x，同提示“您猜小了”
#     让用户循环输入，直到猜对为止，同时显示用户猜数字的次数后退出程序
def caipiao():
    Sum = 0
    while True:
        x = random.randrange(101)
        s = int(input("请输入一个数: "))
        Sum += 1
        if s == x:
            print("恭喜您猜对了！")
            break
        elif s > x:
            print("您猜大了")
        else:
            print("您猜小了")

    return print("您共猜次数为:", Sum)

# caipiao()

# 晨练题
#     1.写一个函数myfn(n)
#     要求:
#     1)每隔1秒在屏幕打印“hello world” 共打印n次
#     2)请在函数中加入文档字符串：
#     '''
#         myfn函数是输出n遍“hello world”
#         n为参数
#     '''
#     3)优先用递归的方法完成此函数(也可以用while循环)
def myfn(n):
    '''
        myfn函数是输出n遍"hello world"
        n为参数
    '''
    if n == 0:
        return
    print("hello world")
    time.sleep(1)
    return myfn(n - 1)
myfn(5)

print("myfn:__doc__", myfn.__doc__)
a = myfn

# 2.在练习1中的函数外部加入如下语句
print(a.__name__)
print(myfn.__name__)

# 3.在函数中如何调用math模块中的pi变量，请写出语句。
from math import pi


