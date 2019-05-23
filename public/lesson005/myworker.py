# coding utf-8
"""
myworker.py
This script should help me with pubsub demo.
Ref:
http://willcrichton.net/notes/gcp-job-queue/
https://github.com/willcrichton/gcp-job-queue
"""

from google.cloud import pubsub
import time

PROJECT      = 'pubsub-197323'
TOPIC        = 'topic10'
SUBSCRIPTION = 'sub10'

def handle_message(message):
    print(message.data)
    time.sleep(7) # Simulate delay due to work on message.
    message.ack()
    time.sleep(3) # help it think.

def main():
    subscriber   = pubsub.SubscriberClient()
    subscription = subscriber.subscribe(
        'projects/{}/subscriptions/{}'
        .format(PROJECT, SUBSCRIPTION))
    subscription.open(handle_message)
    time.sleep(7) # help it think.
    subscription.close()

if __name__ == '__main__':
    main()
