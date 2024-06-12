#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[20]:


df=pd.read_csv("C:/Users/dsk67/Desktop/Old Firefox Data/zomato.csv",encoding="latin-1")


# In[22]:


df.head()


# In[23]:


df.info()


# In[25]:


df.describe()


# In[26]:


df.isnull()


# In[29]:


df.isnull().sum()


# In[48]:


[features for features in df.columns  if  df[features].isnull().sum()>0]


# In[56]:


sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap="viridis")
##the values are very very less thats why we cant see the diagaram


# In[55]:


df.shape


# In[67]:


df1=pd.read_excel("C:/Users/dsk67/Desktop/Old Firefox Data/Country-Code.xlsx")


# In[72]:


print(df1)


# In[74]:


df1.head()


# In[89]:


##how to add two files wecan use pd.merge()
df3= pd.merge(df,df1,on= "Country Code", how="left")
(df3).head()


# In[96]:


##how to check data types
df3.dtypes


# In[98]:


df3.columns


# In[126]:


## how many different types of countries are there
df3.Country.value_counts()


# In[129]:


##name of different countries
countries_name= df3.Country.value_counts().index
countries_name


# In[135]:


##useful to make pie chart
country_values= df3.Country.value_counts().values
country_values


# In[161]:


##for pie chart

plt.pie(country_values,labels=countres_name)


# In[175]:


##pie chart top 3 countries use zomato 
##autopct="%1.2f%%" -it tells  percentage  wise each country use
plt.pie(country_values[:3],labels=countres_name[:3],autopct="%1.2f%%")


# In[178]:


##observation: zomato majority  of users are  1-indians,2-US, 3-UK 
    


# In[180]:


df3.columns


# In[229]:


##adding 3 groups together
Ratings=df3.groupby(['Aggregate rating','Rating color', 'Rating text']).size().reset_index().rename(columns={0:'Rating Count'})


# In[ ]:





# In[230]:


Ratings


# In[ ]:


#observation   rating	 Rating color	 Rating text	
 # {         0             White	           Not rated
 #           1.8to 2.4     Red              Poor
 #           2.4 to 3.4    Orange           Average
 #           3.5 to 3.9    Yellow           good
 #           4.0 to 4.4    Green            Very Good
 #           4.5 to 4.9    Dark Green       Excellent }


# In[267]:


import matplotlib



# In[249]:


matplotlib.rcParams['figure.figsize'] = (18,12)
sns.barplot(x="Aggregate rating",y= "Rating Count", data= Ratings)


# In[269]:


# i changed  white color to blue color beacuse white was not visible ,write colors name in small letters it cant see captial letters and will give error 
sns.barplot(x="Aggregate rating",y= "Rating Count", hue='Rating color' ,data= Ratings,palette=['blue','red','orange','yeLlow','green','darkgreen'])


# In[ ]:


#observation -blue (not rated ) is maximum and  average rating peak at 3.2 
               


# In[272]:


#count plot
sns.countplot(x='Rating color',data= Ratings ,palette=['blue','red','orange','yeLlow','green','darkgreen'])


# In[278]:


Ratings.head()


# In[ ]:






# In[281]:


Ratings


# In[ ]:





# In[303]:


countries_ratings=df3.groupby(['Aggregate rating','Rating color', 'Rating text',"Country"]).size().reset_index().rename(columns={0:'Rating Count'})


# In[305]:


countries_ratings


# In[308]:


##find the countries rating that has 0 rating
sns.countplot(x="Country",data=countries_ratings  ,palette=['blue','red','orange','yeLlow','green','darkgreen'])


# In[ ]:


# observation  - from this bar graph we can say that countries - Brazil ,Sri lanka and South Africa has given zero ratings 


# In[315]:


#which currency is used by which country
currency_usage=df3.groupby(["Country","Currency"]).size().reset_index().rename(columns={0:'Rating Count'})


# In[343]:


currency_usage


# In[344]:


currency_usage.


# In[368]:


# which country  do have online deliveries 
online_deliveries=df3.groupby(["Country","Has Online delivery"]).size().reset_index().rename(columns={0:'Rating Count'})


# In[369]:


online_deliveries


# In[367]:


# graph of which country  do have online deliveries 
sns.countplot(x="Country" ,hue="Has Online delivery",data= online_deliveries ,palette=['yellow','red'])


# In[381]:


#create a pie chart for cities distribution
citites_distribtution=df3.groupby(["City","Has Online delivery","Country"]).size().reset_index()
citites_distribtution


# In[403]:


city_values=df3.City.value_counts().values
city_labels=df3.City.value_counts().index


# In[409]:


plt.pie(df3.City.value_counts(),labels=df3.City.value_counts().index,autopct="%1.2f%%")


# In[408]:


plt.pie(city_values[:4],labels=city_labels[:4],autopct="%1.2f%%")


# In[ ]:


#observation top 4 cities  with most distribution are new delhi, gurgaon,noida and faridabad 

