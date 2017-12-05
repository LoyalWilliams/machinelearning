
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
titanic_survival=pd.read_csv("titanic_train.csv")
titanic_survival.head()


# In[2]:


#查看一些基本的信息，比如Age这一列
age=titanic_survival["Age"]
# print(age.loc[0:10])
age_is_null=pd.isnull(age)
# print(age_is_null)
age_null_true=age[age_is_null]
# print(age_null_true)
age_null_count=len(age_null_true)
print(age_null_count)


# In[3]:


#如果数据中含有空值，则无法求出平均值等统计指标,结果为nan
mean_age=sum(titanic_survival["Age"])/len(titanic_survival["Age"])
print(mean_age)


# In[4]:


#要求出正确的统计指标，必须先把缺少值筛选掉
good_ages=titanic_survival["Age"][age_is_null==False]
correct_mean_age=sum(good_ages)/len(good_ages)
print(correct_mean_age)


# In[5]:


#padas提供了筛掉空值求均值的方法
correct_mean_age=titanic_survival["Age"].mean()
print(correct_mean_age)


# In[6]:


#求每个船舱等级的价格平均值
passenger_classes=[1,2,3]
fares_by_class={}
for this_class in passenger_classes:
    pclass_rows=titanic_survival[titanic_survival["Pclass"]==this_class]
    pclass_fares=pclass_rows["Fare"]
    fare_for_class=pclass_fares.mean()
    fares_by_class[this_class]=fare_for_class
print(fares_by_class)


# In[7]:


#利用pivot_table分组聚合
passenger_survival=titanic_survival.pivot_table(index="Pclass",values="Survived",aggfunc=np.mean)
print(passenger_survival)


# In[8]:


#aggfunc默认求均值
passenger_age=titanic_survival.pivot_table(index="Pclass",values="Age")
print(passenger_age)


# In[9]:


port_stats=titanic_survival.pivot_table(index="Embarked",values=["Fare","Survived"],aggfunc=np.sum)
print(port_stats)


# In[10]:


#specifying axis=1 or(否则) axis='columns' will drop any columns that have null values
drop_na_columns=titanic_survival.dropna(axis=1)
new_titanic_survival=titanic_survival.dropna(axis=0,subset=["Age","Sex"])
print(new_titanic_survival)


# In[11]:


#通过索引找值
row_index_83_age=titanic_survival.loc[83,"Age"]
row_index_1000_pclass=titanic_survival.loc[766,"Pclass"]
print(row_index_83_age)
print(row_index_1000_pclass)


# In[12]:


#排序，重新设置索引
new_titanic_survival=titanic_survival.sort_values("Age",ascending=False)
print(new_titanic_survival[0:10])
titanic_reindexed=new_titanic_survival.reset_index(drop=True)
print("---------------")
print(titanic_reindexed.loc[0:10])


# In[13]:


#自定义函数
def hundredth_row(column):
    #取出第100行的数据
    hundredth_item=column.loc[99]
    return hundredth_item
hundredth_row_data=titanic_survival.apply(hundredth_row)
print(hundredth_row_data)


# In[14]:


#求每个列的缺失指标格式
def not_null_count(column):
    column_null=pd.isnull(column)
    null=column[column_null]
    return len(null)

column_null_count=titanic_survival.apply(not_null_count)
print(column_null_count)


# In[16]:


#通过axis=1这个参数，我们可以使用DataFrame.apply（）方法来迭代每行的数据,进行转换
def which_class(row):
    pclass=row['Pclass']
    if pd.isnull(pclass):
        return "Unknown"
    elif pclass == 1:
        return "First Class"
    elif pclass == 2:
        return "Second Class"
    elif pclass == 3:
        return "Third Class"
    
classes=titanic_survival.apply(which_class,axis=1)
print(classes)


# In[18]:


def is_minor(row):
    if row["Age"]<18:
        return True
    else:
        return False
minors=titanic_survival.apply(is_minor,axis=1)
# print(minors)dsffd
def generate_age_label(row):
    age=row["Age"]
    if pd.isnull(age):
        return "unknown"
    elif age<18:
        return "minor"
    else:
        return "adult"
    
age_labels=titanic_survival.apply(generate_age_label,axis=1)
print(age_labels)


# In[19]:


#获救的平均值
titanic_survival['age_labels']=age_labels
age_group_survival=titanic_survival.pivot_table(index="age_labels",values="Survived")
print(age_group_survival)

