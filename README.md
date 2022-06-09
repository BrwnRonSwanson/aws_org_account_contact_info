# AWS Org Account Contact Information Script

This is a script that allows you to pull all the child account contact information from your AWS organization and place it in a data store such as an S3 bucket. This is a helpful script if you need to upload contact information in to a 3rd party tool. This is a handy little script if you have a SOC or other team that needs to know what account contact matches to which account number / name. 

Prerequisites:
1. Ensure you have Python3 installed and the AWS CLI
2. You must have access to your aws orginization account. (This is required to access child account contact information)
3. You must have access to create lambda functions (and S3 if you will be placing the exported files there)
4. Update the script bucket information ("INSERT BUCKET NAME HERE")
5. The script is written to run on Lambda. If you choose to run this locally, you must remove the "Lamnda Handler Function" and replace it with getAccounts()

Execution:
1. If running locally, make sure you are logged in to the AWS Org master account with the permissions above. The script will use this account to run.
2. The output file will be placed in the mentioned S3 bucket. You can alter this script to do a screen print out, excel or whatever you prefer.

Integrations:
If you have placed the output files in an S3 bucket, you can build integrations with 3rd party tools to pull the data from there.
