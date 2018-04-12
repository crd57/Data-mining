# -*- coding: utf-8 -*-
"""
# @Time    : 18-4-11 下午8:24
# @Author  : Crd
# @Email   : crd57@outlook.com
# @File    : data_csv.py
# @Software: PyCharm
"""

import pandas as pd

data = pd.read_csv('/home/crd/文档/Data-mining/Chapter_five/data.csv')
c = data['Id'].isnull()  # 去空值
for i in range(len(c)):
    if c[i]:
        data.iat[i, 0] = i + 1

data.drop_duplicates()  # 删除重复的行

mean = data[['Chinese', 'Math', 'English']].mean(1)  # 求平均值
data = pd.concat([data, mean], axis=1)  # 将mean添加到列
data.rename(index=str, columns={0: 'Mean'}, inplace=True)
data.Mean[data.Mean == data.Mean.max()].index.tolist()  # 平均值最大值所在的位置
num_chinese = len(data[data.Chinese > 60].index.tolist())  # 每个科目及格的人数
num_math = len(data[data.Math > 60].index.tolist())
num_English = len(data[data.English > 60].index.tolist())
