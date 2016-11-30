#!/bin/sh /usr/lib/irz-web/setscript

l2tp_enabled=$(isOn $(formq l2tp_enabled))
cat <<EOF > /mnt/rwfs/settings/settings.l2tp
L2TP_ENABLED=$l2tp_enabled
L2TP_MODE=`formq l2tp_mode`
L2TP_SERVER_IP=`formq l2tp_server_ip`
L2TP_CLIENT_START=`formq l2tp_client_start`
L2TP_CLIENT_END=`formq l2tp_client_end`
L2TP_PORT=`formq l2tp_port`
L2TP_REDIAL_TIMEOUT=`formq l2tp_redial_timeout`
L2TP_DEFAULT_ROUTE=$(isOn $(formq l2tp_default_route))
L2TP_USERNAME=`formq l2tp_username`
L2TP_PASSWORD=`formq l2tp_password`
L2TP_LOCAL_IP=`formq l2tp_local_ip`
L2TP_REMOTE_IP=`formq l2tp_remote_ip`
L2TP_REMOTE_NETWORK=`formq l2tp_remote_network`
L2TP_REMOTE_NETMASK=`formq l2tp_remote_netmask`
EOF

echo "<pre>"
if [ "$l2tp_enabled" = "1" ]; then
    /etc/init.d/l2tp restart
else
    /etc/init.d/l2tp stop
fi
echo "</pre><hr><a href=\"config_l2tp.cgi\">Return</a>"
