from asyncio import exceptions
import boto3
import botocore.config
import botocore.exceptions
import datetime

org = boto3.client('organizations')
org_bucket = boto3.client('s3')

def getAccounts():
    key_name = 'account-info' + str(datetime.date.today())
    response = org.list_accounts()
    results = response['Accounts']

    while 'NextToken' in response:
        response = org.list_accounts(NextToken=response['NextToken'])
        results.extend(response['Accounts'])

    org_bucket.put_object(Bucket="<insert bucket name here>", Body=results, Key=key_name)

def lambda_handler(event, context):
    try:
        getAccounts()
    except botocore.exceptions.ClientError as error:
        print(error)

        
    