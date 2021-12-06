# 此示例示意python的多态（动态）

class Shape:
    '''图形'''
    def draw(self):
        print("Shape的draw() 被调用")

class Point(Shape):
    def draw(self):
        print('正在画一个点')

class Circle(Point):
    def draw(self):
        print('正在画一个圆')

def my_draw(s):
    s.draw()     # s.draw调用谁，是在运行时由s的类型动态决定，此处显示出运行时状态

shape1 = Circle()
shape2 = Point()
my_draw(shape1)
my_draw(shape2)

L = [Point(), Circle(), Point(), Circle()]
for i in L:
    i.draw()




