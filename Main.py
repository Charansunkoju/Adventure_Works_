#!/usr/bin/env python
# coding: utf-8

# In[32]:


# importing pandas for data cleaning and data manupulation
import pandas as pd 


# In[51]:


df1 = pd.read_csv("C:/Users/91814/OneDrive/Desktop/SQL_105_Dataset/Sales.csv",sep="\t",engine="python")


# In[75]:


df2 = pd.read_csv("C:/Users/91814/OneDrive/Desktop/SQL_105_Dataset/Product.csv",sep = "\t",engine="python")


# In[21]:


df3 = pd.read_csv("C:/Users/91814/OneDrive/Desktop/SQL_105_Dataset/Reseller.csv",sep = "\t",engine="python")


# In[23]:


df4 = pd.read_csv("C:/Users/91814/OneDrive/Desktop/SQL_105_Dataset/Targets.csv",sep = "\t",engine="python")


# In[25]:


df5 = pd.read_csv("C:/Users/91814/OneDrive/Desktop/SQL_105_Dataset/Region.csv",sep = "\t",engine="python")


# In[27]:


df6 = pd.read_csv("C:/Users/91814/OneDrive/Desktop/SQL_105_Dataset/Salesperson.csv",sep = "\t",engine="python")


# In[29]:


df7 = pd.read_csv("C:/Users/91814/OneDrive/Desktop/SQL_105_Dataset/SalespersonRegion.csv",sep = "\t",engine="python")


# In[35]:


#Cleaning and summary statistics of individual data


# In[111]:


#Sales Table
df1.info()


# In[53]:


df1.describe()


# In[54]:


df1.head(6)


# In[56]:


df1.isnull().sum()


# In[57]:


df1.duplicated().sum()


# In[58]:


# Products Table


# In[59]:


df2.head()


# In[60]:


df2.info()


# In[61]:


df2.describe()


# In[76]:


df2.isnull().sum()


# In[77]:


df2.fillna("black",inplace=True)


# In[78]:


df2.isnull().sum()


# In[79]:


df2.duplicated().sum()


# In[86]:


#Resellers Table
df3.head()


# In[81]:


df3.describe()


# In[82]:


df3.info()


# In[83]:


df3.isnull().sum()


# In[84]:


df3.duplicated().sum()


# In[87]:


# Targets Table
df4.head()


# In[88]:


df4.info()


# In[89]:


df4.describe()


# In[90]:


df4.isnull().sum()


# In[91]:


df4.duplicated().sum()


# In[92]:


#Region Table
df5.head()


# In[93]:


df5.info()


# In[94]:


df5.describe()


# In[95]:


df5.isnull().sum()


# In[98]:


df5.duplicated().sum()


# In[99]:


#Sales Person
df6.head()


# In[100]:


df6.info()


# In[101]:


df6.describe()


# In[102]:


df6.isnull().sum()


# In[104]:


df6.duplicated().sum()


# In[105]:


# Sales Person Region Table
df7.head()


# In[106]:


df7.info()


# In[107]:


df7.describe()


# In[108]:


df7.isnull().sum()


# In[110]:


df7.duplicated().sum()


# In[112]:


pip install sqlalchemy


# In[ ]:




