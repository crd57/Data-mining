# -*- coding: utf-8 -*-
"""
# @Time    : 18-4-11 下午7:59
# @Author  : Crd
# @Email   : crd57@outlook.com
# @File    : Shape.py
# @Software: PyCharm
"""
import math


class Shape(object):
    pass


class Rectangle(Shape):

    def __int__(self, long, width):
        self._long = long
        self._width = width

    def getCircumference(self):
        return 2 * self._long + 2 * self._width

    def getArea(self):
        return self._width * self._long


class Circle(Shape):

    def __init__(self, radius):
        self._radius = radius

    def getCircumference(self):
        return self._radius * 2 * math.pi

    def getArea(self):
        return self._radius**2 * math.pi
