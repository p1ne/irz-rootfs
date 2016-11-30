#!/bin/sh
NAME=`cat /etc/hostname`
cat << EOF
Content-Type: application/force-download
Content-Encoding: us-ascii
Content-Description: File Transfer
Content-Disposition: attachment; filename="${NAME}-LAN.log"

EOF
echo "--- Interfaces ---"
echo ""
ifconfig eth0
ifconfig eth0:0
ifconfig eth1
ifconfig ppp0
ifconfig tun0
ifconfig gre1
ifconfig gre2
ifconfig gre3
ifconfig gre4
ifconfig gre5
ifconfig gre6
ifconfig gre7
ifconfig gre8
ifconfig gre9
ifconfig gre10
echo ""
echo "--- Route table ---"
echo ""
route -n | grep -v "127.0.0" | tail -n+2
echo ""
echo "--- Ethernet Link ---"
echo ""
mii-diag eth0
