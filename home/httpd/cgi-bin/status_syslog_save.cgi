#!/bin/sh

NAME=`cat /etc/hostname`
cat << EOF
Content-Type: application/force-download
Content-Encoding: us-ascii
Content-Description: File Transfer
Content-Disposition: attachment; filename="${NAME}-syslog.log"

EOF

if [ -e "/mnt/usb/messages" ]; then
    cat /mnt/usb/messages
else
    cat /var/log/messages
fi
