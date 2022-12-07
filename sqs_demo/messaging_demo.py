'''
    A simple demo on how to perform core operation with the SQS queue.
    
    Multiple threads are used to simulate the interaction of the different components (i.e. producer and consumer) with the queue
'''
   
from queue_setup import MyMessageQueue
from producer import Producer
from consumer import Consumer

from threading import Thread

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('queue_name', help='The name of the queue to work with or to create.')
    parser.add_argument('--create_queue', help='Create the queue. When not specified, the create_queue method is not executed.', action='store_true')
    parser.add_argument('--delete_queue', help='Delete the queue. The messages in the queues will no longer be available!!  When not specified, the queue is not deleted.', action='store_true')

  
    args = parser.parse_args()
    
    my_queue = MyMessageQueue()
    a_producer = Producer()
    a_consumer = Consumer()
    
    if args.create_queue:
        my_queue.create_queue(args.queue_name)
    
    # # create multiple threads to simulate the interaction of the producer and consumer with the queue
    # thread1 = Thread(target=a_consumer.consume_message, args=(args.queue_name,))
       
    # message1 = "Hi there!"
    # thread2 = Thread(target=a_producer.send_message, args=(args.queue_name, message1))
    
    # message2 = '{"artist": "Pink Floyd","song": "Us and Them"}'
    # thread3 = Thread(target=a_producer.send_message, args=(args.queue_name, message2))
    
    # message3 = '{"artist": "Pink Floyd","song": "Another Brick in the Wall"}'
    # thread4 = Thread(target=a_producer.send_message, args=(args.queue_name, message3))
    
    # thread5 = Thread(target=a_consumer.consume_message, args=(args.queue_name,))
    
    # thread1.start()
    # thread2.start()
    # thread3.start()
    # thread4.start()
    # thread5.start()
    
  
    # thread1.join()
    # thread2.join()
    # thread3.join()
    # thread4.join()
    # thread5.join()
    
    # if args.delete_queue:
    #     print('\n{} is being deleted!.'.format(args.queue_name))
    #     my_queue.delete_queue(args.queue_name)
    # else:
    #     print('\n{} will not be deleted.'.format(args.queue_name))
      
    
    
if __name__ == '__main__':
 main()

