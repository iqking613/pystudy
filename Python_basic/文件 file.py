# -*- coding:utf-8 -*-

# 问题
# 压缩算法

import time
from student_project.student_info import *
import os
# 此示例示意文件的打开，读取及关闭
# try:
#     # 第一步打开文件
#     f = open('test/test.txt', 'rt')
#     print("打开文件成功")
#
#     # 第二步读取文件
#     s = f.read()
#     print("文件中的内容是:", s)
#     time.sleep(5)
#
#     # 第三步关闭文件
#     f.close()
#     print("文件已关闭")
# except OSError:
#     print("文件打开不存在或失败")

# 此示例示意readline方法 文件的打开，读取及关闭
# try:
#     f = open('test/test.txt')
#     print("打开文件成功")
#     # 读取内容
#     while True:
#         s = f.readline()
#         if s == '':
#             print('已经读取到了文件尾部')
#             break
#         print("读到这一行是:", s)
#
#     f.close()
# except OSError:
#     print("打开文件失败")

# 此示例示意写文本文件操作
# 'w' 以只写方式打开，删除原有文件内容（如果文件不存在，则创建该文件）
# 'a' 以只写文件打开一个文件，如果有原文件则追加到文件末尾

# f = open('test/myonte.txt', 'a')
# f.write('欢迎')
# f.write('北京')
# f.write('\n')
# f.write('hello world')
# f.write('\n')
#
# f.writelines(['a\n', 'b\n', 'c\n'])

# f.write("-----我是底部-----")
#
# f.close()

# 此示例示意以二进制方式写文件到'data.bin'
# try:
#     f = open('test/data.bin', 'wb')
#     print('打开文件成功')
#     # 写入数据  字节十六进制
#     f.write(b'\xe4\xb8\xad')
#     f.write(b'\x00\x00')
#     f.close()
#
# except OSError:
#     print("打开文件失败")

# 此示例示意以二进制方式读文件'data.bin'
# try:
#     f = open('test/data.bin', 'rb')
#     print("打开文件成功")
#     print(f.read())
#     f.close()
# except OSError:
#     print("打开文件失败")

# 此示例示意 用F.seek方法来定位文件的读写位置
# 注意: seek 通常对 二进制打开的文件进行操作
# try:
#     f = open('test/data.txt', 'rb')
#     print("打开文件成功")
#     print("刚打开文件时，文件的读写位置是: ", f.tell())    # 0
#
#     b = f.read(3)
#     print("刚读入的内容是:", b.decode('utf-8'))
#     print("读取两个字节后的读写位置是:", f.tell())   # 3
#
#     # 从当前位置偏移四个字节开始的3个字节
#     b3 = f.seek(4, 1)
#     b4 = f.read(3)
#     print('seek 从当前位置偏移四个字节后，读入的3个字节内容是:', b4.decode('utf-8'))
#     print("seek 移动后的读写位置是:", f.tell())
#
#     # 从文件尾部位置偏移三十一个字节开始的3个字节
#     b5 = f.seek(-31, 2)
#     b6 = f.read(3)
#     print('seek 从文件尾部位置偏移三十一个字节后，读入的3个字节内容是:', b6.decode('utf-8'))
#     print("seek 移动后的读写位置是:", f.tell())
#
#     # 从文件头部位置偏移七个字节开始的3个字节
#     # 定位
#     # 0 从文件开始
#     # 7 偏移位
#     b1 = f.seek(7, 0)
#     b2 = f.read(3)
#     print('seek 从头部向后偏移七个字节后，读入的3个字节内容是:', b2.decode('utf-8'))
#     print("seek 移动后的读写位置是:", f.tell())
#
#     f.close()
# except OSError:
#     print("打开文件失败")




# 练习
# 1.自己写一个文件info.txt,内部存储一些文字信息如下:
#     小张  20  100
#     小李  18  98
#     小王  19  95
# 写程序将这些数据读取出来，打印在屏幕终端上

# 文件读取/存储函数
def info_txt(file):
    # 读取文件
    L = file.readlines()

    # 将所有数据存储列表
    datas = []

    for i in L:
        # 存储每行数据

        # 方法一
        # d = {}
        # s = i.split()
        # d['name'] = s[0]
        # d['age'] = s[1]
        # d['score'] = s[2]

        # 方法二
        n, a, s = i.split()
        d = {'name': n, 'age': int(a), 'score': int(s)}

        datas.append(d)
    return datas

# try:
#     # 打开info文件
#     f = open('test/info.txt')
#
#     # 调取文件读取/存储函数
#     data = info_txt(f)
#
#     # 姓名输入项
#     while True:
#         s = input('请输入姓名:')
#         for i in data:
#             if i['name'] == s:
#                 L = []
#                 L.append(i)
#
#                 # 调取打印函数
#                 output_student(L)
#         if not s:
#             break
#     f.close()
# except OSError:
#     print('打开文件失败')

# 2.写一个程序，输入很多人的姓名，年龄，家庭住址信息，存入文件'infos.txt'中
# 文件格式自定义
# 效果:输入后查看文本格式是否是你想要的格式（文本文件操作）

def insert_info():
    # 打开文件
    info = open('test/infos.txt', 'a')
    while True:
        name = input('请输入姓名:')
        if not name:
            break
        age = input("请输入年龄:" or 0)
        address = input("请输入住址:" or '无')

        # 写入info数据
        # info.writelines(['姓名:' + name + '\n', '年龄:' + age + '\n', '住址:' + address + '\n'])
        # info.writelines(['姓名:' + name, ' 年龄:' + age, ' 住址:' + address + '\n'])

        info.writelines([name + ',', age + ',', address + '\n'])

    # 关闭文件
    info.close()
    # os.path.abspath 获取绝对路径
    print("已存放至", os.path.abspath('test/infos.txt'))
    return os.path.abspath('test/infos.txt')

# 3.写一个程序读入infos.txt中的内容，以如下格式打印
# infos.txt中内容
# 姓名: xxx, 年龄 20， 住址：xxx
# 姓名: xxx, 年龄 19， 住址：yyy

def select_info(data):
    file = open(data)
    for i in file:
        # 去掉左右空格
        s = i.strip()
        # 分割形成列表
        lst = s.split(',')
        # 序列赋值
        n, a, addr = lst
        print('姓名:%s 年龄:%d 住址:%s' % (n, int(a), addr))

    file.close()

path = r'C:\Users\Administrator\Desktop\python\马哥-python\test\infos.txt'

def main():
    while True:
        print("添加信息: 1")
        print("查看信息: 2")
        s = int(input('请选择:'))
        if s == 1:
           insert_info()
        elif s == 2:
            select_info(path)
        else:
            break

# 4. 将如下数据用二进制文件操作方式写入到文件data.txt中,数据如下：
# 小李 13888888888
# 小王 13666666666
# try:
#     file = open('test/data.txt', 'wb')
#     print("打开文件成功")
#
#     # 文本数据
#     t1 = '小李'
#     t1_number = 13888888888
#     t2 = '小王'
#     t2_number = 13666666666
#     # 拼接格式
#     s1 = t1 + ' ' + str(t1_number) + '\n'
#     s2 = t2 + ' ' + str(t2_number) + '\n'
#
#     # 转义字节串
#     b1 = s1.encode('utf-8')
#     b2 = s2.encode('utf-8')
#
#     # 以二进制字节文件写入
#     file.write(b1)
#     file.write(b2)
#
#     file.close()
# except OSError:
#     print("打开文件失败")

# 5.要程序实现复制文件功能:
# 要求:
# 1)多大的文件都能复制
# 2)要能复制二进制文件
# 3)要考虑关闭文件
# 如:
# 请输入源文件:
# 请输入目录文件:
# 已复制文件，文件长度是:
def copy_file():
    s = input("请输入源文件:")
    d = input("请输入目标文件:")
    try:
        # 打开文件
        # 打开源文件并读取二进制文件
        open_s = open(s, 'rb')
        try:
            # 打开目标文件并写入二进制文件
            open_d = open(d, 'wb')

            # 100个字节
            x = 1000
            while True:
                # 源文件每次读取x个字节
                par = open_s.read(x)
                if not par:
                    break

                # 读取x个字节写入目标文件
                open_d.write(par)

                # 获取当前文件长度
                position = open_s.tell()
                print("已复制文件，文件长度是:", position)

            # 关闭文件
            open_d.close()
        except OSError:
            print('打开', d, '文件失败')

        open_s.close()
        print("文件复制完成")
    except OSError:
        print("打开", s, "文件失败")




# 6.为学生信息管理项目添加两个功能
# | 9) 保存学生信息到文件(si.txt)    |
# | 10) 从文件中读取学生数据(si.txt) |

if __name__ == '__main__':
    copy_file()
    # main()
















