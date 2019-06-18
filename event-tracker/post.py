import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    table = dynamodb.Table(os.environ['TABLE_NAME'])    
    user = json.loads(event['body'])['user']
    response = None
    
    table.put_item(
        Item={
           'visitor_id': user['visitor_id'],
           'anonym_ip': user['anonym_ip'],
           'device': user['device'],
           'user_agent': user['user_agent'],
           'logged_in': user['logged_in'],
           'encrypted_email': user['encrypted_email']
           
        }
    )
    print()
    return {
        'statusCode': 201,
        'body': json.dumps('User saved successfully')
    }
