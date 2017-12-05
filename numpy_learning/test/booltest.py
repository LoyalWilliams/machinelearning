#coding=utf8
import numpy as np
vector=np.array([1,3,5,7,9])
# print("生成一维向量vector=\n",vector)
matrix=np.array([
    [1,3,5],
    [2,4,6],
    [7,8,9]
])
# print("生成二维矩阵matrix=\n",matrix)

# second_colum=matrix[:,1]
# print("第二列second_colum为：",second_colum)

# print(matrix[1:3,0:2])
#判断矩阵里面是否含有某个值,以下方式返回一个布尔值的矩阵matrix==3
is_has_value_three=matrix==3
print(is_has_value_three)
'''
[[False  True False]
 [False False False]
 [False False False]]
'''

#逻辑运算与或(&、|)
is_has_value_three_or_five=(matrix==3)|(matrix==5)
print(is_has_value_three_or_five)
'''
[[False  True  True]
 [False False False]
 [False False False]]
 '''

is_has_value_three_and_five=(matrix==3)&(matrix==5)
print(is_has_value_three_and_five)
'''
[[False False False]
 [False False False]
 [False False False]]
'''

#利用boolean矩阵赋值
#如把矩阵中等于3的地方变成0
matrix[is_has_value_three]=0
print(matrix)
'''
[[1 0 5]
 [2 4 6]
 [7 8 9]]
'''


#矩阵的形状shape函数
print(vector.T.shape)
print(matrix.shape)
#(5,)       5*1或1*5的矩阵
# (3, 3)    3*3的矩阵

#矩阵的数据类型的自动统一化
numbers=np.array(['1',2,3,4])
print(numbers)
print(numbers.dtype)
# ['1' '2' '3' '4']
# <U1

#类型转换
print("----")
vector=vector.astype(float)
print(vector)

numbers=np.array([1,2.0,3,4])
print(numbers)
print(numbers.dtype)
# [ 1.  2.  3.  4.]
# float64

#各种函数
print("求vector最大值:",vector.max())
print("求vector最小值:",vector.min())
print("求vector平均值:",vector.mean())


