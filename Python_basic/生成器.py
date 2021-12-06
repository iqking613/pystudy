# 此示例示意函数yield语句的生成器函数定义方式和用法

def myyield():
    '''此函数应为含有yield语句，所以称之为生成器函数'''
    yield 1
    yield 3
    yield 5
    yield 7

# gen = myyield() # gen绑定的是生成器，生成器是可迭代对象
# for i in gen:
#     print(i)    # 1, 3, 5, 7

# 用生成器函数生成一系类从0开始的整数

def myinteger(n):
    i = 0
    while i < n:
        yield i
        i += 1

# for i in myinteger(10):
#     print(i)

# 此示例示意生成器表达式定义和用法

# for i in (x ** 2 for x in range(1, 5)):
#     print(i)


# 练习
# 写一个生成器函数myeven(start, stop),用来生成从start开始,到stop结束区间内的一系类偶数
def myeven(start, stop):
    while start < stop:
        if start % 2 == 0:
            yield start
        start += 1

# L = myeven(5, 10)
# try:
#     it = iter(L)
#     print(next(it))
#     print(next(it))
#     print(next(it))
# except StopIteration:
#     pass

# evens = list(myeven(10, 20))
# print(evens)


# 程序1
L = [2, 3, 5, 7]
lst = [x + 1 for x in L]    # 列表推导式会创建一个lst新列表
it = iter(lst)
print(next(it))     # 3
L[1] = 30
print(next(it))     # 4

# 程序2
L = [2, 3, 5, 7]
lst = (x + 1 for x in L)
it = iter(lst)
print(next(it))     # 3
L[1] = 30
print(next(it))     # 31

