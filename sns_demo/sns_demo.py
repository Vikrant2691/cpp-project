'''
    A simple demo on how to perform core operation with the SNS.
    
    Multiple threads are used to simulate the interaction of the different components (i.e. publisher and subscribers) with a SNS topic
'''
   
from topic_setup import MyTopic
from publisher import Publisher
from subscriber import Subscriber


from threading import Thread

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('topic_name', help='The name of the topic to work with or to create.')
    parser.add_argument('--message', help='The message to be sent.')
    parser.add_argument('--mobile', help='The mobile number to send the message too.')
   

  
    args = parser.parse_args()
    
    my_topic = MyTopic()
  
   
    a_publisher = Publisher()
    
   
    
    if args.mobile != None:
        # SNS demo: application-to-person communication
        a_publisher.send_SMS_message(args.mobile, args.message)
    else:
        # SNS demo: application-to-application communication
        a_publisher.publish_message(args.topic_name, args.message)
        
    
    
    
if __name__ == '__main__':
 main()

