# --*-- coding: utf-8 --*--
class Human:
    L = []
    count = 0
    def __init__(self, n, a, s):
        self.name = n
        self.age = a
        self.score = s
        self.state = True
        if 0 <= self.score <= 100:
            self.line = {}
            self.line['name'] = self.name
            self.line['age'] = self.age
            self.line['score'] = self.score
            self.line['state'] = self.state
            self.__class__.L.append(self.line)
            self.__class__.count += 1
            print('初始化数据已生成')
        else:
            print('成绩大于0~100范围')

    def info_student(self, data=L):
        for i in data:
            if i.get('state') is True:
                print(i.get('name'), i.get('age'), i.get('score'), i.get('state'))

    def set_student(self, name, score):
        for i in self.__class__.L:
            print(i)
            if i['name'] is name:
                i['score'] = score

    def del_student(self):
        for i in self.__class__.L:
            if i['name'] is self.name:
                i['state'] = False
                self.__class__.count -= 1

    # 成绩排序
    # 默认降序，当order=False 升序
    def desc_score_student(self, order=True):
        self.info_student(sorted(self.L, key=lambda d: d['score'], reverse=order))

    # 年龄排序
    # 默认降序，当order=False 升序
    def desc_age_student(self, order=True):
        self.info_student(sorted(self.L, key=lambda d: d['age'], reverse=order))
    def __del__(self):
        self.__class__.count -= 1












