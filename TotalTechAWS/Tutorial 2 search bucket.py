#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import boto3


# In[21]:


resource=boto3.resource


# In[22]:


resource=boto3.resource("s3")


# In[23]:


bucket_list=list(resource.buckets.all())


# In[24]:


len(bucket_list)


# In[25]:


for bucket in resource.buckets.all():
              print(bucket.name)


# In[ ]:




