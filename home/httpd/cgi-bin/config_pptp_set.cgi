#!/bin/sh /usr/lib/irz-web/setscript

pptp_enabled=$(isOn $(formq pptp_enabled))
pptp_pap=$(isOn $(formq pptp_pap))
pptp_chap=$(isOn $(formq pptp_chap))
pptp_mppe=$(isOn $(formq pptp_mppe))

cat <<EOF > /mnt/rwfs/settings/settings.pptp
PPTP_ENABLED=$pptp_enabled
PPTP_SERVER_IP=`formq pptp_server_ip`
PPTP_PAP=$pptp_pap
PPTP_CHAP=$pptp_chap
PPTP_MPPE=$pptp_mppe
PPTP_USERNAME=`formq pptp_username`
PPTP_PASSWORD=`formq pptp_password`
PPTP_LOCAL_IP=`formq pptp_local_ip`
PPTP_REMOTE_IP=`formq pptp_remote_ip`
PPTP_REMOTE_NETWORK=`formq pptp_remote_network`
PPTP_REMOTE_NETMASK=`formq pptp_remote_netmask`
PPTP_PPP_OPTIONS="`formq pptp_ppp_options`"
EOF

echo "<pre>"
if [ "$pptp_enabled" = "1" ]; then
    /etc/init.d/pptp restart
else
    /etc/init.d/pptp stop
fi
echo "</pre><hr><a href=\"config_pptp.cgi\">Return</a>"
