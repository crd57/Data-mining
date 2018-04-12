# -*- coding: utf-8 -*-
"""
# @Time    : 18-4-10 下午6:47
# @Author  : Crd
# @Email   : crd57@outlook.com
# @File    : Fibonacci.py
# @Software: PyCharm
"""

c = lambda x: int(1/(5**(1/2))*((((1+5**(1/2))/2)**(x+1))- ((1-5**(1/2))/2)**(x+1)))

print(c(10))
