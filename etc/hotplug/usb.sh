#!/bin/sh
#export > /tmp/action
#echo $ACTION $MDEV $MINOR > /tmp/plug

## If usb drive present on boot no action and minor is given
## Workaround is to provide these variables
[ -z "$ACTION" ] && ACTION=add
[ -z "$MINOR" ] && MINOR=0
let "VOL=MINOR + 1"
L=/tmp/usbfsck.log
#echo $VOL >> /tmp/plug
case $ACTION in
    add)
        #echo "add /dev/$MDEV$VOL" >> /tmp/plug
        if [ "$VOL" = "1" ]; then
            if [ -e "/dev/$MDEV$VOL" ]; then
                echo `date +%F_%T` >>$L
                dosfsck -a -v /dev/${MDEV}${VOL} 1>>$L 2>>$L
                echo   "dosfsck -a -v /dev/${MDEV}${VOL}: $?" >>$L
                mount  "/dev/$MDEV$VOL" /mnt/usb ; res=$?
                echo   "mount /dev/$MDEV$VOL /mnt/usb: $res" >>$L
                logger "mount /dev/$MDEV$VOL /mnt/usb: $res"
            elif [ -e "/dev/$MDEV" ]; then
                dosfsck -a -v /dev/${MDEV} 1>>$L 2>>$L
                echo   "dosfsck -a -v /dev/${MDEV}: $?" >>$L
                mount  "/dev/$MDEV" /mnt/usb ; res=$?
                echo   "mount /dev/$MDEV /mnt/usb: $res" >>$L
                logger "mount /dev/$MDEV /mnt/usb: $res"
            else
                logger "USB-Flash device not found"
            exit
            fi

            /etc/init.d/syslog restart

            if [ -e "/mnt/usb/autoupdate.bin" -a ! -e "/mnt/usb/autoupdate.log" ]; then
                log="/mnt/usb/autoupdate.log"
                led busy 1
                date -R > $log
                if [ -e "/mnt/usb/loaddefaults" ]; then
                    loaddefaults >> $log 2>&1
                    echo "Done" >> $log
                    test -e "/usr/bin/saveset" && saveset >> $log 2>&1
                elif [ -e "/mnt/usb/backup.bin" ]; then
                    echo "Restore configuration..." >> $log
                    tar -xf /mnt/usb/backup.bin -C / >> $log 2>&1
                    md5sum -c /tmp/backup.md5 -s >> $log 2>&1
                    md5res=$?
                    #check md5 and mount results
                    if [ "$md5res" = "0" ]; then
                        umount /mnt/rwfs >> $log 2>&1
                        gunzip /tmp/backup.gz >> $log 2>&1
                        flash_erase /dev/mtd6 0 0 >/dev/null 2>&1
                        flashcp /tmp/backup /dev/mtd6
                        if [ "$?" != "0" ]; then
                            echo "Can't write settings to flash" >> $log
                        fi
                        mount -t jffs2 /dev/mtdblock6 /mnt/rwfs -o rw,relatime >> $log 2>&1
                        rm /tmp/backup.md5 >> $log 2>&1
                        rm /tmp/backup >> $log 2>&1
                        if [ -f /mnt/rwfs/settings/settings.eth ]; then
                            . /mnt/rwfs/settings/settings.eth
                            echo "Settings restored" >> $log
                        else
                            echo "Can't read new settings!" >> $log
                        fi
                    else
                        echo "File corrupted!" >> $log
                    fi
                fi
                led busy 0
                firmware_update.start /mnt/usb/autoupdate.bin >> $log 2>&1
                usb umount >/dev/null 2>&1
            fi
        else
            mkdir /tmp/$MDEV$VOL 
            mount /dev/$MDEV$VOL /tmp/$MDEV$VOL
        fi
    ;;
    remove)
        #echo "remove /dev/$MDEV$VOL" >> /tmp/plug
        echo `date +%F_%T` >>$L
        if [ "$VOL" = "1" ]; then
            echo "syslog restart" >>$L
            /etc/init.d/syslog restart
            umount /mnt/usb ; res=$?
            echo "umount /mnt/usb: $res" >>$L
            logger "umount /mnt/usb: $res"
        else
            umount /tmp/$MDEV$VOL ; res=$?
            echo "umount /tmp/$MDEV$VOL: $res" >>$L
            logger "umount /tmp/$MDEV$VOL: $res"
            rmdir /tmp/$MDEV$VOL 
        fi
        if [ ! -f /tmp/nousbreset ]; then
            ## if not disabled - power cycle external USB port
            usb off
            logger "usb off"
            sleep 5
            usb on
            logger "usb on"
        fi
    ;;
    *)
        echo $ACTION $MDEV$VOL >> /tmp/plug
    ;;
esac
