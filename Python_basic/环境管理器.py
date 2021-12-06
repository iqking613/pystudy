# 此示例示意环境管理器类的定义和使用

class A:
    '''此类的对象可以用于with语句进行管理'''

    def __enter__(self):
        print('进去with语句')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('离开with语句')
        if exc_type is None:
            print('在with语句内部没有发生异常，正常离开with')
        else:
            print('离开with语句时，有异常发生')
            print('异常类型:', exc_type)
            print('异常内容:', exc_val)
    
try:
    with A() as a:
        print('这里是with语句里打印的')
        3 / 0     # 触发异常

except:
    print('存在异常，程序已转为正常！')

print('程序退出')