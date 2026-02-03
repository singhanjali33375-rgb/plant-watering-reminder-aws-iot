import json
import boto3

sns = boto3.client('sns')

THRESHOLD = 30
SNS_TOPIC_ARN = "arn:aws:sns:region:account-id:plant-watering-alert"

def lambda_handler(event, context):
    moisture = event['moisture']

    if moisture < THRESHOLD:
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=f"Soil moisture is low ({moisture}%). Please water your plant."
        )

    return {
        'statusCode': 200,
        'body': json.dumps('Processed successfully')
    }
