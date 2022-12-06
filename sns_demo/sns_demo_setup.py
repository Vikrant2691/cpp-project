'''
    A simple demo on how to perform core operation with the SNS.
    
    Multiple threads are used to simulate the interaction of the different components (i.e. publisher and subscribers) with a SNS topic
'''
   
from topic_setup import MyTopic
from publisher import Publisher
from subscriber import Subscriber

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('topic_name', help='The name of the topic to work with or to create.')
    parser.add_argument('--create_topic', help='Create the topic. When not specified, the create_topic method is not executed.', action='store_true')
    parser.add_argument('--delete_topic', help='Delete the topic. When not specified, the topic is not deleted.', action='store_true')
    parser.add_argument('--setup_queue', help='Setup the queue specified via the --queue_name argument as a subscriber', action='store_true')
    parser.add_argument('--queue_name', help='The name of the queue, this servers as a subscriber of the SNS topic.')
    

  
    args = parser.parse_args()
    
    my_topic = MyTopic()
  
    if args.create_topic:
        my_topic.create_topic(args.topic_name)
    
    if args.setup_queue:
        a_subscriber = Subscriber(args.queue_name)
        a_subscriber.subscribe_to_topic(args.topic_name)
    
   
    if args.delete_topic:
        print('\n{} is being deleted!.'.format(args.topic_name))
        my_topic.delete_topic(args.topic_name)
    else:
        print('\n{} will not be deleted.'.format(args.topic_name))
      
    
    
if __name__ == '__main__':
 main()

