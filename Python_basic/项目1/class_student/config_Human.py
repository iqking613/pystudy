class Human:
    def __init__(self, n, a, s):
        self.__name = n
        self.__age = a
        self.__score = s
        self.__state = True
        if 0 <= self.__score <= 100:
            self.line = {}
            self.line['name'] = self.__name
            self.line['age'] = self.__age
            self.line['score'] = self.__score
            self.line['state'] = self.__state
            print('初始化数据已生成')

        else:
            raise ValueError('成绩大于0~100范围')

    def get_Human(self):
        return self.line