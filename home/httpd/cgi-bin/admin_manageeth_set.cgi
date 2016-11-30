#!/bin/sh
[ -e /mnt/rwfs/settings/settings.eth ] && . /mnt/rwfs/settings/settings.eth

# html starts
echo "Content-type: text/html"
echo ""

echo "Please wait...<hr>"
read POST_STRING
eth_enable=`echo "$POST_STRING" | sed -n 's/^.*eth_enable=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`

if [ "$eth_enable" = "on" ]; then
    . /mnt/rwfs/settings/settings.eth
    ifconfig eth0 up $ETH_IPADDR netmask $ETH_NETMASK up
else
    ifconfig eth0 down
fi
echo "<hr><a href=\"admin_manageeth.cgi\">Return</a>"
