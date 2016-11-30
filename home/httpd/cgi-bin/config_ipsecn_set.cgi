#!/bin/sh /usr/lib/irz-web/setscript
F=/mnt/rwfs/settings/settings.ipsec

tun=`formq tun "$QUERY_STRING"`
ipsec_enabled=$(isOn $(formq ipsec_enabled))
ipsec_key_life=`formq ipsec_key_life`
ipsec_ike_life=`formq ipsec_ike_life`
ipsec_rekey_margin=`formq ipsec_rekey_margin`
ipsec_rekey_fuzz=`formq ipsec_rekey_fuzz`

setValue $F IPSEC${tun}_ENABLED $ipsec_enabled
setValue $F IPSEC${tun}_DESC `formq ipsec_desc | encode`
setValue $F IPSEC${tun}_REMOTE_IPADDR `formq ipsec_remote_ipaddr`
setValue $F IPSEC${tun}_REMOTE_ID `formq ipsec_remote_id`
setValue $F IPSEC${tun}_REMOTE_NETWORK `formq ipsec_remote_network`
setValue $F IPSEC${tun}_REMOTE_NETMASK `formq ipsec_remote_netmask`
setValue $F IPSEC${tun}_LOCAL_ID `formq ipsec_local_id`
setValue $F IPSEC${tun}_LOCAL_NETWORK `formq ipsec_local_network`
setValue $F IPSEC${tun}_LOCAL_NETMASK `formq ipsec_local_netmask`
setValue $F IPSEC${tun}_PSK `formq ipsec_psk | encode`
setValue $F IPSEC${tun}_KEY_LIFE ${ipsec_key_life:-"3600"}
setValue $F IPSEC${tun}_IKE_LIFE ${ipsec_ike_life:-"3600"}
setValue $F IPSEC${tun}_REKEY_MARGIN ${ipsec_rekey_margin:-"540"}
setValue $F IPSEC${tun}_REKEY_FUZZ ${ipsec_rekey_fuzz:-"100"}
setValue $F IPSEC${tun}_NAT_TRAVERSAL `formq ipsec_nat_traversal`
setValue $F IPSEC${tun}_AGGRESSIVE `formq ipsec_aggressive`
setValue $F IPSEC${tun}_VERIFY_CERT `formq ipsec_verify_cert`
setValue $F IPSEC${tun}_AUTHBY `formq ipsec_authby`
setValue $F IPSEC${tun}_CA_CERT `formq ipsec_ca_cert | encode`
setValue $F IPSEC${tun}_REMOTE_CERT `formq ipsec_remote_cert | encode`
setValue $F IPSEC${tun}_LOCAL_CERT `formq ipsec_local_cert | encode`
setValue $F IPSEC${tun}_LOCAL_KEY `formq ipsec_local_key | encode`
setValue $F IPSEC${tun}_LOCAL_PASS `formq ipsec_local_pass | encode`
setValue $F IPSEC${tun}_LOCAL_IP `formq ipsec_local_ip`
setValue $F IPSEC${tun}_P1ENCALG `formq ipsec_p1encalg`
setValue $F IPSEC${tun}_P1HASHALG `formq ipsec_p1hashalg`
setValue $F IPSEC${tun}_P1DHGROUP `formq ipsec_p1dhgroup`
setValue $F IPSEC${tun}_P2ENCALG `formq ipsec_p2encalg`
setValue $F IPSEC${tun}_P2AUTHALG `formq ipsec_p2authalg`
setValue $F IPSEC${tun}_P2PFSGROUP `formq ipsec_p2pfsgroup`
setValue $F IPSEC${tun}_MY_TYPE `formq ipsec_my_type`
setValue $F IPSEC${tun}_MY_IDENTIFIER `formq ipsec_my_identifier | encode`
setValue $F IPSEC${tun}_PEERS_TYPE `formq ipsec_peers_type`
setValue $F IPSEC${tun}_PEERS_IDENTIFIER `formq ipsec_peers_identifier | encode`
setValue $F IPSEC${tun}_VERIFY_IDENTIFIER $(isOn $(formq ipsec_verify_identifier))
setValue $F IPSEC${tun}_PINGTEST_IP `formq ipsec_pingtest_ip`
setValue $F IPSEC${tun}_PINGTEST_INT `formq ipsec_pingtest_int`
setValue $F IPSEC${tun}_LEVEL `formq ipsec_level`

echo "<pre>"
if [ "$ipsec_enabled" = "1" ]; then
	if [ -e /var/run/racoon.pid ]; then
		/etc/init.d/ipsec-tools restart
	else
		/etc/init.d/ipsec-tools start
	fi
else
	/etc/init.d/ipsec-tools stop
fi
echo '</pre><hr><a href="config_ipsec.cgi">Return</a>'
