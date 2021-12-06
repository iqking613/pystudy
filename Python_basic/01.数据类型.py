# x = input("请输入x:")
# x = int(x)
# y = input("请输入y:")
# y = int(y)
#
# print(x, "+", y, "=", x + y)
# print(x, "*", y, "=", x * y)
# print(x, "**", y, "=", x ** y)
#
# print(int(20 * 365 / 7))
# print(20 * 365 % 7)

# hour = int(input("请输入小时:"))
#
# minute = int(input("请输入分钟:"))
#
# second = int(input("请输入秒:"))
#
# s = hour * 60 * 60 + minute * 60 + second
# print('从凌晨到现在经历了', s, '秒')

# n = int(input("请输入一个数字:"))
# 方法一
# if n < 0:
#     a = -n
#     print(n)
# else:
#     a = n

# 方法二
# a = n       #先绑定原来的值
# if a < 0:   #如果a为负数，则翻转符合
#     a = -a  #<<翻转符合
# print('绝对值是:', a)

#条件表达式实现
# u = -n if n < 0 else n
# print(u)

#布尔或
# score = int(input('请输入学生成绩:') or '0')   #or '0' 定义默认值
# print("score = ", score)

# 练习一
# liang = 216
#
# jin = 216 // 16
# l = 216 % 16
# print("斤", jin, "两", l)

# 练习二
# m = 63320
# s = m // 60 // 60
# f = m // 60 % 60
# m = m % 60
# print(s, "时", f, "分", m, "秒")

# 练习三
# f = 100
# c = 5.0 / 9.0 * (f - 32)
# print("摄氏温度", c)

# 练习四
# 一
# km = int(input("请输入公里数:"))
# money = 0
# if km >= 1:
#     if km <= 3:
#         money = 13
#         print("金额:", money)
#     elif 3 < km <= 15:
#         money = 13 + 2.3 * (km - 3)
#         print("金额:", round(money))
#     elif 15 < km:
#         money = 13 + 2.3 * (km - 3) + 2.3 * 0.5 * (km - 15)
#         print("金额", round(money))
# else:
#     print("您输入的格式有误")
# 二
# money = 0
# if 0 <= km <= 3:
#     money = 13
# elif 3 < km <= 15:
#     money = 13 + 2.3 * (km - 3)
# else:
#     money = 13 + 2.3 * (km - 3) + 2.3 * 0.5 * (km - 15)
#
# print("金额为:", round(money))

# 三
# money = 13
# if km > 3:
#     money += 2.3 * (km - 3)
# if km > 15:
#     money += 2.3 * 0.5 * (km - 15)
# print("金额为:", round(money))

# 练习五
# a = int(input("请输入语文分数:"))
# b = int(input("请输入数学分数:"))
# c = int(input("请输入英语分数:"))

# zuida = a
# if b > zuida:
#     zuida = b
#
# if c > zuida:
#     zuida = c
# print("最高分是:", zuida)

# zuixiao = a
# if b < zuixiao:
#     zuixiao = b
# if c < zuixiao:
#     zuixiao = c
# print("最小分是:", zuixiao)

# print("平均分是:", round((a + b + c) / 3))

# 练习六
# sg = int(input("请输入您的身高:"))
# tz = int(input("请输入您的体重:"))
#
# if tz >= 1 and sg >= 1:
#     bmi = round(tz / (sg / 100) ** 2, 2)
#     print(bmi)
#     if bmi < 18.5:
#         print("体重过轻")
#     elif 18.5 <= bmi < 24:
#         print("体重正常")
#     else:
#         print("体重过重")
# else:
#     print("您输入的格式有误")

# 练习七
#输入一个字符串用变量S绑定
    # 1.判断输入的字符串有几个空格
    # 2.将原字符串的左右空白字符去掉，打印出剩余的字符个数
    # 3.判断输入的是否是数字
    # 4.如果是数字，判断这个数字是否大于100
# S = str(input("请输入一个字符串:"))
# print('输入的字符串中空格占:', S.count(' '))
# St = S.strip()
# print('去除空格后剩余字符:', St.count('', 1))
# print('去除空格后剩余字符:', len(St))
# if St.isdigit():
#     if St >= '100':
#         print('大于100')


#输入三行文字，让这三行文字在一个方框内居中显示
S1 = str(input("请输入一个字符串:"))
S2 = str(input("请输入二个字符串:"))
S3 = str(input("请输入三个字符串:"))

# print('+' + '-' * 22 + '+')
# print('|', S1.center(20), '|')
# print('|', S2.center(20), '|')
# print('|', S3.center(20), '|')
# print('+' + '-' * 22 + '+')

max_length = max(len(S1), len(S2), len(S3))
first_line = '+' + '-' * (max_length + 2) + '+'
print(first_line)
print('|' + S1.center(max_length + 2) + '|')
print('|' + S2.center(max_length + 2) + '|')
print('|' + S3.center(max_length + 2) + '|')
print(first_line)




