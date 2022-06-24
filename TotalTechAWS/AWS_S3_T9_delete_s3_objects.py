#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Tutorial 9


# In[ ]:


#How to delete objects from S3


# In[26]:


import boto3


# In[27]:


s3_resource=boto3.client("s3")


# In[28]:


# Delete single object
s3_resource.delete_object(Bucket='geektest-t1',
      Key='sausage4.jpeg')


# In[29]:


# Delete multiple objects
import os
import glob


# In[30]:


# Find all objects from the bucket
objects=s3_resource.list_objects(Bucket="geektest-t1")["Contents"]


# In[31]:


#cwd=os.getcwd()


# In[32]:


#cwd=cwd+"/upload/"


# In[33]:


#files=glob.glob(cwd+"*.jpeg")


# In[34]:


len(objects)


# In[35]:


objects


# In[36]:


# iteration Delete objects in Bucket with response
for object in objects:
    response=s3_resource.delete_object(Bucket='geektest-t1',
      Key=object["Key"])
    print(response)


# In[25]:


# iteration Delete objects in Bucket
for object in objects:
      s3_resource.delete_object(Bucket='geektest-t1',
      Key=object["Key"])

