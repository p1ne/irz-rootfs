#!/bin/sh /usr/lib/irz-web/setscript
formq usercron | tr -d '\r' > /mnt/rwfs/settings/usercron

if [ "`formq usercron_enabled`" = "on" ]; then
	chmod 0755 /mnt/rwfs/settings/usercron
else
	chmod 0644 /mnt/rwfs/settings/usercron
fi
/etc/init.d/cron restart
echo "<hr><a href=\"admin_usercron.cgi\">Return</a>"
