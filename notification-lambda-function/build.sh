#!/bin/sh
HOME_DIR=`pwd`

cp index.py ./notification-env/lib/python3.9/site-packages/

cd ./notification-env/lib/python3.9/site-packages/

zip -r ../../../../notification-function.zip .