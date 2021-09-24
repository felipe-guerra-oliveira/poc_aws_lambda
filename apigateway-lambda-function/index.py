#!/bin/python
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def main(event, context):
    logger.debug('######## A função foi invocada [%s] ########' % (event))
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": 'Olá mundo!'
        })
    }

if __name__ == '__main__':
    print(main(None, None))
