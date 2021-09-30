#!/usr/bin/env python
import unittest

from index import *

class TestLambdaHanlder(unittest.TestCase):
    def test_main(self):
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
        response = main(event, None)
        self.assertEqual(200, response['statusCode'])

if __name__ == '__main__':
    unittest.main()