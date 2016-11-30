#!/bin/sh /usr/lib/irz-web/setscript
formq script | tr -d '\r'  > /mnt/rwfs/settings/startup

if [ "`formq script_enabled`" = "on" ]; then
	chmod 0755 /mnt/rwfs/settings/startup
else
	chmod 0644 /mnt/rwfs/settings/startup
fi

echo "<hr><a href=\"admin_startup.cgi\">Return</a>"
