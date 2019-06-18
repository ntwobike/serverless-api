# Serverless-Api

This is a simple crud api use aws sam, created with aws ApiGateway, Lambda and DynamoDB.

# Before Deploy
- You need python >= 2.7
- You need aws sam cli https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html

- Create a role for lambda that can call Cloudwatch and Dynamodb, and replace role arn with `<role-for-lambda-to-call-cloudwatch-dynamodb>`
You need a s3 bucket to store the code, and pass that bucket name while you deploy.

- Also you can run locally check the sam doc https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-command-reference.html

# Deployment
Prepare the deployment file

    sam package --output-template-file <output-file-name.yaml> --s3-bucket <bucket-name>

deploy

    sam deploy --template-file <output-file-name.yaml> --stack-name event-tracker-api --region <region>