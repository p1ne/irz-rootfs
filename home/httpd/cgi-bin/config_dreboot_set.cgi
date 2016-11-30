#!/bin/sh /usr/lib/irz-web/setscript
cat <<EOF > /mnt/rwfs/settings/settings.dreboot
DREBOOT_ENABLED=$(isOn $(formq dreboot_enabled))
DREBOOT_HOURS="`formq dreboot_hours`"
DREBOOT_MINUTES="`formq dreboot_minutes`"
EOF
echo "<pre>"
/etc/init.d/cron restart
echo "</pre><hr><a href=\"config_dreboot.cgi\">Return</a>"
