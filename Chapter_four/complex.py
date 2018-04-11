# -*- coding: utf-8 -*-
"""
# @Time    : 18-4-11 下午7:22
# @Author  : Crd
# @Email   : crd57@outlook.com
# @File    : complex.py
# @Software: PyCharm
"""


class Complex(object):
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def add(self, c):
        self._a = self._a + c._a
        self._b = self._b + c._b

    def show(self):
        if self._b < 0:
            print("%a - %si" % (self._a, abs(self._b)))
        elif self._b == 0:
            print("%a " % self._a)
        else:
            print("%a + %si" % (self._a, abs(self._b)))

c1 = Complex(2, 3)
c2 = Complex(8, -1)
# c2 = Complex c2(8,-1)
c1.add(c2)
c2.show()
c1.show()
