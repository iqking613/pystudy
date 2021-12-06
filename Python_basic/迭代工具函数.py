# 此示例示意zip函数定义方法和用法
numbers = [10086, 10000, 10010, 95588]
names = ["中国移动", "中国电信", "中国联通"]

# 返回元组
for t in zip(names, numbers):
    print(t)

# 返回字典
# d = dict(zip(names, numbers))
# print(d)

# 此示例示意enumerate函数定义方法和用法
names = ["中国移动", "中国电信", "中国联通"]

# 返回生成带有索引元组
# for i in enumerate(names):
#     print(i)



# 练习
# 1.写一个程序，读入任何行文字，当输入空行是结束输入
# 打印带有行号的输入结果
def read_lines():
    '''此函数读取用户输入的信息'''
    L = []
    while True:
        s = input("请输入:")
        if s == '':     # 也可以写成 if not s:
            break
        L.append(s)
    return L

def print_lines(L):
    '''打印带有行号的文字'''
    for i in enumerate(L, 1):
        print("第%d行:%s" % i)

if __name__ == "__main__":
    lst = read_lines()
    print_lines(lst)



