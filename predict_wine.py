#!/usr/bin/env python
# coding: utf-8

# # wine dataset

# ## step 1 import all libery

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


from sklearn.datasets import load_wine


# In[4]:


wine=load_wine()


# In[5]:


wine['feature_names']


# In[7]:


wine['target_names']


# In[66]:


#print(wine.DESCR)


# In[14]:


feature=pd.DataFrame(wine['data'],columns=wine['feature_names'])


# In[15]:


feature.head()


# In[17]:


target=pd.Series(wine['target'],name='wine_type')


# In[18]:


target.unique()


# In[19]:


wine['target_names']


# In[20]:


map_dict={0:'class_0',1:'class_1',2:'class_2'}


# # scaling wine data

# In[21]:


from sklearn.preprocessing import StandardScaler


# In[22]:


scaler=StandardScaler()


# In[23]:


scaler.fit(feature)


# In[24]:


scaler_feature=pd.DataFrame(scaler.transform(feature),columns=wine['feature_names'])


# In[25]:


scaler_feature.head()


# # model selection

# In[27]:


from sklearn.model_selection import train_test_split


# In[29]:


x_train,x_test,y_train,y_test=train_test_split(scaler_feature,target,test_size=0.2)


# In[31]:


x_train.head()


# In[32]:


y_train


# ## this is multi nomial classifaction problem 

# In[34]:


from sklearn.linear_model import LogisticRegressionCV


# In[35]:


model=LogisticRegressionCV(solver='newton-cg',multi_class='multinomial')


# ### fit model

# In[36]:


model.fit(x_train,y_train)


# In[38]:


pred=model.predict(x_test)


# In[40]:


pred[:5]


# In[ ]:





# In[41]:


y_test[:5]


# In[42]:


##check accurrecy


# In[43]:


from sklearn.metrics import accuracy_score,classification_report,confusion_matrix


# In[49]:


print(f"accuracy: {accuracy_score(y_test,pred)*100:.2f}")


# In[50]:


print(f"confusion matrix:\n\n",confusion_matrix(y_test,pred))


# In[51]:


print(f"classfication report",classification_report(y_test,pred))


# In[55]:


#predting with scaling


# In[54]:


xtrain,xtest,ytrain,ytest=train_test_split(feature,target,test_size=.02)


# In[56]:


model1=LogisticRegressionCV(solver='newton-cg',multi_class='multinomial')


# In[57]:


model1.fit(xtrain,ytrain)


# In[58]:


pred1=model1.predict(xtest)


# In[59]:


pred1[:5]


# In[60]:


ytest[:5]


# In[61]:


print(f"accuracy: {accuracy_score(ytest,pred1)*100:.2f}")


# In[63]:


print(f"confusion matrix:\n\n",confusion_matrix(ytest,pred1))


# In[64]:


print(f"classfication report",classification_report(ytest,pred1))


# In[ ]:




