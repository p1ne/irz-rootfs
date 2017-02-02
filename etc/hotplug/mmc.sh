#!/bin/sh
#export > /tmp/action
logger "mmc hotplug $ACTION $MDEV $MINOR"

mkdir -p /var/mnt/$MDEV
mount -t ext2 /dev/$MDEV /var/mnt/$MDEV
echo $ACTION $MDEV >> /tmp/plug    
