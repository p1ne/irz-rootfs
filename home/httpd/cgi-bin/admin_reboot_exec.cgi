#!/bin/sh
[ -e /mnt/rwfs/settings/settings.eth ] && . /mnt/rwfs/settings/settings.eth

# html starts
echo "Content-type: text/html"
echo "Refresh: 80; URL=/"
echo ""

echo "Please wait...<hr>"
read FORM_URLENCODED
export FORM_URLENCODED
reboot_defaults=`formq reboot_defaults`

if [ "$reboot_defaults" = "on" ]; then
    loaddefaults
    echo "done <hr>"
    . /mnt/rwfs/settings/settings.eth
fi

if [ -n "$ETH_IPADDR" ]; then
    if [ ! -f /tmp/noreboot ]; then
        echo "Please wait one minute and "
        echo "<a href=http://"$ETH_IPADDR">click here to return</a>"
        /etc/init.d/connection message "Reboot by user via web interface"
        ( sleep 2 && reboot ) &
        echo "<br>Rebooting..."
    else
        echo "<br>Reboot is disabled by FW upgrade"
        echo "<hr><a href=\"config_dreboot.cgi\">Return</a>"
    fi
else
    echo "IP address not configured!"
    echo "<br>Please go to <a href=\"cgi-bin/config_eth.cgi\">LAN configuration page</a>, set IP address and apply settings."
fi
