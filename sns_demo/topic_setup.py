import logging
import boto3
from botocore.exceptions import ClientError

''' a simple class to demonstrate one solution possible solution to create and delete a topic'''

class MyTopic:

    
    ''' creates a SNS topic and return the Amazon Resource Name (ARN) assigned to the created topic.'''
    def create_topic(self, topic_name):
        
        try:
            sns_client = boto3.client('sns')
            print('\ncreating the topic {}...'.format(topic_name))
            '''
                 Note that the documentation of the SNS Client API says that the create_topic method is 
                 "[...] This action is idempotent, so if the requester already owns a topic with the specified name, 
                 that topic's ARN is returned without creating a new topic."
            '''     
            response = sns_client.create_topic(Name=topic_name)
            print(response) # this is not really needed
            return response['TopicArn']
        
        except ClientError as e:
            logging.error(e)
            return False
        return True
        
    
    def delete_topic(self, topic_name):
        
        try:
            sns_client = boto3.client('sns')
            # recall that if the topic already exists, the create_topic() method returns that topic's ARN
            response = sns_client.create_topic(Name=topic_name)
            topic_arn = response['TopicArn']
            print('\ndeleting the topic {}...'.format(topic_name))
            sns_client.delete_topic(TopicArn=topic_arn)
           
            
        except ClientError as e:
            logging.error(e)
            return False
        return True
        
        
        