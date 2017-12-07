
# coding: utf-8

# In[1]:


import pandas
#利用pandas读取csv格式的数据
titanic_train=pandas.read_csv("titanic_train.csv")
print(type(titanic_train))
print(titanic_train.dtypes)


# In[2]:


print(help(pandas.read_csv))


# In[4]:


#显示前几条数据，默认显示5条
titanic_train.head()


# In[5]:


#显示倒数前几条数据，默认显示5条
titanic_train.head()


# In[6]:


#查看列名字
titanic_train.columns


# In[7]:


#查看形状,即维度
titanic_train.shape


# In[9]:


#pandas 使用索引定位数据，使用loc函数即可
#Series object representing the row at index 0.
print(titanic_train.loc[2])


# In[17]:


#通过切片取数据,如取3到6行的数据
titanic_train.loc[3:6]


# In[27]:


#取2，5，10的数据，注意这里传入的参数是一个列表
# titanic_train.loc[[2,5,10]]#这条语句与以下两条语句等价
two_five_ten=[2,5,10]
titanic_train.loc[two_five_ten]


# In[28]:


#通过列名取数据，注意这里传入的参数是一个列表
# titanic_train[["Name","Sex"]]这条语句与以下两条语句等价
name_sex=["Name","Sex"]
titanic_train[name_sex]


# In[35]:


# 查找列名以e结尾的数据
col_name=titanic_train.columns.tolist()
print(col_name)
end_with_e_col=[]

for c in col_name:
  if c.endswith("e"):
    end_with_e_col.append(c)
print(end_with_e_col)
end_with_data=titanic_train[end_with_e_col]
print(end_with_data.head(3))


# In[36]:


#增加列操作，注意增加的列的维度必须和原来的dataframe的维度匹配，如下增加一列name2
titanic_train["Name2"]=titanic_train["Name"]
titanic_train.head()


# In[48]:


#对dataframe进行排序,按年龄来排序
titanic_train.sort_values("Age",inplace=True,ascending=True)
titanic_train.head()

