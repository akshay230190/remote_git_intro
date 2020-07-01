#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


credit=pd.read_csv('creditcard.csv')


# In[4]:


credit.head()


# In[5]:


credit.shape


# In[11]:


credit.info()


# In[13]:


credit['Class']


# In[16]:


target=credit['Class']


# In[17]:


target[:5]


# In[25]:


feature=credit[credit.columns[0:30]]


# In[26]:


feature


# In[ ]:


#Training data


# In[27]:


from sklearn.model_selection import train_test_split


# In[29]:


xtrain,xtest,ytrain,ytest=train_test_split(feature,target,test_size=0.2)


# In[31]:


xtrain.head()


# In[33]:


ytrain


# # select model

# In[34]:


from sklearn.linear_model import LogisticRegression


# In[35]:


model=LogisticRegression()


# In[37]:


model.fit(xtrain,ytrain)


# In[38]:


pred=model.predict(xtest)


# In[39]:


pred[:5]


# In[40]:


ytest[:5]


# In[41]:


from sklearn.metrics import accuracy_score,classification_report,confusion_matrix


# In[43]:


print(f"accuracy score",accuracy_score(ytest,pred)*100)


# In[44]:


print(f"confusion matrix",confusion_matrix(ytest,pred))


# In[45]:


print(classification_report(ytest,pred))


# In[ ]:




