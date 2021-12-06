# d = {'name': 'zhangsan', 'age': '25'}
#
# d = dict([('name', 'tarena'), ['age', '15']])
#
# print(d['name'])
#
# d = {'name': 'tarena', 'age': 15, (1990, 1, 1): '生日'}
# print(d['name'], '的年龄是:', d['age'], '生日为', d[(1990, 1, 1)])
#
# d = {}
# d['name'] = 'tarena'
# d['age'] = 15
# d['age'] = 16
# # del d['age']
# print(d)

# d = {'name': 'tarena', 'age': 16}
# if 'name' in d:
#     print(d['age'], '在字典中')
#
#     print(16 in d)  #False，只判断键，不判断值

# d = {'name': 'tarena', 'age': 15}
# for k in d:
#     print(k, '对应的值是:', d[k])
#
# for k, v in d.items():
#     print('键:', k, '值:', v)

#生成一个字典，键为数字（10以内），值为键的平方
# d = {x: x**2 for x in range(10)}
# print(d)

#请创建一个字典D为{"name": "Bob", "age": 20}
# D = {"name": "Bob", "age": 20}
# D["score"] = 90
# if D.get("name") == "Bob":
#     D["age"] = 25
# print(D["age"])

# 练习
# 1.写程序，实现以下要求：
#     1)将如下数据形成一个字典seasons:
#         '键'     '值 '
#         1       '春季有1，2，3月'
#         2       '夏季有4，5，6月'
#         3       '秋季有7，8，9月'
#         4       '冬季有10，11，12月'
#     2)用户输入一个整数，代表一个季度，打印这个季度对应的信息，如果用户输入的信息不存在字典内，则打印信息不存在
# seasons = {}
# seasons[1] = '春季有1，2，3月'
# seasons[2] = '夏季有4，5，6月'
# seasons[3] = '秋季有7，8，9月'
# seasons[4] = '冬季有10，11，12月'
#
# d = int(input("请输入一个整数:"))
# if d in seasons:
#     print('您输入的处于:', seasons[d])
# else:
#     print("信息不存在")

# 2.输入一段字符串，打印出这个字符串中出现的次数
# 如
#     输入：
#         abcdabcaba
#     打印：
#         a: 4次
#         b: 3次
#         c: 2次
#         d: 1次
# s = input("输入:")
# d ={}
# for i in s:
#     # if i not in d:
#     #     k = i
#     #     v = s.count(k)
#     #     d[k] = v
#     #第二种写法
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1
# for k, v in d.items():
#     print(k, ':', v, '次')

# 3.有字符串的列表如下:
# L = ['tarena','xiaozhang','tyke']
# 用上述列表生成如下字典
# d = {'tarena': 6, 'xiaozhang': 9, 'tyke': 4}
# 注：
#     字典的值为键的长度

# L = ['tarena', 'xiaozhang', 'tyke']
#推导式写法
# D = {x: len(x) for x in L}
# print(D)
#
# 写法二
# d = {}
# for i in L:
#     d[i] = len(i)
# print(d)

# 4.已知有两个等长的列表 list1 和 list2
#     以list1中的元素为键，以list2中的元素为值，生成相应的字典
#     list1 = [1001, 1002, 1003, 1004]
#     list2 = ['Tom', 'Jerry', 'Spike', 'tyke']
#     生成字典为：
#     {1001: 'Tom',1002: 'Jerry'}
# list1 = [1001, 1002, 1003, 1004]
# list2 = ['Tom', 'Jerry', 'Spike', 'tyke']
# list3 = {}
# i = 0
# 方法一
# while i < len(list1):
#     list3[list1[i]] = list2[i]
#     i += 1
# print(list3)

# 方法二
# for i in range(len(list1)):
#     list3[list1[i]] = list2[i]
# print(list3)

# 字典推导式
# L = {list1[i]: list2[i] for i in range(len(list1))}
# print(L)

# 优化打印
# for k, v in list3.items():
#     print('id:', k,
#           #换行输出
#           '\nname:', v)

# 5.输入任意个学生的姓名，年龄，成绩，每个学生的信息存入字典中，然后放入至列表中，每个学生的信息需要手动输入
#     当输入姓名为空时结束输入：
#     如：
#     请输入姓名: zhangsan
#     请输入年龄: 20
#     请输入成绩: 100
#
#     请输入姓名: lisi
#     请输入年龄: 19
#     请输入成绩: 98
#
#     请输入姓名: 空    -->>结束

# 要求内部存储格式如下:
#     [{'name': 'zhangsan', 'age': '20', 'score': 100},
#      {'name': 'lisi', 'age': '19', 'score': 98},
#      ]

# 打印所有学生的信息如下:
#     +--------------+------------+------------+
#     |    name      |    age     |   score    |
#     +--------------+------------+------------+
#     |   zhangsan   |    20      |    100     |
#     |    lisi      |    19      |    98      |
#     +--------------+------------+------------+

# 输入框
#     请输入姓名: zhangsan
#     请输入年龄: 20
#     请输入成绩: 100

# list = []
# name_len = 0
# age_len = 0
# score_len = 0
# while True:
#     names = input("请输入姓名:")
#     if names == '':
#         break
#     if len(names) > name_len:
#         name_len = len(names)
#
#     age = int(input("请输入年龄:"))
#     if len(str(age)) > age_len:
#         age_len = len(str(age))
#
#     score = int(input("请输入成绩:"))
#     if len(str(score)) > score_len:
#         score_len = len(str(score))

# 存储方式
# 要求内部存储格式如下:
#     [{'name': 'zhangsan', 'age': '20', 'score': 100},
#      {'name': 'lisi', 'age': '19', 'score': 98},
#      ]

#     #存入字典
#     data = {}
#     data['name'] = names
#     data['age'] = age
#     data['score'] = score
#
#     #存入列表
#     list.append(data)
# print(list)
# print(name_len)

# 显示方式
# 打印所有学生的信息如下:
#     +--------------+------------+------------+
#     |    name      |    age     |   score    |
#     +--------------+------------+------------+
#     |   zhangsan   |    20      |    100     |
#     |    lisi      |    19      |    98      |
#     +--------------+------------+------------+
#
list = [{'name': 'lianyuxue', 'age': 20, 'score': 100}, {'name': 'sunhaitao', 'age': 30, 'score': 99}, {'name': 'yangjianhuai', 'age': 23, 'score': 98}]
name_len = 12
age_len = 3
score_len = 2

#根据name长度居中
print('+' + '-' * (name_len + 2) + '+' + '-' * 5 + '+' + '-' * 7 + '+')
print('|' + 'name'.center(name_len + 2) + '|' + 'age'.center(5) + '|' + 'score'.center(7) + '|')
print('+' + '-' * (name_len + 2) + '+' + '-' * 5 + '+' + '-' * 7 + '+')
# 循环取出列表中每一个元素
for i in list:
    print('|' + i.get('name').center(name_len + 2) + '|' + str(i.get('age')).center(5) + '|' + str(i.get('score')).center(7) + '|')
print('+' + '-' * (name_len + 2) + '+' + '-' * 5 + '+' + '-' * 7 + '+')


#方法二
# for d in list:
#     n = d['name'].center(15)
#     a = str(d['age']).center(10)
#     s = str(d['score']).center(10)
#     print("|%s|%s|%s|" % (n, a, s))



# 循环取出列表中每一个元素
# i = 0
# while i < len(list):
#     # 获取元素中key['name']对应的值
#     name_values = list[i].get('name')
#
#     # 取name长度最大，用于表格居中
#     name_len.append(len(name_values))
#
#     # 获取元素中key['age']对应的值
#     age_values = list[i].get('age')
#
#     # 获取元素中key['score']对应的值
#     score_values = list[i].get('score')
#     print(name_values, age_values, score_values)
#     i += 1







