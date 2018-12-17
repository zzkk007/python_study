
class Test(object):
    def __init__(self):
        self.items = list([1, 2, 3, 4, 5, 6])
    def prt(self):
        print(self.items)

        if 1 in self.items:
            print('True')
        else:
            print('False')

    def forfor(self):
        for i in range(len(self.items)):
            print(i)


t = Test()
t.prt()
t.forfor()
