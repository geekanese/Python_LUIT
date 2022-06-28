#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# tutorial 8


# In[ ]:


# list objects from S3 bucket


# In[1]:


import boto3


# In[ ]:


# s3_resource=boto3.client("s3")??


# In[2]:


s3_resource=boto3.client("s3")


# In[7]:


#objects=s3_resource. ##tab after dot to get functions of s3_resource.##
#s3_resource.list_objects(Bucket="geektest-t1")["Contents"]


# In[9]:


objects=s3_resource.list_objects(Bucket="geektest-t1")["Contents"]


# In[15]:


len(objects)


# In[16]:


if len(objects)>0:
    print("objects exists")


# In[17]:


for object in objects:
    print(object)


# In[18]:


for object in objects:
    print(object["Key"])


# In[ ]:




