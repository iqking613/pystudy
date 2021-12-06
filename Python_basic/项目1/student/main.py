from student.login import Login
from student.message import Message
from index.menu import show_menu
from index.index1 import Index1

def main():

    while True:
        # 调用登录/注册菜单
        index = show_menu()

        # 调用登录/注册对象
        main = Login()
        Choice = input('请选择:')

        # 登录
        if Choice is '1':
            name = input('请输入账号:')
            passwd = input('请输入密码:')
            # sign_in传参
            status = main.sign_in(name, passwd)
            if status is True:
                while True:
                    # 调用信息菜单
                    main = Index1()
                    Choice = input('请选择:')
                    # 我的信息
                    if Choice is '1':
                        I_Info = Message().info(name)
                        # 格式化输出
                        for i in I_Info:
                            print('姓名:%s' % i[0])
                            print('身份证:%d' % int(i[1]))
                            print('Tel:%d' % int(i[2]))
                            print('Email:%s' % i[3])
                    # 课程信息
                    elif Choice is '2':
                        Course = Message().course(name)
                        # 格式化输出
                        for i in Course:
                            print('课程名称:%s' % i[0])
                            print('学习进度:%s' % i[1])
                    elif Choice is '3':
                        Score = Message().s_score(name)
                        # 格式化输出
                        for i in Score:
                            print('课程名称:%s' % i[0])
                            print('课程成绩:%d' % int(i[1]))
                    # 注销/退出登录
                    elif Choice is 'q':
                        print('用户%s: 已退出!' % name)
                        break
        # 注册
        elif Choice is '2':
            name = input('请设置用户:')
            passwd = input('请设置密码:')
            id = input('请输入身份证号:')
            Tel = input('请输入手机号:')
            Email = input('请输入邮箱:')
            # register传参
            main.register(name, passwd, id, Tel, Email)



if __name__ == '__main__':
    main()