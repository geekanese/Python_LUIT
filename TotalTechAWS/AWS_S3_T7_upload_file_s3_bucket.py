#!/usr/bin/env python
# coding: utf-8

# In[12]:


# tutorial 7


# In[13]:


# Upload file


# In[33]:


import boto3


# In[34]:


# how to upload single file
s3_resource=boto3.client("s3")
s3_resource.upload_file(
    Filename="sausage.jpeg",
    Bucket="geektest-t1",
    Key="uploadtest.jpeg")


# In[35]:


# how to upload multiple files
import os
import glob


# In[36]:


cwd=os.getcwd()


# In[37]:


cwd=cwd+"/upload/"


# In[38]:


files=glob.glob(cwd+"*.jpeg")


# In[39]:


files


# In[40]:


for file in files:
    s3_resource=boto3.client("s3")
    s3_resource.upload_file(
    Filename=file,
    Bucket="geektest-t1",
    Key=file.split("/")[-1])
    


# In[41]:


#files[0].split("/"


# In[ ]:




