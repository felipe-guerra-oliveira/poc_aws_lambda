#!/usr/bin/env python

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
