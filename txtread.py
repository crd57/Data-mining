# -*- coding: utf-8 -*-
"""
# @Time    : 18-4-10 下午3:46
# @Author  : Crd
# @Email   : crd57@outlook.com
# @File    : txtread.py
# @Software: PyCharm
"""

f = open('horseColic.txt', mode='r')
data = f.readlines()
dataArr = []
for i in range(len(data)):
    dataArr.append(data[i].strip('\n').split(sep='\t'))
