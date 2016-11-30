#!/bin/sh
DATE=`date +%F_%T|sed -e 's/:/-/g'`
NAME=`cat /etc/hostname`
cat << EOF
Content-Type: application/octet-stream
Content-Description: File Transfer
Content-Disposition: attachment; filename="${NAME}_settings_${DATE}.bin"

EOF

gzip -c /dev/mtd6 > /tmp/backup.gz
md5sum /tmp/backup.gz > /tmp/backup.md5
tar cf /tmp/backup.tar /tmp/backup.gz /tmp/backup.md5
cat /tmp/backup.tar

rm /tmp/backup.gz
rm /tmp/backup.md5

