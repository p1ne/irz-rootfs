#!/bin/sh /usr/lib/irz-web/setscript
CF=/mnt/rwfs/settings/settings.nat

echo "NAT_DISABLE_MASQ=$(isOn $(formq nat_disable_masq))" > $CF
echo "NAT_DEFAULT_ENABLED=$(isOn $(formq nat_default_enabled))" >> $CF
echo "NAT_DEFAULT_IPADDR=$(formq nat_default_ipaddr)" >> $CF
echo "NAT_UPNP_ENABLED=$(isOn $(formq nat_upnp_enabled))" >> $CF

for i in `seq 1 10`; do
    eval echo "NAT_PORT${i}_PUBLIC=`formq nat_port${i}_public`"
    eval echo "NAT_PORT${i}_PRIVATE=`formq nat_port${i}_private`"
    eval echo "NAT_PORT${i}_TYPE=`formq nat_port${i}_type`"
    eval echo "NAT_PORT${i}_IPADDR=`formq nat_port${i}_ipaddr`"
done >> $CF

echo "<pre>"
/etc/init.d/pfwd restart
/etc/init.d/miniupnp restart
echo "</pre><hr><a href=\"config_nat.cgi\">Return</a>"
