#!/usr/bin/env python
# coding: utf-8

# tutorial 8
# list objects from S3 bucket

import boto3
# s3_resource=boto3.client("s3")??
s3_resource=boto3.client("s3")

#objects=s3_resource. ##tab after dot to get functions of s3_resource.##
#s3_resource.list_objects(Bucket="geektest-t1")["Contents"]
objects=s3_resource.list_objects(Bucket="geektest-t1")["Contents"]

len(objects)

if len(objects)>0:
    print("objects exists")

for object in objects:
    print(object)

for object in objects:
    print(object["Key"])
