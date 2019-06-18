import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    table = dynamodb.Table(os.environ['TABLE_NAME'])
    response = responseBody = None
    
    if event['pathParameters'] is None:
        response = table.scan()
        responseBody = response['Items']        

    elif "id" in event['pathParameters']:
        response = table.get_item(
            Key={
                'visitor_id': event['pathParameters']['id'],
            }
        )
        responseBody = response['Item']
        
    return {
        'statusCode': 200,
        'body':json.dumps(responseBody)
    }
