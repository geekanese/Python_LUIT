#!/usr/bin/env python3.7
# Week 14 Project - Week one of Python coding/scripting
# Project author - Christopher Utley
#
# Project requirements - Create a list of services using Python. i.e. S3, Lambda, EC2, etc
# 1. Create an empty list of AWS Services using Python
# 2. Populate the list using append or insert
# 3. Print the list and print the length of the list
# 4. Remove two specific services from the list by name or by index
# 5. Print the new list and the new length of the list
#
#
    #Create an empty list of AWS Services
list = []

    # Populate the list using append
print(list)
list.append ('WorkSpaces'),
list.append ('Cloud9'),
list.append ('AWS DeepRacer'),
list.append ('Glacier'),
list.append ('Ground Station'),
list.append ('Amazon Braket')


    # Print the list and print the length of the list
print(list)
len(list)

print ("This is a list of AWS services", list, "This is the length of this list", len(list))
    
    # Remove two specific services from the list by name or by index
del list[1]
del list[2]
new_list = list

    
    # Print the new list and the new length of the list
print(new_list)
print(len(new_list))
print("New length of updated list", len(new_list))
