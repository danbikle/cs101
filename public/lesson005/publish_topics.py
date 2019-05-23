# coding utf-8
"""
publish_topics.py

This script should publish many topics to pubsub.

Ref:
http://willcrichton.net/notes/gcp-job-queue/
https://github.com/willcrichton/gcp-job-queue

Demo:
python publish_topics.py
"""

from google.cloud import pubsub
from tqdm import tqdm

PROJECT = 'pubsub-197323'
TOPIC   = 'topic10'

def main():
    publisher  = pubsub.PublisherClient()
    topic_s    = 'projects/{}/topics/{}'.format(PROJECT, TOPIC)
    tkrs_l = ['FB','AAPL','AMZN','NFLX','GOOG','IBM','SPY','WMT','MSFT','XOM','ORCL','NVDA']
    for id in tqdm(tkrs_l):
        publisher.publish(topic_s, 'You should predict: '+id)

if __name__ == '__main__':
    main()
