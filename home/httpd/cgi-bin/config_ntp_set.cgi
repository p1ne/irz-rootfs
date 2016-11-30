#!/bin/sh /usr/lib/irz-web/setscript
ntp_tz=$(formq ntp_tz)

cp /usr/share/zoneinfo/${ntp_tz:="GMT-04"} /mnt/rwfs/etc/localtime
echo -n "New local time: "
date

cat <<EOF > /mnt/rwfs/settings/settings.ntp
NTP_ENABLED=$(isOn $(formq ntp_enabled))
NTPDATE_ENABLED=$(isOn $(formq ntpdate_enabled))
NTPSERVER_ENABLED=$(isOn $(formq ntpserver_enabled))
NTP_PRIMARY_SERVER="`formq ntp_primary_server`"
NTP_SECONDARY_SERVER="`formq ntp_secondary_server`"
NTP_TZ="$ntp_tz"
EOF

echo "<pre>"
/etc/init.d/ntp restart
echo "</pre><hr><a href=\"config_ntp.cgi\">Return</a>"
