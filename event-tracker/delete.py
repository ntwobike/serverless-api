import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    table = dynamodb.Table(os.environ['TABLE_NAME'])
    response = responseBody = None
    
    table.delete_item(
            Key={
                'visitor_id': event['pathParameters']['id'],
            }
    )
        
    return {
        'statusCode': 200,
        'body':json.dumps('Deleted successfully')
    }
