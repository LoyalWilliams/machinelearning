#coding=utf8
import numpy as np
vector=np.array([1,3,5,7,9])
# print("生成一维向量vector=\n",vector)
matrix=np.array([
    [1,3,5],
    [2,4,6],
    [7,8,9]
])


#各种函数
print("求vector最大值:",vector.max())
print("求vector最小值:",vector.min())
print("求vector平均值:",vector.mean())

#axis=1为对行操作，axis=0为对列操作
print("求矩阵matrix最大值：",matrix.max(axis=1))
print("求矩阵matrix最大值：",matrix.max(axis=0))
