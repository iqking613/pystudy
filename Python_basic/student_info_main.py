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
            desc_score_student(datas)
        if Choice == "6":
            asc_score_student(datas)
        if Choice == "7":
            desc_age_student(datas)
        if Choice == "8":
            asc_age_student(datas)
        if Choice == "q":
            break
main()