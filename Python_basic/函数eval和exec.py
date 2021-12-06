# 此示例示意eval的用法
# x = 100
# y = 200
# v = eval("x + y")
# print(v)
#
# dict_local = {"x": 1, "y": 2}
# v = eval("x + y", None, dict_local)
# print(v)    # 3
#
# dict_global = {"x": 10, "y": 20}
# v = eval("x + y", None, dict_local)
# print(v)    # 3


# 此示例示意exec的用法
x = 100
y = 200
s = '''
z=x+y
print("z = ", z)
print("hello")
'''
exec(s)

