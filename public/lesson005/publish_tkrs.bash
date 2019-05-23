#!/bin/bash

# publish_tkrs.bash

# This script should use gcloud to publish a list of tkrs to pub/sub.

# Later another script, workon_tkrs.bash, should work on the tkrs.

# Demo:
# bash ~/publish_tkrs.bash

export PROJECT=pubsub-197323
gcloud pubsub topics publish topic10 --message "Please work on FB now"   --project $PROJECT
gcloud pubsub topics publish topic10 --message "Please work on AAPL now" --project $PROJECT
gcloud pubsub topics publish topic10 --message "Please work on AMZN now" --project $PROJECT
gcloud pubsub topics publish topic10 --message "Please work on NFLX now" --project $PROJECT
gcloud pubsub topics publish topic10 --message "Please work on GOOG now" --project $PROJECT
gcloud pubsub topics publish topic10 --message "Please work on SPY now"  --project $PROJECT

exit
