import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    table = dynamodb.Table(os.environ['TABLE_NAME'])    
    user = json.loads(event['body'])['user']
    response = None
    
    updatedRecord = table.update_item(
        Key={
                'visitor_id': event['pathParameters']['id']
            },
        # UpdateExpression: "SET anonym_ip = :cd",
        UpdateExpression = "SET anonym_ip = :anonym_ip, device= :device, user_agent= :user_agent, logged_in= :logged_in, encrypted_email= :encrypted_email",
        ExpressionAttributeValues = {
            ":anonym_ip": user['anonym_ip'],
            ":device":user['device'],
            ":user_agent":user['user_agent'],
            ":logged_in":user['logged_in'],
            ":encrypted_email":user['encrypted_email']
        },
        ReturnValues = "UPDATED_NEW"
    )

    responseBody = updatedRecord['Attributes']
    return {
        'statusCode': 200,
        'body': json.dumps(responseBody)
    }
