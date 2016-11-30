#!/bin/sh /usr/lib/irz-web/setscript
[ "`formq enabled`" = "on" ] && snmp_enabled="yes" || snmp_enabled="no"
[ "`formq auth`" = "on" ] && require_auth="yes" || require_auth="no"
community=`formq community_string`
timeout=`formq timeout`

cat <<EOF > /mnt/rwfs/settings/settings.snmp
SNMP_COMMUNITY_STRING=${community:-"public"}
SNMP_DESCRIPTION="`formq description | encode`"
SNMP_LOCATION="`formq location | encode`"
SNMP_CONTACT="`formq contact | encode`"
SNMP_MOUNTPOINTS=/mnt/usb,/mnt/rwfs,/var
SNMP_INTERFACES=eth0,eth1,ppp0,ppp10,tun0,tap0,gre1,gre2,gre3,gre4,gre5,gre6,gre7,gre8,gre9,gre10
SNMP_REQUIRE_AUTH=$require_auth
SNMP_TIMEOUT=${timeout:-"1"}
SNMP_ENABLED=$snmp_enabled
EOF

regen_ident
echo "<pre>"
/etc/init.d/snmp stop
if [ "$snmp_enabled" = "yes" ]; then
    /etc/init.d/snmp start
fi
echo "</pre><hr><a href=\"config_snmp.cgi\">Return</a>"
