#!/bin/sh

#logger "usb-eth called"

#logger "action=$ACTION"
#logger "seqnum=$SEQNUM"
#logger "major=$MAJOR"
#logger "mdev=$MDEV"
#logger "devpath=$DEVPATH"
#logger "sussystem=$SUBSYSTEM"
#logger "minor=$MINOR"
#logger "physdevpath=$PHYSDEVPATH"
#logger "physdevdriver=$PHYSDEVDRIVER"
#logger "physdevbu=$PHYSDEVBU"

if [ "$ACTION" = "add" ] && [ "$MAJOR" = "189" ]; then
    [ -e /mnt/rwfs/settings/settings.eth ] && . /mnt/rwfs/settings/settings.eth

    if [ "$ETH_USB_LAN" = "1" ]; then
    (sleep 1; ifconfig eth1 $ETH_IPADDR3 netmask $ETH_NETMASK3 up )&
    fi

fi
