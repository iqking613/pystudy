import os
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
def desc_score_student(data):
    output_student(sorted(data, key=lambda d: d['score'], reverse=True))

# 6) 按学生成绩低-高显示学生信息
def asc_score_student(data):
    output_student(sorted(data, key=lambda d: d['score']))

# 7) 按学生年龄高-低显示学生信息
def desc_age_student(data):
    output_student(sorted(data, key=lambda d: d['age'], reverse=True))

# 8) 按学生年龄低-高显示学生信息
def asc_age_student(data):
    output_student(sorted(data, key=lambda d: d['age']))

# 9) 保存学生信息到文件(data.txt)
# 数据文件
# [{'name': 'zhagnsan', 'age': 20, 'score': 100}, {'name': 'lisi', 'age': 30, 'score': 99}]
def save_shudent(data):
    try:
        # 默认保存路径
        file = 'data/data_student.txt'

        # 读取文件
        data_read = open(file, 'wb')
        for i in data:
            # 获取键值
            n = i.get('name')
            a = i.get('age')
            s = i.get('score')

            # 拼接格式
            par = n + ' ' + str(a) + ' ' + str(s) + '\n'
            # 转义字节串
            byte = par.encode('utf-8')
            # 写入文件
            data_read.write(byte)
        # 关闭文件
        data_read.close()
        # 获取绝对路径
        print("文件存放至:", os.path.abspath(file))
    except OSError:
        print("文件路径有误")

# 10) 从文件中读取学生数据(data.txt)
def read_shudent():
    try:
        # 默认读取路径文件
        file = open('data/data_student.txt', 'rb')

        while True:
            # 读取文件
            data = file.readline()
            if not data:
                break
            # 二进制解码
            t = data.decode('utf-8')
            # 去掉左右空格
            t1 = t.strip()
            # 分割形成列表
            t2 = t1.split()
            # 序列赋值
            n, a, s = t2
            print('姓名:%s 年龄:%d 成绩:%d' % (n, int(a), int(s)))

        file.close()
    except OSError:
        print("打开文件失败")

