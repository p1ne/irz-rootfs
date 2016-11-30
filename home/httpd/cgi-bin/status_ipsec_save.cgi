#!/bin/sh

NAME=`cat /etc/hostname`
cat << EOF
Content-Type: application/force-download
Content-Encoding: us-ascii
Content-Description: File Transfer
Content-Disposition: attachment; filename="${NAME}-ipsec.log"

EOF
LOG=/var/log/racoon.log
if [ -e "$LOG" ]; then
    cat  $LOG
else
    echo "IPSec disabled."
fi
