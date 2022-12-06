import logging
import boto3
from botocore.exceptions import ClientError

from queue_setup import MyMessageQueue

''' a simple class to demonstrate how to retrieve one or more messages from a given queue'''

class Subscriber:
    
    def __init__(self, name):
            self.name = name
            my_queue = MyMessageQueue()
            my_queue.create_queue(name)
          
            
            
    
    def subscribe_to_topic(self, topic_name):
        try:
            sqs_client = boto3.resource('sqs')
            # get an SQS.Queue instance that corresponds to the gueue with the given name
            queue = sqs_client.get_queue_by_name(QueueName=self.name)
            queue_arn = queue.attributes['QueueArn']
            
        
            sns_client = boto3.client('sns')
            # recall that if the topic already exists, the create_topic() method returns that topic's ARN
            response = sns_client.create_topic(Name=topic_name)
            topic_arn = response['TopicArn']
           
            print('Subscriber {} is subscribing to topic {}...'.format(self.name, topic_name))
            sns_client.subscribe(TopicArn=topic_arn, Protocol='sqs', Endpoint=queue_arn)
           
        except ClientError as e:
            logging.error(e)
            return False
        return True
        
