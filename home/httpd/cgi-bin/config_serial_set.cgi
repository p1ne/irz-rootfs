#!/bin/sh /usr/lib/irz-web/setscript
## select model
. /etc/version
case "$MODEL" in
    RCA|RC1)
        HAS232=1
        HAS485=0
        HAS422=0
        HASDCC=0
        ;;  
    RUH|RUH2)
        HAS232=1
        HAS485=0
        HAS422=0
        HASDCC=1
        ;;  
    RUH2b|RUHm|RUH2m|RUH2-RS485)
        HAS232=1
        HAS485=1
        HAS422=0
        HASDCC=1
        ;;  
    RUH3)
        HAS232=1
        HAS485=1
        HAS422=1
        HASDCC=0
        ;;  
    *)  
        HAS232=1
        HAS485=0
        HAS422=0
        HASDCC=0
        ;;
esac

[ "$HAS232" = "1" ] && ser_mode=`formq ser_mode`
[ -z "$ser_mode" ] && ser_mode="none"

[ "$HAS485" = "1" ] && ser_mode_4XX=`formq ser_mode_4XX`
[ -z "$ser_mode_4XX" ] && ser_mode_4XX="none"

[ "$HASDCC" = "1" ] && sec_mode=`formq sec_mode`
[ -z "$sec_mode" ] && sec_mode="none"

## load old settings
[ -e /mnt/rwfs/settings/settings.serial ] && . /mnt/rwfs/settings/settings.serial

#save settings
SER=/mnt/rwfs/settings/settings.serial
cat /dev/null > $SER # poor's man truncate
if [ "$HAS232" = "1" ]; then
    ser_tout=`formq ser_tout`
    cat <<EOF >> $SER
SER_MODE=$ser_mode
SER_IFACE=`formq ser_iface`
SER_PORT=`formq ser_port`
SER_SERVER=`formq ser_server`
SER_BAUD=`formq ser_baud`
SER_DATA=`formq ser_data`
SER_PARITY=`formq ser_parity`
SER_STOP=`formq ser_stop`
SER_TOUT=${ser_tout:-"0"}
SER_ACCUM_INTVL=`formq ser_accum_intvl`
SER_ACCUM_ATTS=`formq ser_accum_atts`
SER_RECON_DELAY=`formq ser_recon_delay`
SER_BANNER=`formq ser_banner | encode`
EOF
fi
if [ "$HAS485" = "1" ]; then
    ser_tout_4XX=`formq ser_tout_4XX`
    cat <<EOF >> $SER
SER_MODE_4XX=$ser_mode_4XX
SER_IFACE_4XX=`formq ser_iface_4XX`
SER_PORT_4XX=`formq ser_port_4XX`
SER_SERVER_4XX=`formq ser_server_4XX`
SER_BAUD_4XX=`formq ser_baud_4XX`
SER_DATA_4XX=`formq ser_data_4XX`
SER_PARITY_4XX=`formq ser_parity_4XX`
SER_STOP_4XX=`formq ser_stop_4XX`
SER_TOUT_4XX=${ser_tout_4XX:-"0"}
SER_ACCUM_INTVL_4XX=`formq ser_accum_intvl_4XX`
SER_ACCUM_ATTS_4XX=`formq ser_accum_atts_4XX`
SER_RECON_DELAY_4XX=`formq ser_recon_delay_4XX`
SER_BANNER_4XX=`formq ser_banner_4XX | encode`
EOF
fi
if [ "$HASDCC" = "1" ]; then
    cat <<EOF >> $SER
SEC_INTVL=`formq sec_intvl`
SEC_MODE=$sec_mode
SEC_PHONES=`formq sec_phones | encode`
SEC_OPEN=`formq sec_open | encode`
SEC_CLOSE=`formq sec_close | encode`
EOF
fi

#start/stop/reload serial
echo "<pre>"
if [ "$ser_mode" != "none" ]; then
	if [ "$SER_MODE" != "none" ]; then
		/etc/init.d/serial restart 1
	else
		/etc/init.d/serial start 1
	fi
else
	/etc/init.d/serial stop 1
fi

if [ "$ser_mode_4XX" != "none" ]; then
	if [ "$SER_MODE_4XX" != "none" ]; then
		/etc/init.d/serial restart 2
	else
		/etc/init.d/serial start 2
	fi
else
	/etc/init.d/serial stop 2
fi

if [ $sec_mode != "none" ]; then
    if [ $SEC_MODE != "none" ]; then
        /etc/init.d/con_check restart
    else
        /etc/init.d/con_check start
    fi  
else
    /etc/init.d/con_check stop
fi

echo "</pre><hr><a href=\"config_serial.cgi\">Return</a>"
