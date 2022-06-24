#!/usr/bin/env python
# coding: utf-8

# Upload file
import boto3

# how to upload single file
s3_resource=boto3.client("s3")
s3_resource.upload_file(
    Filename="sausage.jpeg",
    Bucket="geektest-t1",
    Key="uploadtest.jpeg")

# how to upload multiple files
import os
import glob

#Change Working Directory
cwd=os.getcwd()
cwd=cwd+"/upload/"

#Create files with Glob
files=glob.glob(cwd+"*.jpeg")

files

#Upload files
for file in files:
    s3_resource=boto3.client("s3")
    s3_resource.upload_file(
    Filename=file,
    Bucket="geektest-t1",
    Key=file.split("/")[-1])
    
#files[0].split("/"
