#!/bin/sh /usr/lib/irz-web/setscript
ovpn_num=`formq ovpn_num`
ovpn_enabled=$(isOn $(formq ovpn_enabled))

F=/mnt/rwfs/settings/settings.ovpns
setValue $F OVPN${ovpn_num}_ENABLED $ovpn_enabled
setValue $F OVPN${ovpn_num}_DESC `formq ovpn_desc | encode`
setValue $F OVPN${ovpn_num}_NAME `formq ovpn_name | encode`
setValue $F OVPN${ovpn_num}_CONFIG `formq ovpn_config | encode`
echo "<pre>"
if [ $ovpn_enabled = "1" ]; then
	if [ $OVPN_ENABLED = "1" ]; then
		/etc/init.d/ovpn-server restart 1
	else
		/etc/init.d/ovpn-server start 1
	fi
else
	/etc/init.d/ovpn-server stop 1
fi
echo "</pre><hr><a href=\"config_ovpnserv.cgi\">Return</a>"
