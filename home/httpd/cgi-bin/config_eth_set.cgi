#!/bin/sh /usr/lib/irz-web/setscript
F=/mnt/rwfs/settings/settings.eth
[ -r $F ] && . $F

eth_ipaddr=`formq eth_ipaddr`
eth_netmask=`formq eth_netmask`
dhcp=$(isOn $(formq dhcp_enabled))

cat <<EOF > $F
ETH_IPADDR=$eth_ipaddr
ETH_NETMASK=$eth_netmask
ETH_SECONDARY=$(isOn $(formq eth_secondary))
ETH_IPADDR2=`formq eth_ipaddr2`
ETH_NETMASK2=`formq eth_netmask2`
ETH_USB_LAN=$(isOn $(formq usb_lan))
ETH_IPADDR3=`formq eth_ipaddr3`
ETH_NETMASK3=`formq eth_netmask3`
ETH_DHCP_ENABLED=$dhcp
ETH_DHCP_POOL_LO=`formq dhcp_pool_lo`
ETH_DHCP_POOL_HI=`formq dhcp_pool_hi`
ETH_DHCP_DEF=`formq dhcp_def`
ETH_DHCP_MAX=`formq dhcp_max`
ETH_DHCP_STATIC=$(isOn $(formq dhcp_static))
EOF

for i in `seq 1 5`; do
    echo "ETH_DHCP_NAME${i}=`formq dhcp_name${i}`"
    echo "ETH_DHCP_MAC${i}=`formq dhcp_mac${i}`"
    echo "ETH_DHCP_IP${i}=`formq dhcp_ip${i}`"
done >> $F

cat <<EOF >> $F
ETH_RESERVE=$(isOn $(formq eth_reserve))
ETH_RESERVE_TARGET=`formq eth_reserve_target`
ETH_RESERVE_ROUTER=`formq eth_reserve_router`
ETH_RESERVE_INTERVAL=`formq eth_reserve_interval`
ETH_RESERVE_IFACE=`formq eth_reserve_iface`
ETH_RESERVE_PPPON=`formq eth_reserve_pppon`
ETH_MII_FORCE=$(isOn $(formq eth_force_media))
ETH_MII_MEDIA=`formq eth_force_media_type`
ETH_MII_DUPLEX=`formq eth_force_media_duplex`
EOF

echo "<pre>"
## if interface settings changed - reboot
if [ "$ETH_IPADDR" != "$eth_ipaddr" ] || [ "$ETH_NETMASK" != "$eth_netmask" ]; then
    echo "LAN configuration was changed"    
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

echo "</pre><hr><a href=\"config_eth.cgi\">Return</a>"
