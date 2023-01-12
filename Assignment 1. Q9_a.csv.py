#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


data=pd.read_csv("Q9_a.csv")


# In[3]:


data


# In[4]:


data.skew()


# In[5]:


data.kurt()


# In[ ]:




