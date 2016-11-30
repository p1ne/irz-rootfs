#!/bin/sh /usr/lib/irz-web/setscript

formq downscript | tr -d '\r' > /mnt/rwfs/settings/ipdown
if [ "`formq script_enabled`" = "on" ]; then
	chmod 0755 /mnt/rwfs/settings/ipdown
else
	chmod 0644 /mnt/rwfs/settings/ipdown
fi

echo "<hr><a href=\"admin_ipdown.cgi\">Return</a>"
