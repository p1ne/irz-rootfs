#!/bin/sh /usr/lib/irz-web/setscript
formq script | tr -d '\r'  > /mnt/rwfs/settings/shutdown

if [ "`formq script_enabled`" = "on" ]; then
	chmod 0755 /mnt/rwfs/settings/shutdown
else
	chmod 0644 /mnt/rwfs/settings/shutdown
fi

echo "<hr><a href=\"admin_shutdown.cgi\">Return</a>"
