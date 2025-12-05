#!/usr/bin/env python
# coding: utf-8

# # Import Libararies

# In[9]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# # Read All Datasheets

# In[10]:


# import orders file:
F_Order = pd.read_excel(r"D:\COURSES\Data X\Database (1).xlsx",sheet_name="Orders")
F_Order


# In[11]:


# import Salesperson file:
Dim_Salesperson = pd.read_excel(r"D:\COURSES\Data X\Database (1).xlsx",sheet_name="Salesperson")
Dim_Salesperson


# In[12]:


# import Customer file:
Dim_Customer = pd.read_excel(r"D:\COURSES\Data X\Database (1).xlsx",sheet_name="Customer")
Dim_Customer


# In[13]:


# import City file:
Dim_City = pd.read_excel(r"D:\COURSES\Data X\Database (1).xlsx",sheet_name="City")
Dim_City


# # Exploration Data Analysis(EDA)

# In[14]:


# get info from F_order table:
F_Order.info()


# In[15]:


# check duplicated rows:
F_Order.duplicated().sum()


# In[16]:


# get info from Dim_City: 
Dim_City.info()


# In[17]:


# get info from Dim_Customer table:
Dim_Customer.info()


# In[18]:


# I need to convert Datatype in city columns to int
# I also need to merage table city, customer to one table based on city-id after i converted cityid in one table to int


# In[19]:


# get info from Dim_Salesperson table
Dim_Salesperson.info()


# In[20]:


# check missing data in all tables


# In[21]:


Dim_Salesperson.isnull().sum()


# In[22]:


F_Order.isnull().sum()


# In[23]:


# I have two columns I need to treat with them leter they are ScheduledDeliveryDate and ActualDeliveryDate   


# In[24]:


Dim_Customer.isnull().sum()


# In[25]:


# i have missed values in cityID


# In[26]:


Dim_City.isnull().sum()


# # Data Cleaning

# In[27]:


# convert cityid from int datatype to float


# In[28]:


# convert to float
Dim_City["CityID"]=Dim_City["CityID"].astype(float)
# check result
Dim_City.info()


# In[29]:


# merge Dim_costumer table with Dim_city table based on CityID in new table called full_customer


# In[30]:


# merge tables
Full_Customer=Dim_Customer.merge(Dim_City, how="inner")
Full_Customer


# In[31]:


# check if I have duplicate or not
Full_Customer.duplicated().sum()


# In[33]:


# check duplicate in custumerID column
Full_Customer["CustomerID"].duplicated().sum()


# In[47]:


#check missing values
Full_Customer.isnull().sum()


# # Analysis Data

# In[ ]:


# I do relationships between tables and create date table 
# I will do calculation all KPIs in Power BI after by writting profitional DAX functions.
# Grouping calculation kpis with same category sach as city, customer,salesperson,team and so on.


# # Visualize Data

# In[ ]:


# I will visualize data in Power bi Desktop to show all my results
#after that writing report to explane what is happen? why? and how to solve this problems. 


# # Saved Cleaned Data

# In[58]:


Full_Customer.to_excel('Full_Customer.xlsx',index=False)


# In[59]:


Dim_Salesperson.to_excel('Dim_Salesperson.xlsx',index=False)


# In[61]:


F_Order.to_excel('F_Order.xlsx',index=False)


# In[ ]:


# let us to go power bi to create date table, create model, writing dax and visualize all data.

