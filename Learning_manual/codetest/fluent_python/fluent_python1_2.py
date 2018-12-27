from math import hypot

class Vector(object):

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)


    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
'''
v1 = Vector(2, 4)
v2 = Vector(2, 1)
print(v1 + v2)
print(abs(v2))

'''

class Test(object):
    def __init__(self, value):
        self.data = value

class TestRepr(Test):
    def __repr__(self):
        return 'Value(%r)' % self.data

class TestStr(Test):
    def __str__(self):
        return '(Value(%s)' % self.data

tr = TestRepr(1)
print(tr)
tr1 = TestRepr('1')
print(tr1)

ts = TestStr(1)
print(ts)
ts1 = TestStr('1')
print(ts1)








