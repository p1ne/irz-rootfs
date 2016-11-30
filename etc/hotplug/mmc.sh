#!/bin/sh
#export > /tmp/action
logger "mmc hotplug $ACTION $MDEV $MINOR"

mkdir -p /var/mnt/$MDEV
mount /dev/$MDEV /var/mnt/$MDEV
echo $ACTION $MDEV >> /tmp/plug    
