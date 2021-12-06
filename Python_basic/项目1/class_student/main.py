from class_student.menu import show_menu
from class_student.student import Student

def main():
    while True:
        # 调取主菜单
        show_menu()

        # 调取主程序
        main = Student()

        Choice = input("请选择:")
        # 1)添加学生信息
        if Choice == "1":
            main.create_user()

        # 2)显示学生信息
        if Choice == "2":
            main.select_user()

        # # 3)删除学生信息
        if Choice == "3":
            main.delete_user()

        # 4)修改学生成绩
        if Choice == "4":
            main.update_user_score()

        # # 5)按学生成绩高 - 低显示学生信息
        if Choice == "5":
            main.desc_score()


        # # 6)按学生成绩低 - 高显示学生信息
        if Choice == "6":
            main.desc_score(order=False)

        # # 7)按学生年龄高 - 低显示学生信息
        if Choice == "7":
            main.desc_age()

        # # 8)按学生年龄低 - 高显示学生信息
        if Choice == "8":
            main.desc_age(order=False)

        # # 9)保存学生信息到文件
        if Choice == "9":
            main.save_user()

        # # 10)从文件中读取学生数据
        if Choice == "10":
            main.read_user()

        # q)退出程序
        if Choice == "q":
            break

if __name__ == '__main__':
    main()







