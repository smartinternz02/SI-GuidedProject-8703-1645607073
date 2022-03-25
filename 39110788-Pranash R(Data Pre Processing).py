#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder


# In[2]:


df=pd.read_csv(r'E:\ML\New folder\flightdata.csv')


# In[3]:


df


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.info()


# In[7]:


df.describe()


# In[10]:


df.isnull()


# In[8]:


df.isnull().sum()


# In[9]:


df.shape


# In[11]:


df['TAIL_NUM'].nunique()


# In[12]:


df['UNIQUE_CARRIER'].unique()


# In[13]:


df['TAIL_NUM'].nunique()


# In[14]:


df['ORIGIN'].unique()


# In[15]:


df['DEP_TIME']=df['DEP_TIME'].fillna(df['DEP_TIME'].mean())
df['DEP_DELAY']=df['DEP_DELAY'].fillna(df['DEP_DELAY'].mean())
df['DEP_DEL15']=df['DEP_DEL15'].fillna(df['DEP_DEL15'].mean())
df['ARR_TIME']=df['ARR_TIME'].fillna(df['ARR_TIME'].mean())
df['ARR_DELAY']=df['ARR_DELAY'].fillna(df['ARR_DELAY'].mean())
df['ARR_DEL15']=df['ARR_DEL15'].fillna(df['ARR_DEL15'].mean())
df['ACTUAL_ELAPSED_TIME']=df['ACTUAL_ELAPSED_TIME'].fillna(df['ACTUAL_ELAPSED_TIME'].mean())


# In[16]:


df


# In[17]:


df.isnull().sum()


# In[18]:


from sklearn.preprocessing import LabelEncoder
from collections import Counter as count
le=LabelEncoder()


# In[19]:


df['ORIGIN']=le.fit_transform(df['ORIGIN'])


# In[20]:


df['TAIL_NUM']=le.fit_transform(df['TAIL_NUM'])


# In[21]:


df['UNIQUE_CARRIER']=le.fit_transform(df['UNIQUE_CARRIER'])


# In[22]:


df


# In[23]:


from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct=ColumnTransformer([('on',OneHotEncoder(),[0])],remainder='passthrough')


# In[24]:


df=ct.fit_transform(df)


# In[25]:


df


# In[26]:


df.shape


# In[27]:


df[df[:,:]=='SEA']

