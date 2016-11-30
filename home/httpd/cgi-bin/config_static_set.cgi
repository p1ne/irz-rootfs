#!/bin/sh /usr/lib/irz-web/setscript

echo "<pre>"
## remove old routes
/etc/init.d/static stop

## save settings
for i in `seq 1 5`; do
    eval echo "STATIC_NETWORK${i}=`formq static_network${i}`"
    eval echo "STATIC_NETMASK${i}=`formq static_netmask${i}`"
    eval echo "STATIC_GATEWAY${i}=`formq static_gateway${i}`"
    eval echo "STATIC_DEVICE${i}=`formq static_device${i}`"
done > /mnt/rwfs/settings/settings.static

## Add new routes
/etc/init.d/static start
echo "</pre><hr><a href=\"config_static.cgi\">Return</a>"
