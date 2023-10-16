#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data= pd.read_csv(r"C:\Users\hp\OneDrive\Desktop\8. Netflix Dataset.csv")


# In[3]:


data.head(2)


# In[4]:


data.shape


# In[5]:


data.info()


# In[7]:


data.describe()


# In[8]:


data.columns


# In[9]:


data.info()


# In[10]:


data.isnull().sum()


# In[11]:


import seaborn as sns


# In[12]:


sns.heatmap(data.isnull())


# In[13]:


data.dtypes


# In[15]:


data.duplicated().sum()


# In[18]:


data[data.duplicated()]


# In[20]:


data.drop_duplicates(inplace=True)


# In[22]:


data.duplicated().sum()


# In[23]:


data.isnull().sum()


# In[25]:


sns.heatmap(data.isnull())


# In[26]:


data.head(4)


# In[33]:


data[data['Title'].isin(['House of Cards'])]


# In[34]:


data[data['Title'].isin(['House of Cards'])]


# In[36]:


data[data['Title'].str.contains('House of Cards')]


# In[37]:


data.dtypes


# In[40]:


data['Release_Date'] = data['Release_Date'].apply(pd.to_datetime)


# In[41]:


data.head(2)


# In[42]:


data.dtypes


# In[43]:


data


# In[45]:


data['Release_Date'].dt.year.value_counts().plot(kind='bar')


# In[47]:


data['Release_Date'].dt.year.value_counts().plot(kind='bar')


# In[48]:


data.head()


# In[50]:


data.Category.value_counts()


# In[51]:


sns.countplot(x='Category',data=data)


# In[54]:


data['year']=data['Release_Date'].dt.year


# In[55]:


data


# In[58]:


data[(data['Category'] == 'Movie') & (data['year']==2020)].shape


# In[68]:


data[(data['Category'] == 'TV Show') & (data['Country']=='India')] ['Title'].value_counts().sum()


# In[69]:


data.head(2)


# In[71]:


data.Director.value_counts().head(10)


# In[73]:


data[(data['Category'] == 'Movie') &(data['Type'] == 'Comedies')| (data['Country']=='United Kingdom')].shape


# In[74]:


data.head(2)


# In[75]:


data[data['Cast']=='Tom Cruise']


# In[76]:


data.Cast.dtypes


# In[77]:


data.isnull().sum()


# In[78]:


data1 = data.dropna()


# In[79]:


data1.head(2)


# In[80]:


data1.isnull().sum()


# In[82]:


data1[data1['Cast'].str.contains('Tom Cruise')]


# In[83]:


data.head(2)


# In[86]:


data.Rating.nunique()


# In[87]:


data.Rating.unique()


# In[89]:


data[(data['Category'] == 'Movie') &(data['Rating'] == 'TV-14')& (data['Country']=='Canada')].shape


# In[90]:


data[(data['Category'] == 'TV Show') &(data['Rating'] == 'R')& (data['year'] >2018)].shape


# In[91]:


data.head(2)


# In[92]:


data[['Minutes','Units']]=data['Duration'].str.split(' ',expand=True)


# In[93]:


data


# In[94]:


data.dtypes


# In[100]:


data.Minutes.max()


# In[102]:


data.Minutes.min()


# In[103]:


data.Minutes.mean()


# In[104]:


data_tvshow = data[data['Category']=='TV Show']


# In[106]:


data_tvshow.Country.value_counts().head(10)


# In[109]:


data.sort_values(by='year', ascending=False).head(2)


# In[110]:


data[(data['Category'] == 'Movie') &(data['Type'] == 'Dramas') ]#& (data['year'] >2018)].shape


# In[112]:


data[(data['Category'] == 'Movie') &(data['Type'] == 'Dramas') |(data['Category'] == 'TV Show')& (data['Type'] == "Kids' TV")].shape


# In[ ]:




