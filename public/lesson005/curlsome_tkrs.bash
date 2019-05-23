#!/bin/bash

curl http://tkrprice.herokuapp.com/static/CSV/history/FB.csv   > FB.csv
curl http://tkrprice.herokuapp.com/static/CSV/history/AAPL.csv > AAPL.csv
curl http://tkrprice.herokuapp.com/static/CSV/history/AMZN.csv > AMZN.csv
curl http://tkrprice.herokuapp.com/static/CSV/history/NFLX.csv > NFLX.csv
curl http://tkrprice.herokuapp.com/static/CSV/history/GOOG.csv > GOOG.csv
curl http://tkrprice.herokuapp.com/static/CSV/history/SPY.csv  > SPY.csv

exit
