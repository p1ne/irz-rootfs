#!/bin/sh /usr/lib/irz-web/setscript
gre_num=`formq gre_num`
gre_enabled_new=$(isOn $(formq gre_enabled))
gre_enabled_old=`cat /mnt/rwfs/settings/settings.gre | grep "GRE${gre_num}_ENABLED" | sed -e 's/^.*=//'`

F=/mnt/rwfs/settings/settings.gre

setValue $F GRE${gre_num}_ENABLED $gre_enabled_new
setValue $F GRE${gre_num}_DESC `formq gre_desc | encode`
setValue $F GRE${gre_num}_REMOTE_IPADDR `formq gre_remote_ipaddr`
setValue $F GRE${gre_num}_SRC_IPADDR `formq gre_src_ipaddr`
setValue $F GRE${gre_num}_DST_IPADDR `formq gre_dst_ipaddr`
setValue $F GRE${gre_num}_REMOTE_NETWORK `formq gre_remote_network`
setValue $F GRE${gre_num}_REMOTE_NETMASK `formq gre_remote_netmask`
setValue $F GRE${gre_num}_TUNNEL_MASK `formq gre_tunnel_mask`
setValue $F GRE${gre_num}_TUNNEL_MTU `formq gre_tunnel_mtu`

#start/stop/reload gre
echo "<pre>"
if [ $gre_enabled_new = "1" ]; then
	if [ $gre_enabled_old = "1" ]; then
		/etc/init.d/gre restart $gre_num
	else
		/etc/init.d/gre start $gre_num
	fi
else
	/etc/init.d/gre stop $gre_num
fi
echo "</pre><hr><a href=\"config_gre.cgi\">Return</a>"
