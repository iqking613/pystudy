from menu import show_menu
from student_info import *

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
        if Choice == "9":
            save_shudent(datas)
        if Choice == "10":
            read_shudent()
        if Choice == "q":
            break
if __name__ == '__main__':
    main()







