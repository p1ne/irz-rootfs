#!/bin/sh
NAME=`cat /etc/hostname`
cat << EOF
Content-Type: application/force-download
Content-Encoding: us-ascii
Content-Description: File Transfer
Content-Disposition: attachment; filename="${NAME}-OpenVPN_Server.log"

EOF

if [ -e /var/log/ovpn-serv.log ]; then
    cat /var/log/ovpn-serv.log
else
    echo "OpenVPN Server is stopped."
fi
