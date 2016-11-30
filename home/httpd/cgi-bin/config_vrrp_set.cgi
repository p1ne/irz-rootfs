#!/bin/sh /usr/lib/irz-web/setscript

cat <<EOF > /mnt/rwfs/settings/settings.vrrp
VRRP_ENABLE=$(isOn $(formq vrrp_enable))
VRRP_PASSWORD="`formq vrrp_password | encode`"
VRRP_AUTH=`formq vrrp_auth`
VRRP_INSTANCE=`formq vrrp_instance`
VRRP_IP=`formq vrrp_ip`
VRRP_ROUTER_ID=`formq vrrp_router_id`
VRRP_PRIORITY=`formq vrrp_priority`
VRRP_SMTP=`formq vrrp_smtp`
VRRP_SRV_MAIL=`formq vrrp_srv_mail`
VRRP_EMAIL=`formq vrrp_email`
EOF
echo "<pre>"
/etc/init.d/vrrp configure
/etc/init.d/vrrp restart
echo "</pre><hr><a href=\"config_vrrp.cgi\">Return</a>"
