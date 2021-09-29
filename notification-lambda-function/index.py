#!/bin/python
import logging
import os
import json

import requests

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def post_event(message_event):
    notification_url = None
    json_data = None
    response = None
    #custom headers
    headers = {
        "content-type": "application/json; charset=utf8"
    }
    try:
        notification_url = os.getenv('NOTIFICATION_SERVICE_URL')
        #create JSON message
        json_data = {
            "text": message_event
        }
        response = requests.post(notification_url, headers=headers, data=json.dumps(json_data))
        return response
    except Exception as e:
        logger.error(('Erro na tentativa de postar uma mensagem: [%s]') % (e))
        raise e

def main(event, context):
    try:
        response = post_event(event['Records'][0]['Sns']['Message'])

        return {
            "statusCode": response.status_code,
            "body": json.dumps({
                "message": response.text
            })
        }
    except Exception as e:
        logger.error(('Erro na integração com o Slack %s') % (e))
        raise e

if __name__ == '__main__':
    event = {
        "Records": [
            {
            "EventSource": "aws:sns",
            "EventVersion": "1.0",
            "EventSubscriptionArn": "arn:aws:sns:us-east-1:9999999999:ExampleTopic",
            "Sns": {
                "Type": "Notification",
                "MessageId": "95df01b4-ee98-5cb9-9903-4c221d41eb5e",
                "TopicArn": "arn:aws:sns:us-east-1:123456789012:ExampleTopic",
                "Subject": "example subject",
                "Message": "Text 1",
                "Timestamp": "1970-01-01T00:00:00.000Z",
                "SignatureVersion": "1",
                "Signature": "EXAMPLE",
                "SigningCertUrl": "EXAMPLE",
                "UnsubscribeUrl": "EXAMPLE",
                "MessageAttributes": {
                "Test": {
                    "Type": "String",
                    "Value": "TestString"
                },
                "TestBinary": {
                    "Type": "Binary",
                    "Value": "TestBinary"
                }
                }
            }
            }
        ]
    }
    print(main(event, None))