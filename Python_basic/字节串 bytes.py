# 练习
# 输入一个字符串用S 绑定
#     将此字符串转换为字节串，用b绑定
#     再将此字节串b转换回字符串，用s2绑定
#     判断s 与 s2 是否相同

def bytes_byte():
    S = input("请输入:")

    # 编码
    b = S.encode('utf-8')
    print("转换为字节串:", b)

    # 解码
    s2 = b.decode('utf-8')
    print("转换为字符串:", s2)

    # 判断输入与解密后是否相同
    if S == s2:
        return print("相同")
    return print("不同")

# bytes_byte()


# 练习
# 1.写一个生成器函数myodd(x) 来生成一系列奇数
# 如：
#     myodd(10)  可以生成1， 3， 5， 7， 9
def myodd(x):
    i = 1
    while i < x:
        if i % 2 != 0:
            yield i
        i += 1

# gen = myodd(10)
# for i in gen:
#     print(i)

# 2.写一个生成器函数primes(n)来生成n以内的所有素数
#     1)打印100以内的全部素数
#     2)打印100以内的全部素数的和
def pimes(n):
    x = 2
    while x < n:
        i = 2
        while i < x:
            # print("%d %% %d = %d" % (x, i, x % i))
            if x % i == 0:
                break
            i += 1
        else:
            yield x
        x += 1

# gen = pimes(100)
# Sum = 0
# for i in gen:
#     print(i)
#     Sum += i
# print(Sum)
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# 3.写一个生成器函数myrange([start,] stop [,step])来生成一系列的整数
# 要求：
#     myrange功能与range功能完全相同
#     不允许调用range函数
#     用自己写的myrange结合生成器表达式求1~100内奇数的平方和

def myrange(start, stop = None, step = 1):
    if stop is None:
        stop = start
        start = 0
    if step > 0:
        while start < stop:
            yield start
            start += step
    elif step < 0:
        while start > stop:
            yield start
            start += step

    # if stop is 0:
    #     while stop < start:
    #         yield stop
    #         stop += step
    # elif stop > start and step > 0:
    #     while start < stop:
    #         yield start
    #         start += step
    # elif stop < start and step < 0:
    #     while start > stop:
    #         yield start
    #         start -= abs(step)
    # else:
    #     print("格式有误")
    # elif stop > 0:
    #     i = start
    #     while i < stop and step > 0:
    #         yield i
    #         i += step
    #     while i > stop and step < 0:
    #         yield i
    #         i -= abs(step)
    # elif stop < 0 and step < 0:
    #     i = start
    #     while i > stop:
    #         yield i
    #         i -= abs(step)
# print([x for x in myrange(39)])
# print([x for x in myrange(39, 51)])
# print([x for x in myrange(69, 51, -2)])
# print([x for x in myrange(69, 100, 2)])
# for i in myrange(20, 30):
#     print(i)

print(sum( (x ** 2 for x in myrange(1, 11) if x % 2 != 0) ))











