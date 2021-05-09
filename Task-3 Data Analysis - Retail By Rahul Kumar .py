#!/usr/bin/env python
# coding: utf-8

# ## Exploratory Data Analysis - Retail
# 
# #### By Rahul Kumar
# 
# * Perform ‘Exploratory Data Analysis’ on dataset ‘SampleSuperstore’
# * As a business manager, try to find out the weak areas where you can work to make more profit.
# * What all business problems you can derive by exploring the data?
# * I used Python to perform EDA on this dataset.
# * I used Tableau for Dashboard .
# * Dataset: https://bit.ly/3i4rbWl 

# In[1]:


import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


# In[2]:


data = pd.read_csv("/Users/rahulkumar/Desktop/data_set_data_scinece/SampleSuperstore.csv")


# In[3]:


data.sample(5)


# In[7]:


data.head()


# In[8]:


data.tail()


# In[10]:


data.shape


# In[11]:


data.info()


# In[13]:


data.describe()


# ## Number of unique values in each column
# 

# In[14]:


for i in data.columns:
    print(i,len(data[i].unique()))


# 
# 

# ## Check for null values

# In[15]:


data.isnull().sum()


# ## Data Visualization

# In[16]:


sns.pairplot(data)


# In[6]:


data.hist()


# In[9]:


data.hist('Postal Code')


# In[10]:




data.hist('Sales')


# In[11]:


data.hist('Quantity')


# In[12]:


data.hist('Discount')


# In[13]:


data.hist('Profit')


# In[17]:



fig,axes = plt.subplots(1,1,figsize=(12,7))
sns.heatmap(data.corr())
plt.show()


# In[18]:


fig,axes = plt.subplots(1,2,figsize=(14,5))
fig.suptitle("Total profit VS sales ")
sns.barplot(data=df.groupby('Sub-Category')['Sales','Profit'].agg(sum),x='Sales',y='Profit',ax=axes[1])
data.groupby('Sub-Category')['Sales','Profit'].agg(sum).plot(kind='bar',ax=axes[0])
plt.xticks(rotation=90)
plt.show()


# In[19]:


fig,axes = plt.subplots(1,2,figsize=(14,5))
fig.suptitle("Total Sales VS Quantity ")
sns.barplot(data=df.groupby('Sub-Category')['Sales','Quantity'].agg(sum),x='Sales',y='Quantity',ax=axes[1])
data.groupby('Sub-Category')['Sales','Quantity'].agg(sum).plot(kind='bar',ax=axes[0])
plt.xticks(rotation=90)
plt.show()


# In[20]:


fig,axes = plt.subplots(1,2,figsize=(14,5))
df.groupby('Sub-Category')['Discount','Profit'].agg(sum).plot(kind='bar',ax=axes[0]).set_title('Discount & Profit Relation based on Sub-Category')
data.groupby('Sub-Category')['Profit','Quantity'].agg(sum).plot(kind='bar',ax=axes[1]).set_title('Quantity & Profit Relation based on Sub-Category')
plt.xticks(rotation=90)
plt.show()


# In[21]:


fig,axes = plt.subplots(2,2,figsize=(16,8))
fig.suptitle("Distribution plots", fontsize=16)
sns.distplot(data['Sales'],ax=axes[0,0])
sns.distplot(data['Profit'],ax=axes[0,1])
sns.distplot(data['Discount'],ax=axes[1,0])
sns.distplot(data['Quantity'],ax=axes[1,1])
plt.show()


# In[22]:


fig,axes = plt.subplots(2,2,figsize=(16,8))
fig.suptitle("Sales with different shipping modes and Segments", fontsize=16)
sns.barplot(df['Ship Mode'],data['Sales'],ax=axes[0,0])
sns.lineplot(df['Ship Mode'],data['Sales'],ax=axes[0,1])
sns.barplot(df['Segment'],data['Sales'],ax=axes[1,0])
sns.lineplot(df['Segment'],data['Sales'],ax=axes[1,1])
plt.show()


# In[23]:


fig,ax= plt.subplots(1,1,figsize=(12,7))
sns.countplot(data['Quantity'],hue=data['Region'])
plt.show()


# ## Some important Findings
# *  The features Profit and Discounts are highly related.
# *  Over Less quantity of products also the sales were high.
# * The maximum quantity of product in demand was in range 2-4.
# *  The mode of shipping doesn't affect much to the sales
# *  The Home Office provides highest sales followed by Corporate by a slight variation
# 

# ## Thank You :)
# 
#   #### By Rahul Kumar

# In[ ]:




