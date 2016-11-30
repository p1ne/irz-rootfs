#!/bin/sh /usr/lib/irz-web/setscript
F=/mnt/rwfs/settings/settings.ipsec

for i in `seq 1 5`; do
    enabled=$(isOn $(formq ipsec${i}_enabled))
    setValue $F IPSEC${i}_ENABLED $enabled
    enabled_any=$(( $enabled_any + $enabled ))
done

echo "<pre>"
/etc/init.d/ipsec-tools stop
[ "$enabled_any" -gt 0 ] && /etc/init.d/ipsec-tools start
echo "</pre><hr><a href=\"config_ipsec.cgi\">Return</a>"
