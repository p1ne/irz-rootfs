#!/bin/sh /usr/lib/irz-web/setscript
en=$(isOn $(formq dyndns_enabled))
cat <<EOF > /mnt/rwfs/settings/settings.dyndns
DYNDNS_ENABLED=$en
DYNDNS_FORCE_UPDATE=$(isOn $(formq dyndns_force_updates))
DYNDNS_SYSTEM="`formq dyndns_system`"
DYNDNS_HOSTNAME="`formq dyndns_hostname`"
DYNDNS_USERNAME="`formq dyndns_username`"
DYNDNS_PASSWORD="`formq dyndns_password | encode`"
DYNDNS_NAME="`formq dyndns_name | encode`"
DYNDNS_URL="`formq dyndns_url | encode`"
DYNDNS_UPDATE_INTERVAL="`formq dyndns_update_interval`"
EOF
echo "<pre>"
#start/stop/reload inadyn
if [ -e /var/ppp/ip ]; then
	if [ "$en" = "1" ]; then
		/etc/init.d/dyndns restart
	else
		/etc/init.d/dyndns stop
	fi
fi
echo "</pre><hr><a href=\"config_dyndns.cgi\">Return</a>"
