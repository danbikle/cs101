#coding utf-8
"""
pubsub11.py

This script should publish work-tokens (wtkns) to a GCP topic list: topic10.

Next, with sub10, it should subscribe to one of the wtkns from topic10.

Demo:
python pubsub11.py
"""
from google.cloud import pubsub
from google.cloud import monitoring
import time
import subprocess as sp

PROJECT      = 'pubsub-197323'
TOPIC        = 'topic10'
SUBSCRIPTION = 'sub10'

def print_message(message):
    print(message.data)
    time.sleep(19)
    message.ack()

def main():
    # I should publish wtkn0_s to topic10:
    publisher = pubsub.PublisherClient()
    topic_s   = 'projects/'+PROJECT+'/topics/'+TOPIC
    for t_i in range(99):
        wtkn_s = str(t_i)
        publisher.publish(topic_s, wtkn_s)
    
    # I should open a connection to the message queue asynchronously
    flow_control = pubsub.types.FlowControl(max_messages=1)
    subscriber   = pubsub.SubscriberClient()
    sub_s = 'projects/'+PROJECT+'/subscriptions/'+SUBSCRIPTION
    subscription = subscriber.subscribe(sub_s, flow_control=flow_control)
    subscription.open(print_message)
    time.sleep(2)
    subscription.close()
    
if __name__ == '__main__':
    main()

'bye'
