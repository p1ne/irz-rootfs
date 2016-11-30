#!/bin/sh /usr/lib/irz-web/setscript
F=/mnt/rwfs/settings/settings.wifi
[ -r $F ] && . $F

wifi_ipaddr=`formq wifi_ipaddr`
wifi_netmask=`formq wifi_netmask`
dhcp=$(isOn $(formq dhcp_enabled))

cat <<EOF > $F
WIFI_IPADDR=$wifi_ipaddr
WIFI_NETMASK=$wifi_netmask
WIFI_DHCP_ENABLED=$dhcp
WIFI_DHCP_POOL_LO=`formq dhcp_pool_lo`
WIFI_DHCP_POOL_HI=`formq dhcp_pool_hi`
WIFI_DHCP_DEF=`formq dhcp_def`
WIFI_DHCP_MAX=`formq dhcp_max`
WIFI_DHCP_STATIC=$(isOn $(formq dhcp_static))
EOF

for i in `seq 1 5`; do
    echo "WIFI_DHCP_NAME${i}=`formq dhcp_name${i}`"
    echo "WIFI_DHCP_MAC${i}=`formq dhcp_mac${i}`"
    echo "WIFI_DHCP_IP${i}=`formq dhcp_ip${i}`"
done >> $F

cat <<EOF >> $F

WIFI_MODE=`formq wifi_mode`

WIFI_AP_SSID=`formq wifi_ap_ssid`
WIFI_AP_PASS=`formq wifi_ap_pass`
WIFI_AP_AUTH=`formq wifi_ap_auth`

WIFI_CLIENT_SSID=`formq wifi_client_ssid`
WIFI_CLIENT_BSSID=`formq wifi_client_bssid`
WIFI_CLIENT_PASS=`formq wifi_client_pass`
WIFI_CLIENT_AUTH=`formq wifi_client_auth`

EOF

echo "<pre>"
## if interface settings changed - reboot
if [ "$WIFI_IPADDR" != "$wifi_ipaddr" ] || [ "$WIFI_NETMASK" != "$wifi_netmask" ]; then
    echo "WIFI configuration was changed"
    echo "Router is rebooting"
    echo "</pre><hr>"
	echo "Please wait one minute and <a href=http://"$eth_ipaddr">click here to return</a>"
	echo "<meta http-equiv=\"refresh\" content=\"60;url=http://"$eth_ipaddr"\"/>"
	(sleep 5;reboot)&
	exit 0
else
    /etc/init.d/network restart

	if [ "$dhcp" = "1" ]; then
		if [ -e /var/run/dhcpd.pid ]; then
			/etc/init.d/dhcp-server stop
		fi
		/etc/init.d/dhcp-config start
		/etc/init.d/dhcp-server start
	else
		/etc/init.d/dhcp-server stop
	fi
fi

echo "</pre><hr><a href=\"config_wifi.cgi\">Return</a>"
