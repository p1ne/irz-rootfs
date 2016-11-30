#!/bin/sh

# html starts
echo "Content-type: text/html"
echo ""

echo "Please wait...<hr>"

#remove header
echo "Reading package...<br>"
sed '1,4d;$d;$d;$d;$d;$d;$d;' - > /tmp/backup.tar

tar -xf /tmp/backup.tar -C /
rm /tmp/backup.tar
md5sum -c /tmp/backup.md5 -s
md5res=$?
#check md5 and mount results
if [ "$md5res" = "0" ]; then
    umount /mnt/rwfs
    gunzip /tmp/backup.gz
    flash_erase /dev/mtd6 0 0 2>&1 1>/dev/null
    flashcp /tmp/backup /dev/mtd6
    if [ "$?" != "0" ]; then
        echo "Can't write settings to flash<br>"
    fi
    mount -t jffs2 /dev/mtdblock6 /mnt/rwfs -o rw,relatime
    rm /tmp/backup.md5
    rm /tmp/backup

    if [ -f /mnt/rwfs/settings/settings.eth ]; then
        if [ ! -f /tmp/noreboot ]; then
            . /mnt/rwfs/settings/settings.eth
            echo "Settings restored, rebooting...<br>"
            echo "Please wait one minute and <a href="http://$ETH_IPADDR">click here to return</a>"
            /etc/init.d/connection message "Restore settings reboot"
            ( sleep 5 && reboot ) &
            exit 0
        else
            echo "Settings restored, but reboot is disabled by FW upgrade<br>"
        fi
    else
        echo "Can't read new settings!"
    fi
else
    echo "File corrupted!<br>"
fi
echo "<hr><a href=\"admin_backrest.cgi\">Return</a>"
