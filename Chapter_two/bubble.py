# -*- coding: utf-8 -*-
"""
# @Time    : 18-4-10 下午3:21
# @Author  : Crd
# @Email   : crd57@outlook.com
# @File    : bubble.py
# @Software: PyCharm
"""

SList = [5, 6, 3, 4, 8, 1, 9, 0, 2]


def bubble(List):
    for j in range(len(List)):
        for i in range(len(List))[::-1]:
            if (i-1) >= 0:
                if List[i] < List[i-1]:
                    temp = List[i]
                    List[i] = List[i-1]
                    List[i-1] = temp
    return List


a = bubble(SList)
