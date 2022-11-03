class C(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        print("getter of x called")
        return self._x

    @x.setter
    def x(self, value):
        print("setter of x called")
        self._x = value

    @x.deleter
    def x(self):
        print("deleter of x called")
        del self._x


class Test:
    def __init__(self):
        self._p1 = 0

    @property
    def p1(self):
        print ('getter')
        return self._p1

    @p1.setter
    def p1(self, v):
        print ('setter')
        if v > 10:
            self._p1 = v
        else:
            self._p1 = 100
