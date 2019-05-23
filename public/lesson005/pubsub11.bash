#!/bin/bash

# pubsub11.bash

# Ref:
# https://console.cloud.google.com/iam-admin/serviceaccounts
# https://cloud.google.com/pubsub/docs/quickstart-cli

# Before I run this script I should,
# create a service account via iam-admin/serviceaccounts page.
# I should give pub/sub-admin privileges to the account.
# When I create the account I should ask GCP to give me JSON file I later use to authenticate.

# Authentication demo:
# gcloud auth activate-service-account --key-file=mykey.json

gcloud pubsub topics create  topic11 sub11              --project pubsub-197323
gcloud pubsub topics publish topic11 --message "hello0" --project pubsub-197323
gcloud pubsub topics publish topic11 --message "hello1" --project pubsub-197323
gcloud pubsub topics publish topic11 --message "hello2" --project pubsub-197323
gcloud pubsub subscriptions pull --auto-ack sub11       --project pubsub-197323
gcloud pubsub topics delete  topic11 sub11              --project pubsub-197323

exit
