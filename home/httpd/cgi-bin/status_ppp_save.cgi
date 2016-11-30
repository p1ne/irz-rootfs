#!/bin/sh
NAME=`cat /etc/hostname`
cat << EOF
Content-Type: application/force-download
Content-Encoding: us-ascii
Content-Description: File Transfer
Content-Disposition: attachment; filename="${NAME}-PPP.log"

EOF

echo "--- GSM info ---"
echo ""
gsminfo
echo ""
echo "--- Estimated traffic ---"
echo ""
pppinfo
echo ""
echo "--- Connection log ---"
echo ""

if [ -s /mnt/rwfs/settings/connection.log ]; then
    cat /mnt/rwfs/settings/connection.log
else
    echo "Log is empty."
fi


