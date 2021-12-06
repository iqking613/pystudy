
# 此示例示意多继承的语法和用法
class Car:
    def run(self, speed):
        print('车正在以', speed, '公里/小时的速度行驶')

class Plane:
    def fly(self, height):
        print('飞机以', height, '米的高空飞行')

class PlaneCar(Plane, Car):
    '''PlanCar 类同时继承Plane和Car 类'''
    pass

p1 = PlaneCar()
p1.fly(1000)
p1.run(300)

# 多继承缺陷
class A:
    def m(self):
        print('A.m()被调用')

class B:
    def m(self):
        print('B.m()被调用')

class AB(A, B):
    def m(self):
        print('AB.m()被调用')
        super().m()
ab = AB()
ab.m()      # 当AB类没有覆盖父类的方法时会出现名字冲突问题

# 类的__mro__属性
class A:
    pass
class B:
    pass
class C:
    pass
class D:
    pass
class AB(A, B):
    pass
class CD(C, D):
    pass
class ABCD(AB, CD):
    pass

print(ABCD.__mro__)




