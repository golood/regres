import numpy as np
from functools import reduce

# x = np.array([[2., 5.],
#           [9., 4.],
#           [6., 1.],
#           [8., 3.],
#           [1., 7.],
#           [5., 8.]])
#
# y = np.array([7., 9., 1., 6., 4., 5.])
#
#
# h1 = np.array([[2, 5],
#           [9, 4],
#           [6, 1]])
#
# h2 = np.array([
#           [8, 3],
#           [1, 7],
#           [5, 8]])
#
# y1 = np.array([7, 9, 1])
# y2 = np.array([6, 4, 5])


class Method:

    def __init__(self, x, y):
        self.y = np.array(y)
        self.x = np.array(x)
        self.a = None
        self.eps = None
        self.e = None

    def _y(self, alfa):
        A = list(map(lambda item:
                     list(map(lambda x, a: x * a, item,
                              alfa)),
                     self.x))
        A = list(map(lambda item:
                     reduce(lambda x, y: x + y, item), A))

        return A

    def epselon(self, alfa):
        return list(
            map(lambda x, y: y - x, self._y(alfa), self.y))

    def Epselon(self, alfa):
        mod = lambda x: x if (x > 0) else x * -1

        E = 1 / len(self.y) * reduce(
            lambda x, y: x + y,
            list(map(lambda x, y: mod((y - x) / y),
                     self._y(alfa), self.y))) * 100

        return E

    def getResaul(self):
        return self.a, self.eps, self.e


class MNK(Method):

    def __init__(self, x, y):
        super().__init__(x, y)

    def find_a(self):
        return np.dot(
            np.dot(
                np.linalg.inv(np.dot(self.x.T, self.x)),
                self.x.T),
            self.y)

    def run(self):
        self.a = self.find_a()
        self.eps = self.epselon(self.a)
        self.e = self.Epselon(self.a)


class MNM(Method):

    def __init__(self, x, y):
        super().__init__(x, y)

    def find_a(self):
        pass

    def run(self):
        pass


class MAO(Method):

    def __init__(self, x, y):
        super().__init__(x, y)

    def find_a(self):
        pass

    def run(self):
        pass

class MCO(Method):

    def __init__(self, x, y):
        super().__init__(x, y)

    def find_a(self):
        pass

    def run(self):
        pass


class Task:

    def __init__(self, x, y, h1=None, h2=None):
        self.methods = []
        self.methods.append(MNK(x, y))

    def run(self):

        for item in self.methods:
            item.run()

    def getResaults(self):
        resaults = []

        for item in self.methods:
            resaults.append(item.getResaul())

        return resaults
