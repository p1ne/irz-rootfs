#!/bin/sh /usr/lib/irz-web/setscript
CONF=/mnt/rwfs/settings/settings.openvpn
[ -e $CONF ] && . $CONF

new_openvpn_enabled=$(isOn $(formq openvpn_enabled))

cat <<EOF > $CONF
OPENVPN_ENABLED=$new_openvpn_enabled
OPENVPN_DEVICE=`formq openvpn_device`
OPENVPN_PROTO=`formq openvpn_proto`
OPENVPN_PORT=`formq openvpn_port`
OPENVPN_REMOTE_IPADDR=`formq openvpn_remote_ipaddr`
OPENVPN_REMOTE_NETWORK=`formq openvpn_remote_network`
OPENVPN_REMOTE_NETMASK=`formq openvpn_remote_netmask`
OPENVPN_REDIRECT_GW=`formq openvpn_redirect_gw`
OPENVPN_LOCAL_IF_IPADDR=`formq openvpn_local_if_ipaddr`
OPENVPN_REMOTE_IF_IPADDR=`formq openvpn_remote_if_ipaddr`
OPENVPN_PING_INTVL=`formq openvpn_ping_intvl`
OPENVPN_PING_TOUT=`formq openvpn_ping_tout`
OPENVPN_RENEG_SEC=`formq openvpn_reneg_sec`
OPENVPN_HAND_WINDOW=`formq openvpn_hand_window`
OPENVPN_INACTIVE=`formq openvpn_inactive`
OPENVPN_FRAGMENT=`formq openvpn_fragment`
OPENVPN_COMP=`formq openvpn_comp`
OPENVPN_NAT=`formq openvpn_nat`
OPENVPN_AUTH=`formq openvpn_auth`
OPENVPN_PING2_IP=`formq openvpn_ping2_ip`
OPENVPN_PING2_INT=`formq openvpn_ping2_int`
OPENVPN_PING2_ALLOW=`formq openvpn_ping2_allow`
OPENVPN_SECRET=`formq openvpn_secret | encode`
OPENVPN_CA_CERT=`formq openvpn_ca_cert | encode`
OPENVPN_DH_PARAMS=`formq openvpn_dh_params | encode`
OPENVPN_LOCAL_CERT=`formq openvpn_local_cert | encode`
OPENVPN_LOCAL_KEY=`formq openvpn_local_key | encode`
OPENVPN_USERNAME=`formq openvpn_username`
OPENVPN_PASSWORD=`formq openvpn_password`
OPENVPN_CONFIG_FILE=`formq openvpn_config_file | encode`
EOF

regen_ident
echo "<pre>"
if [ "$new_openvpn_enabled" = "1" ]; then
    if [ "$OPENVPN_ENABLED" = "1" ]; then
        /etc/init.d/openvpn stop
    fi
    /etc/init.d/openvpn start
    /etc/init.d/cron restart > /dev/null
else
    if [ "$OPENVPN_ENABLED" = "1" ]; then
        /etc/init.d/openvpn stop
    fi
fi

echo "</pre><hr><a href=\"config_openvpn.cgi\">Return</a>"
