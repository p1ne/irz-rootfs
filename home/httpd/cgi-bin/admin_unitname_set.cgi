#!/bin/sh /usr/lib/irz-web/setscript

if [ "`formq unitnamemode`" = "user" ]; then
    formq unitname > /mnt/rwfs/settings/unitname
fi

if [ "`formq hostnamemode`" = "user" ] ; then
    new_hostname=`formq hostname`
    if [ -n "$new_hostname" ]; then
        echo "$new_hostname" | tr ' ' '_' > /etc/hostname
    else
        cp -f /etc/defaults/hostname /etc/hostname
    fi
fi

cat <<EOF > /mnt/rwfs/settings/settings.etc
ETC_UNITNAME="`formq unitnamemode`"
ETC_HOSTNAME="`formq hostnamemode`"
EOF

regen_ident

echo "Setting unit name to: `cat /mnt/rwfs/settings/unitname`<br>"
echo "Setting host name to: `hostname`<br>"
echo "<hr><a href=\"admin_unitname.cgi\">Return</a>"
