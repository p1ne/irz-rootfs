#!/bin/sh /usr/lib/irz-web/setscript
cat <<EOF > /mnt/rwfs/settings/settings.sms
SMS_SEND_POWERUP=$(isOn $(formq sms_send_powerup))
SMS_SEND_CONNECT=$(isOn $(formq sms_send_connect))
SMS_SEND_DISCONNECT=$(isOn $(formq sms_send_disconnect))
SMS_SEND_ETH_CONNECT=$(isOn $(formq sms_send_eth_connect))
SMS_SEND_ETH_DISCONNECT=$(isOn $(formq sms_send_eth_disconnect))
SMS_PHONE_NO1=$(formq sms_phone_no1)
SMS_PHONE_NO2=$(formq sms_phone_no2)
SMS_UNIT_ID="$(formq sms_unit_id)"
EOF

echo "<hr><a href=\"config_sms.cgi\">Return</a>"
