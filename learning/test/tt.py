#coding=utf8
import numpy as np
# c,v=np.load('data.csv',delimiter=',',usecols=(6,7),unpack=True)
vector=np.array([1,3,5,7,9])
print("生成一维向量vector=\n",vector)
matrix=np.array([
    [1,3,5],
    [2,4,6],
    [7,8,9]
])
print("生成二维矩阵matrix=\n",matrix)

second_colum=matrix[:,1]
print("第二列second_colum为：",second_colum)

print(matrix[1:3,0:2])
#判断矩阵里面是否含有某个值,以下方式返回一个布尔值的矩阵matrix==3
is_has_value_three=matrix==3
print(is_has_value_three)

#逻辑运算与或(&、|)
