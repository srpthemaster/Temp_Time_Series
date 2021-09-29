#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
 
# read a tips.csv file from seaborn library
Data = pd.read_csv (r'IOT-temp.csv')
print(Data)


# In[3]:


InsideData = Data[(Data['out/in']=='In')]
print (InsideData)


# In[4]:


OutsideData = Data[(Data['out/in']=='Out')]
print (OutsideData)


# In[39]:


#Vertically slice for training and test data
SlicedInputData = InsideData.iloc[:,-2:-1]
SlicedInputData


# In[7]:


#Vertically slice for training and test data
SlicedOutputData = OutsideData.iloc[:,-3:-1]
SlicedOutputData


# In[8]:


#Decompose the seansonal and other components from the trend
import statsmodels
from statsmodels.tsa.seasonal import seasonal_decompose
series = SlicedInputData
result = seasonal_decompose(series, model='additive')
print(result.trend)
print(result.seasonal)
print(result.resid)
print(result.observed)


# In[31]:


# Python program to convert
# date to timestamp
 
import time
import datetime

def ConvertToFloat (date):
     #'08-12-2018 09:30'
    element = datetime.datetime.strptime(date,("%d-%m-%Y %H:%M"))
 
    tuple = element.timetuple()
    timestamp = time.mktime(tuple)
 
    return timestamp


# In[15]:


for eachEntry in InsideData:
    eachEntry['timestamp'] = ConvertToFloat (eachEntry['noted_date'])
    
print(InsideData)


# In[19]:


for i in InsideData:
    print(InsideData.iloc[i:i+1,-3])


# In[43]:


InsideData['timestamp'] = InsideData['noted_date'].apply(ConvertToFloat)
print(InsideData)


# In[40]:


print(InsideData)


# In[44]:


#Vertically slice for training and test data
SlicedInputData = InsideData.iloc[:,-3:-1]
SlicedInputData


# In[45]:


for i in InsideData:
    print(i)


# In[46]:


InsideDataNew = InsideData
print(InsideDataNew)


# In[47]:


#Vertically slice for training and test data
SlicedInputDataNew = InsideDataNew.iloc[:,-3:-1]
SlicedInputDataNew


# In[ ]:




