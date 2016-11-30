#!/bin/sh /usr/lib/irz-web/setscript
FILE=/mnt/rwfs/settings/settings.fw

echo "FW_MODE=`formq fw_mode`" > $FILE

for i in `seq 1 10`; do
    eval echo "FW_RULE${i}_TYPE=`formq fw_rule${i}_type`"
    eval echo "FW_RULE${i}_IPADDR=`formq fw_rule${i}_ipaddr`"
    eval echo "FW_RULE${i}_SUBNET=`formq fw_rule${i}_subnet`"
    eval echo "FW_RULE${i}_PROTO=`formq fw_rule${i}_proto`"
    eval echo "FW_RULE${i}_PORT=`formq fw_rule${i}_port`"
done >> $FILE
echo "<pre>"
/etc/init.d/fw restart
echo "</pre><hr><a href=\"config_firewall.cgi\">Return</a>"
