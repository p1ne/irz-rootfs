#!/bin/sh /usr/lib/irz-web/setscript

dec_addr=`formq ping_address`
ping_size=`formq ping_size`
ping_count=`formq ping_count`

echo "<pre>"
if [ -z "$dec_addr" -o -z "$ping_count" ]; then
	echo "Wrong ping address or ping count!"
else
	ping $dec_addr -c $ping_count -s ${ping_size:-"56"} 2>&1
fi
echo "</pre>"
echo "<hr><a href=\"admin_pingtest.cgi\">Return</a>"
