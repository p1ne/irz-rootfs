#!/bin/sh /usr/lib/irz-web/setscript

formq upscript | tr -d '\r' > /mnt/rwfs/settings/ipup
if [ "`formq script_enabled`" = "on" ]; then
	chmod 0755 /mnt/rwfs/settings/ipup
else
	chmod 0644 /mnt/rwfs/settings/ipup
fi

echo "<hr><a href=\"admin_ipup.cgi\">Return</a>"
