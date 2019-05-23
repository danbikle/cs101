#coding utf-8
"""
pubsub10.py

This script should publish work-tokens (wtkns) to a GCP topic list: topic10.

Then it should add them to a file: gs://pubsub611/wtkns.txt

Next, with sub10, it should subscribe to one of the wtkns from topic10.

Then, it should add an empty file, wtkn0.txt, to gs://pubsub611/done_tkns/

Demo:
python pubsub10.py
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
    time.sleep(5)
    message.ack()

def main():
    # I should publish wtkn0_s to topic10:
    publisher = pubsub.PublisherClient()
    topic_s   = 'projects/'+PROJECT+'/topics/'+TOPIC
    wtkn0_s   = 'wtkn0'
    wtkn1_s   = 'wtkn1'
    wtkn2_s   = 'wtkn2'
    publisher.publish(topic_s, wtkn0_s)
    publisher.publish(topic_s, wtkn1_s)
    publisher.publish(topic_s, wtkn2_s)
    # I should write to wtkns.txt
    with open('wtkns.txt','a') as fh:
        fh.write('wtkn0'+"\n")
        fh.write('wtkn1'+"\n")
        fh.write('wtkn2'+"\n")
    # I should copy wtkns.txt to gs://pubsub611/wtkns.txt
    sp.check_call('gsutil cp wtkns.txt gs://pubsub611/',shell=True)
    
    # I should open a connection to the message queue asynchronously
    flow_control = pubsub.types.FlowControl(max_messages=1)
    subscriber   = pubsub.SubscriberClient()
    sub_s = 'projects/'+PROJECT+'/subscriptions/'+SUBSCRIPTION
    subscription = subscriber.subscribe(sub_s, callback=print_message, flow_control=flow_control)
    # What should happen here:
    # subscription.open(print_message)
    time.sleep(5)

    #    subscription.close()

if __name__ == '__main__':
    main()

'bye'
