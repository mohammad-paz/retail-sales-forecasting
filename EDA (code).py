#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv("Retail Sales Forecasting.csv")


# In[3]:


df.head()


# In[4]:


df.shape


# In[5]:


df.isnull().sum()


# In[6]:


df.dtypes


# In[7]:


df["date"] = pd.to_datetime(df["date"])


# In[8]:


df.dtypes


# In[9]:


df["Revenue"] = df["Sale"] * df["price"]


# In[10]:


df.head()


# In[11]:


df["Day"] = df["date"].dt.day
df["Month"] = df["date"].dt.month
df["Year"] = df["date"].dt.year
df.head()


# In[12]:


df[df["Revenue"] == df["Revenue"].max()]


# In[13]:


df[df["Sale"] == df["Sale"].max()]


# In[14]:


((df.corr()>0.1)|(df.corr()<-0.1))*df.corr()  #calculatin the correlation, ignoring those with absolute value less than 0.1


# In[15]:


day_sales = df.groupby("Day").mean()
day_sales = day_sales[["Sale", "Stock", "price", "Revenue"]]


# In[16]:


fig, axs = plt.subplots(2, 2 , figsize = [14, 14])
fig.suptitle('Variables over the days of the month', fontsize = 18)
axs[0, 0].plot(day_sales.index, day_sales.Sale, color = 'red')
axs[0, 0].set_title('Sales', fontsize = 14)
axs[0, 1].plot(day_sales.index, day_sales.Stock, color = 'black')
axs[0, 1].set_title('Stock', fontsize = 14)
axs[1, 0].plot(day_sales.index, day_sales.price, color = 'blue')
axs[1, 0].set_title('Price', fontsize = 14)
axs[1, 1].plot(day_sales.index, day_sales.Revenue, color = 'green')
axs[1, 1].set_title('Revenue', fontsize = 14)


# In[17]:


# rescaling all the variables
dsm = day_sales
dsm.head()
# multiplying by the mean differences to ensure all are on the same scale
dsm['price'] = dsm['price'] * 1010
dsm['Sale'] = dsm['Sale'] * 17.77
dsm['Revenue'] = dsm['Revenue'] * 10.8
dsm = dsm.reset_index()


# In[18]:


plt.figure(figsize=(16,8))
plt.title('Relationship Between Variables', fontsize = 18)
plt.plot('Day', 'Sale', data = dsm, color='black', linewidth=2, label = "Sales")
plt.plot('Day', 'price', data = dsm, color='gold', linewidth=2, label = "Price")
plt.plot('Day', 'Stock', data = dsm, color='red', linewidth=2, label="Stock")
plt.plot('Day', 'Revenue', data = dsm, color='green', linewidth=2, label="Revenue")
plt.yticks([])
plt.legend(fontsize = 12)


# In[ ]:




