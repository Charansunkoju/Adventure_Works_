# importing pandas for data cleaning and data manupulation
import pandas as pd 

df1 = pd.read_csv("C:/Users/91814/OneDrive/Desktop/SQL_105_Dataset/Sales.csv",sep="\t",engine="python")

df2 = pd.read_csv("C:/Users/91814/OneDrive/Desktop/SQL_105_Dataset/Product.csv",sep = "\t",engine="python")

df3 = pd.read_csv("C:/Users/91814/OneDrive/Desktop/SQL_105_Dataset/Reseller.csv",sep = "\t",engine="python")

df4 = pd.read_csv("C:/Users/91814/OneDrive/Desktop/SQL_105_Dataset/Targets.csv",sep = "\t",engine="python")

df5 = pd.read_csv("C:/Users/91814/OneDrive/Desktop/SQL_105_Dataset/Region.csv",sep = "\t",engine="python")

df6 = pd.read_csv("C:/Users/91814/OneDrive/Desktop/SQL_105_Dataset/Salesperson.csv",sep = "\t",engine="python")

df7 = pd.read_csv("C:/Users/91814/OneDrive/Desktop/SQL_105_Dataset/SalespersonRegion.csv",sep = "\t",engine="python")

#Cleaning and summary statistics of individual data


#Sales Table
df1.info()


df1.describe()

df1.head(6)

df1.isnull().sum()


df1.duplicated().sum()


# Products Table


df2.head()


df2.info()


df2.describe()


df2.isnull().sum()



df2.fillna("black",inplace=True)


df2.isnull().sum()



df2.duplicated().sum()


#Resellers Table
df3.head()


df3.describe()



df3.info()


df3.isnull().sum()


df3.duplicated().sum()

# Targets Table
df4.head()


df4.info()


# In[89]:


df4.describe()


df4.isnull().sum()



df4.duplicated().sum()


#Region Table
df5.head()



df5.info()


df5.describe()



df5.isnull().sum()



df5.duplicated().sum()


#Sales Person
df6.head()



df6.info()


df6.describe()


df6.isnull().sum()



df6.duplicated().sum()


# Sales Person Region Table
df7.head()

df7.info()

df7.describe()

df7.isnull().sum()


df7.duplicated().sum()

pip install sqlalchemy




