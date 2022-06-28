#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Tutorial 22 - How to remove AWS VPC


# In[2]:


import boto3


# In[3]:


client=boto3.client("ec2")


# In[8]:


client.delete_vpc


# In[9]:


response = client.delete_vpc(
    VpcId='string'
    
)      


# In[ ]:




