#!/bin/sh
HOME_DIR=`pwd`

source $HOME_DIR/notification-env/bin/activate

NOTIFICATION_SERVICE_URL=

python3 test_index.py