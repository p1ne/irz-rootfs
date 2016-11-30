#!/bin/sh
NAME=`cat /etc/hostname`
cat << EOF
Content-Type: application/force-download
Content-Encoding: us-ascii
Content-Description: File Transfer
Content-Disposition: attachment; filename="${NAME}-DYNDNS.log"

EOF

[ -s /var/log/inadyn.log.2.gz ] && zcat /var/log/inadyn.log.2.gz
[ -s /var/log/inadyn.log.1.gz ] && zcat /var/log/inadyn.log.1.gz
[ -s /var/log/inadyn.log ] && cat /var/log/inadyn.log


