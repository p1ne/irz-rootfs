#!/bin/sh /usr/lib/irz-web/setscript
F=/mnt/rwfs/settings/settings.ovpns

ovpns_enabled=$(isOn $(formq ovpns_enabled))

#server
setValue $F OVPNS_ENABLED $ovpns_enabled
setValue $F OVPNS_PROTO `formq ovpns_proto`
setValue $F OVPNS_PORT `formq ovpns_port`
setValue $F OVPNS_CONFIG `formq ovpns_config | encode`
setValue $F OVPNS_CA_CERT `formq ovpns_ca_cert | encode`
setValue $F OVPNS_DH_PARAMS `formq ovpns_dh_params | encode`
setValue $F OVPNS_LOCAL_CERT `formq ovpns_local_cert | encode`
setValue $F OVPNS_LOCAL_KEY `formq ovpns_local_key | encode`

#clients
for i in `seq 1 5`; do
    setVale $F OVPN${i}_ENABLED $(isOn $(formq ovpn${i}_enabled))
done
echo "<pre>"
if [ "$ovpns_enabled" = "1" ]; then
    /etc/init.d/ovpn-serv restart
else
    /etc/init.d/ovpn-serv stop
fi

echo "</pre><hr><a href=\"config_ovpnserv.cgi\">Return</a>"
