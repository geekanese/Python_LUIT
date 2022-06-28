#!/usr/bin/env python
# coding: utf-8

import boto3

client=boto3.client("ec2")

client.create_vpc(CidrBlock='10.0.0.0/16')


