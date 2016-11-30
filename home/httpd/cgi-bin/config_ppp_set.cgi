#!/bin/sh

# html starts
echo "Content-type: text/html"
echo ""

echo "Please wait...<hr>"
read POST_STRING

#select sim card
new_simcard=`echo "$POST_STRING" | sed -n 's/^.*simcard=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
if [ -z "$new_simcard" ]; then
    echo "No parameters given!"
    echo "<hr><a href=\"config_ppp.cgi\">Return</a>"
    exit 0
fi
# sim1
tmp_ppp_apn=`echo "$POST_STRING" | sed -n 's/^.*ppp_apn=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
tmp_ppp_username=`echo "$POST_STRING" | sed -n 's/^.*ppp_username=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
tmp_ppp_password=`echo "$POST_STRING" | sed -n 's/^.*ppp_password=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
new_ppp_auth=`echo "$POST_STRING" | sed -n 's/^.*ppp_auth=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
new_ppp_pin=`echo "$POST_STRING" | sed -n 's/^.*ppp_pin=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
new_ppp_ipaddr=`echo "$POST_STRING" | sed -n 's/^.*ppp_ipaddr=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
new_ppp_ripaddr=`echo "$POST_STRING" | sed -n 's/^.*ppp_ripaddr=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
tmp_ppp_dial=`echo "$POST_STRING" | sed -n 's/^.*ppp_dial=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
new_ppp_mru=`echo "$POST_STRING" | sed -n 's/^.*ppp_mru=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
new_ppp_mtu=`echo "$POST_STRING" | sed -n 's/^.*ppp_mtu=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
new_ppp_roaming=`echo "$POST_STRING" | sed -n 's/^.*ppp_roaming=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
tmp_ppp_band=`echo "$POST_STRING" | sed -n 's/^.*ppp_band=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
new_ppp_usedns=`echo "$POST_STRING" | sed -n 's/^.*ppp_dns=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
new_ppp_dns_server=`echo "$POST_STRING" | sed -n 's/^.*ppp_dns_server=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
new_ppp_dns_secondary=`echo "$POST_STRING" | sed -n 's/^.*ppp_dns_secondary=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
tmp_ppp_mode=`echo "$POST_STRING" | sed -n 's/^.*ppp_mode=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
# sim2
tmp_ppp_apn2=`echo "$POST_STRING" | sed -n 's/^.*ppp_apn2=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
tmp_ppp_username2=`echo "$POST_STRING" | sed -n 's/^.*ppp_username2=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
tmp_ppp_password2=`echo "$POST_STRING" | sed -n 's/^.*ppp_password2=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
new_ppp_auth2=`echo "$POST_STRING" | sed -n 's/^.*ppp_auth2=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
new_ppp_pin2=`echo "$POST_STRING" | sed -n 's/^.*ppp_pin2=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
new_ppp_ipaddr2=`echo "$POST_STRING" | sed -n 's/^.*ppp_ipaddr2=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
new_ppp_ripaddr2=`echo "$POST_STRING" | sed -n 's/^.*ppp_ripaddr2=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
tmp_ppp_dial2=`echo "$POST_STRING" | sed -n 's/^.*ppp_dial2=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
new_ppp_mru2=`echo "$POST_STRING" | sed -n 's/^.*ppp_mru2=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
new_ppp_mtu2=`echo "$POST_STRING" | sed -n 's/^.*ppp_mtu2=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
new_ppp_roaming2=`echo "$POST_STRING" | sed -n 's/^.*ppp_roaming2=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
tmp_ppp_band2=`echo "$POST_STRING" | sed -n 's/^.*ppp_band2=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
new_ppp_usedns2=`echo "$POST_STRING" | sed -n 's/^.*ppp_dns2=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
new_ppp_dns_server2=`echo "$POST_STRING" | sed -n 's/^.*ppp_dns_server2=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
new_ppp_dns_secondary2=`echo "$POST_STRING" | sed -n 's/^.*ppp_dns_secondary2=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
tmp_ppp_mode2=`echo "$POST_STRING" | sed -n 's/^.*ppp_mode2=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
#ping settings
new_ppp_ping=`echo "$POST_STRING" | sed -n 's/^.*ppp_ping=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
new_ppp_ping_ipaddr=`echo "$POST_STRING" | sed -n 's/^.*ppp_ping_ipaddr=\([^&]*\).*$/\1/p' | sed "s/%20/ /g" | sed "s/%3B/;/g"`
new_ppp_ping_intvl=`echo "$POST_STRING" | sed -n 's/^.*ppp_ping_intvl=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
new_ppp_ping_repeat_intvl=`echo "$POST_STRING" | sed -n 's/^.*ppp_ping_repeat_intvl=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
new_ppp_ping_count=`echo "$POST_STRING" | sed -n 's/^.*ppp_ping_count=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
new_ppp_ping2=`echo "$POST_STRING" | sed -n 's/^.*ppp_ping2=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
new_ppp_ping_ipaddr2=`echo "$POST_STRING" | sed -n 's/^.*ppp_ping_ipaddr2=\([^&]*\).*$/\1/p' | sed "s/%20/ /g" | sed "s/%3B/;/g"`
new_ppp_ping_intvl2=`echo "$POST_STRING" | sed -n 's/^.*ppp_ping_intvl2=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
new_ppp_ping_repeat_intvl2=`echo "$POST_STRING" | sed -n 's/^.*ppp_ping_repeat_intvl2=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
new_ppp_ping_count2=`echo "$POST_STRING" | sed -n 's/^.*ppp_ping_count2=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
#maxfail and retry
new_ppp_switch=`echo "$POST_STRING" | sed -n 's/^.*ppp_switch=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
new_ppp_maxfail=`echo "$POST_STRING" | sed -n 's/^.*ppp_maxfail=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
new_ppp_tryprimary=`echo "$POST_STRING" | sed -n 's/^.*ppp_tryprimary=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
new_ppp_retry=`echo "$POST_STRING" | sed -n 's/^.*ppp_retry=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
new_ppp_reboot=`echo "$POST_STRING" | sed -n 's/^.*ppp_reboot=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
new_ppp_reboot_count=`echo "$POST_STRING" | sed -n 's/^.*ppp_reboot_count=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
new_ppp_persist=`echo "$POST_STRING" | sed -n 's/^.*ppp_persist=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
new_ppp_softretr=`echo "$POST_STRING" | sed -n 's/^.*ppp_softretr=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
#fix apn
new_ppp_apn=`post_decode $tmp_ppp_apn|encode`
new_ppp_apn2=`post_decode $tmp_ppp_apn2|encode`
#fix dial numbers
new_ppp_dial=`post_decode $tmp_ppp_dial`
new_ppp_dial2=`post_decode $tmp_ppp_dial2`
#fix usernames
new_ppp_username=`post_decode $tmp_ppp_username|encode`
new_ppp_username2=`post_decode $tmp_ppp_username2|encode`
#fix passwords
new_ppp_password=`post_decode $tmp_ppp_password|encode`
new_ppp_password2=`post_decode $tmp_ppp_password2|encode`
# fix GSM frequency
new_ppp_band=`post_decode $tmp_ppp_band`
new_ppp_band2=`post_decode $tmp_ppp_band2`
# set 2G/3G mode
ppp_mode=`post_decode $tmp_ppp_mode`
ppp_mode2=`post_decode $tmp_ppp_mode2`

if [ "$new_simcard" = "0" ]; then
    ppp_en="0"
else
    ppp_en="1"
fi

if [ "$new_ppp_switch" = "on" ]; then
    switch="1"
else
    switch="0"
fi

if [ "$new_ppp_tryprimary" = "on" ]; then
    tryprimary="1"
else
    tryprimary="0"
fi

if [ "$new_ppp_reboot" = "on" ]; then
    reboot="1"
else
    reboot="0"
fi

if [ "$new_ppp_persist" = "on" ]; then
    persist="1"
else
    persist="0"
fi

if [ "$new_ppp_ping" = "on" ]; then
    ping="1"
else
    ping="0"
fi
if [ "$new_ppp_ping2" = "on" ]; then
    ping2="1"
else
    ping2="0"
fi

# load old settings
FILE=/mnt/rwfs/settings/settings.ppp
[ -e "$FILE" ] && . $FILE
# save new settings
echo "PPP_ENABLED=$ppp_en" > $FILE
#sim1
echo "PPP_APN=$new_ppp_apn" >> $FILE
echo "PPP_USERNAME=$new_ppp_username" >> $FILE
echo "PPP_PASSWORD=$new_ppp_password" >> $FILE
echo "PPP_AUTH=$new_ppp_auth" >> $FILE
echo "PPP_IPADDR=$new_ppp_ipaddr" >> $FILE
echo "PPP_RIPADDR=$new_ppp_ripaddr" >> $FILE
echo "PPP_DIAL=$new_ppp_dial" >> $FILE
echo "PPP_MRU=$new_ppp_mru" >> $FILE
echo "PPP_MTU=$new_ppp_mtu" >> $FILE
echo "PPP_ALLOW_ROAMING=$new_ppp_roaming" >> $FILE
echo "PPP_USEDNS=$new_ppp_usedns" >> $FILE
echo "PPP_DNS_SERVER=$new_ppp_dns_server" >> $FILE
echo "PPP_DNS_SECONDARY=$new_ppp_dns_secondary" >> $FILE
echo "PPP_MODE=$ppp_mode" >> $FILE
#sim2
echo "PPP_APN2=$new_ppp_apn2" >> $FILE
echo "PPP_USERNAME2=$new_ppp_username2" >> $FILE
echo "PPP_PASSWORD2=$new_ppp_password2" >> $FILE
echo "PPP_AUTH2=$new_ppp_auth2" >> $FILE
echo "PPP_IPADDR2=$new_ppp_ipaddr2" >> $FILE
echo "PPP_RIPADDR2=$new_ppp_ripaddr2" >> $FILE
echo "PPP_DIAL2=$new_ppp_dial2" >> $FILE
echo "PPP_MRU2=$new_ppp_mru2" >> $FILE
echo "PPP_MTU2=$new_ppp_mtu2" >> $FILE
echo "PPP_ALLOW_ROAMING2=$new_ppp_roaming2" >> $FILE
echo "PPP_USEDNS2=$new_ppp_usedns2" >> $FILE
echo "PPP_DNS_SERVER2=$new_ppp_dns_server2" >> $FILE
echo "PPP_DNS_SECONDARY2=$new_ppp_dns_secondary2" >> $FILE
echo "PPP_MODE2=$ppp_mode2" >> $FILE
#maxfail, retry and reboot
echo "PPP_SWITCH=$switch" >> $FILE
echo "PPP_MAXFAIL=$new_ppp_maxfail" >> $FILE
echo "PPP_TRYPRIMARY=$tryprimary" >> $FILE
echo "PPP_RETRY=$new_ppp_retry" >> $FILE
echo "PPP_REBOOT=$reboot" >> $FILE
echo "PPP_REBOOT_COUNT=$new_ppp_reboot_count" >> $FILE
echo "PPP_PERSIST=$persist" >> $FILE
echo "PPP_SOFTRETR=$new_ppp_softretr" >> $FILE
#card#
echo "PPP_SIMCARD=$new_simcard" >> $FILE
#ping
echo "PPP_PING=$ping" >> $FILE
echo "PPP_PING_IPADDR=\"$new_ppp_ping_ipaddr\"" >> $FILE
echo "PPP_PING_INTVL=$new_ppp_ping_intvl" >> $FILE
echo "PPP_PING_REPEAT_INTVL=$new_ppp_ping_repeat_intvl" >> $FILE
echo "PPP_PING_COUNT=$new_ppp_ping_count" >> $FILE
echo "PPP_PING2=$ping2" >> $FILE
echo "PPP_PING_IPADDR2=\"$new_ppp_ping_ipaddr2\"" >> $FILE
echo "PPP_PING_INTVL2=$new_ppp_ping_intvl2" >> $FILE
echo "PPP_PING_REPEAT_INTVL2=$new_ppp_ping_repeat_intvl2" >> $FILE
echo "PPP_PING_COUNT2=$new_ppp_ping_count2" >> $FILE
#fixed band frequency
echo "PPP_BAND=$new_ppp_band" >> $FILE
echo "PPP_BAND2=$new_ppp_band2" >> $FILE
echo "" >> $FILE
## PIN
if [ -n "$new_ppp_pin" ]; then
    echo $new_ppp_pin > /mnt/rwfs/settings/settings.pin1
else
    [ -e /mnt/rwfs/settings/settings.pin1 ] && rm /mnt/rwfs/settings/settings.pin1
fi
if [ -n "$new_ppp_pin2" ]; then
    echo $new_ppp_pin2 > /mnt/rwfs/settings/settings.pin2
else
    [ -e /mnt/rwfs/settings/settings.pin2 ] && rm /mnt/rwfs/settings/settings.pin2
fi  

# start/stop pppd
touch /tmp/start
if [ "$ppp_en" = "1" ]; then
    echo "<br>"
    if [ "$PPP_ENABLED" = "0" ]; then
        /etc/init.d/ppp start
    else
        /etc/init.d/ppp stop
        echo "<br>"
        /etc/init.d/ppp start
    fi
else
    echo "<br>"
    /etc/init.d/ppp stop
fi

echo "<hr><a href=\"config_ppp.cgi\">Return</a>"
