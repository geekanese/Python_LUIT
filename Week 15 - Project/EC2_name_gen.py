# Week 15 Project - Week two of Python coding/scripting
# Project author - Christopher Utley

# **EC2 Random Name Generator**

# Several departments share an AWS environment. You need to ensure that the EC2s are properly named and are unique so team members can easily tell who the EC2 instances belong to. Use Python to create your unique EC2 names that the users can then attach to the instances. The Python Script should:
# 1. Allow the user to input how many EC2 instances they want names for and output the same amount of unique names.
# 2. Allow the user to input the name of their department that is used in the unique name.
# 3. Generate random characters and numbers that will be included in the unique name.


# Add Random number generator Python library module "random"
import random
from random import seed
from random import random


# Prompt user to input the number of EC2 instances they require names for and output the same number of unique names



# Allow user to input the name of their department to use as identifier in the unique names

# Generate random characters and numbers to append to the department name
random.seed(a=None, version=2)
print(random.random)
