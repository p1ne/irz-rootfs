#!/bin/sh
NAME=`cat /etc/hostname`
cat << EOF
Content-Type: application/force-download
Content-Encoding: us-ascii
Content-Description: File Transfer
Content-Disposition: attachment; filename="${NAME}-OpenVPN.log"

EOF

if [ -e /var/log/openvpn.log ]; then
    cat /var/log/openvpn.log
else
    echo "OpenVPN Tunnel is stopped."
fi
