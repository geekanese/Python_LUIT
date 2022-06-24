Using Python boto3 library & other AWS Services
https://aws.amazon.com/sdk-for-python/
Boto3 documentation — Boto3 Docs 1.24.9 documentation

I was assigned Project A


Using Python boto3 library & other AWS Services 
https://aws.amazon.com/sdk-for-python/
https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

**Project A**

Scenario: Our DevOps engineering team often uses a development lab to test releases of our application. 
The Managers are complaining about the rising cost of our development lab and need to save money by 
stopping our (for this example) 3 ec2 instances after all engineers are clocked out. 

**Create a Python script that you can run that will stop all instances.**

ADVANCED

We want to ensure that only our Development instances are stopped to make sure nothing in Production is accidentally stopped. 
Add logic to your script that only stops **running** instances that have the **Environment: Dev** tag.

COMPLEX

Use your script in a Lambda function using Python 3.7 or higher runtime. Make sure the lambda runs on a set schedule daily. 
No one should be working in the Dev environment past 7pm. (Note: to test you may need to modify the time accordingly so you 
aren't waiting for 7pm)


**Project B**

All code should be inline commented.

1. Create a DynamoDB table for something of your choosing (e.g. movies, food, games).
2. Using the Gist (https://gist.github.com/zaireali649/0ec6b90155120cf508223788b7b86efc) 
    as a starting point, use boto3 and Python to add 10 or more items to the table.
3. Use boto3 and Python to scan the DynamoDB table.

ADVANCED

1) Use boto3 and Python to query a table, remove an item from a table, create a table, and delete a table.

COMPLEX

1) Create a lambda function using boto3 and Python to query a table, return an item from a table and remove/delete an item from a table.
2) Run a test of the lambda function to verify you were able to do all of the previous actions. 
3) Create APIs using API Gateway using the console that will each return query a table, return an item, delete an item by calling your lambda function. 
Note: You can reference the following documentation to point you in the right direction. The code they are using is NOT Python so take that 
into consideration: https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-dynamo-db.html