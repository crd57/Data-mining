# -*- coding: utf-8 -*-
"""
# @Time    : 18-4-10 下午3:22
# @Author  : Crd
# @Email   : crd57@outlook.com
# @File    : dict.py
# @Software: PyCharm
"""
import json

D = {}
for i in range(160503, 160532):
    D[i] = 0
D[160501] = 1
D[160502] = 1


def com(dicts, day):
    return dicts[day]
com(D, 160502)

f = open('outdata,json', 'w')
y = json.dump(D, f)
f.close()
