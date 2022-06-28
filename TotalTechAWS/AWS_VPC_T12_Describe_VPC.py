#!/usr/bin/env python
# coding: utf-8

#Tutorial 12, How to describe VPC using Python
#
import boto3
client=boto3.client("ec2")

# how to describe all VPC available in your account
client.describe_vpcs()
x=client.describe_vpcs()

# Create variable no_of_vpcs
no_of_vpcs=x["Vpcs"]

# Output the number of VPCs in use
len(no_of_vpcs)

# Output the VPC names in a list
for vpc in no_of_vpcs:
    print(vpc["VpcId"])
