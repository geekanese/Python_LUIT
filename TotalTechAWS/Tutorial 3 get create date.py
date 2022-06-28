#!/usr/bin/env python
# coding: utf-8

# In[1]:


import boto3


# In[2]:


get_ipython().run_line_magic('pinfo2', 'boto3.client')


# In[4]:


s3_resource=boto3.client("s3")


# In[5]:


s3_resource.list_buckets()["Buckets"][0]["Name"]


# In[10]:


creation_date=s3_resource.list_buckets()["Buckets"][0]["CreationDate"]


# In[11]:


creation_date.strftime("%d%m%y_%H:%M:%s")


# In[12]:


for bucket in s3_resource.list_buckets()["Buckets"]:
    print(bucket["Name"])
    print(bucket["CreationDate"])


# In[ ]:




