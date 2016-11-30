#!/bin/sh

NAME=`cat /etc/hostname`
cat << EOF
Content-Type: application/force-download
Content-Encoding: us-ascii
Content-Description: File Transfer
Content-Disposition: attachment; filename="${NAME}-iptables.log"

EOF

echo "Table: filter"
iptables -L -t filter -v -n
echo ""
echo "Table: nat"
iptables -L -t nat -v -n

