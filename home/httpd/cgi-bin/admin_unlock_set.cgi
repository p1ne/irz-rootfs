#!/bin/sh /usr/lib/irz-web/setscript
simcard=`formq simcard`
## set sim
echo "<pre>"
/etc/init.d/ppp stop
echo "Switching to SIM $simcard"
modem off
sleep 1
sim set $simcard
modem on
sleep 10
## test pin
if sim_check pres; then
    ## No pin
	echo "No PIN required for SIM $simcard"
else
    pin=`formq sim_pin`
    ## enter pin
    if /usr/bin/pin_enter $pin ; then
	    echo "PIN for SIM $simcard OK"
		## unlock sim card
		if /usr/bin/pin_unlock $pin; then
			echo "SIM $simcard unlocked"
		else
			echo "Failed to unlock SIM $simcard"
	    fi
    else
	    echo "Bad PIN code for SIM $simcard!"
    fi
fi
echo "</pre>"
echo "<hr><a href=\"admin_unlock.cgi\">Return</a>"
