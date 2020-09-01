import json
import boto3

def handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('movies_table')



    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': 'Waaazzzaaaaaaa!!!\n'
    }
