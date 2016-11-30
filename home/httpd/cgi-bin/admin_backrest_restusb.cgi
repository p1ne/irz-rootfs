#!/bin/sh

# html starts
echo "Content-type: text/html"
echo ""

echo "Please wait...<hr><pre>"

[ -e "/mnt/rwfs/settings/unitname" ] && unitname=`cat /mnt/rwfs/settings/unitname`

flash=/mnt/usb
tmpfile1=/tmp/openvpn.tmp1
tmpfile2=/tmp/openvpn.tmp2

mount|grep /mnt/usb -q &> /dev/null
res=$?

_exit() {
    echo "</pre>"
    echo "<hr><a href=\"admin_backrest.cgi\">Return</a>"
    exit 0
}

if [ "$res" = "0" ]; then
    if [ -f "${flash}/backup.bin" ]; then
        tar -xf ${flash}/backup.bin -C /
        md5sum -c /tmp/backup.md5 -s
        md5res=$?
        #check md5 and mount results
        if [ "$md5res" = "0" ]; then
            umount /mnt/rwfs
            gunzip /tmp/backup.gz
            flash_erase /dev/mtd6 0 0 2>&1 1>/dev/null
            flashcp /tmp/backup /dev/mtd6
            if [ "$?" != "0" ]; then
                echo "Can't write settings to flash"
            else
                echo "Done!"
            fi
            mount -t jffs2 /dev/mtdblock6 /mnt/rwfs -o rw,relatime
            rm /tmp/backup.md5
            rm /tmp/backup
        else
            echo "Backup file corrupted!"
            _exit
        fi
    else
        echo "No backup.bin found!"
        _exit
    fi

    if [ -e "${flash}/$unitname" ]; then
        echo "unitname dir exist"
        echo "${flash}/$unitname/openvpn_client/"
        if [ -e "${flash}/$unitname/openvpn_client" ]; then
            echo "OpenVPN client config files are found. Writing to config."
            setfile=/mnt/rwfs/settings/settings.openvpn
            cp $setfile $tmpfile1
            [ -e "${flash}/$unitname/openvpn_client/ca.crt" ] && (client_ca_crt=`cat ${flash}/$unitname/openvpn_client/ca.crt|encode`; sed "/OPENVPN_CA_CERT/ c\OPENVPN_CA_CERT=${client_ca_crt}" $tmpfile1 > $tmpfile2; mv $tmpfile2 $tmpfile1)
            [ -e "${flash}/$unitname/openvpn_client/dh1024.pem" ] && (client_dh=`cat ${flash}/$unitname/openvpn_client/dh1024.pem|encode`;sed "/OPENVPN_DH_PARAMS/ c\OPENVPN_DH_PARAMS=${client_dh}" $tmpfile1 > $tmpfile2; mv $tmpfile2 $tmpfile1)

            files=`ls ${flash}/$unitname/openvpn_client/*.crt|sed "/ca.crt/d"`
            if [ "`echo $files|wc -l`" = "1" ]; then
                (client_local_crt=`cat $files|encode`;sed "/OPENVPN_LOCAL_CERT/ c\OPENVPN_LOCAL_CERT=${client_local_crt}" $tmpfile1 > $tmpfile2; mv $tmpfile2 $tmpfile1)
            else
                echo "openvpn certificate not found, or there is more than one certificate in openvpn_client directory"
            fi
            if [ "`ls ${flash}/$unitname/openvpn_client/*.key|wc -l`" = "1" ]; then
                (client_local_key=`cat ${flash}/$unitname/openvpn_client/*.key|encode`;sed "/OPENVPN_LOCAL_KEY/ c\OPENVPN_LOCAL_KEY=${client_local_key}" $tmpfile1 > $tmpfile2; mv $tmpfile2 $tmpfile1)
            else
                echo "openvpn local key file not found, or there is more than one key file in openvpn_client directory"
            fi
            [ -e "${flash}/$unitname/openvpn_client/psk" ] && (client_psk=`cat ${flash}/$unitname/openvpn_client/psk|encode`;sed "/OPENVPN_SECRET/ c\OPENVPN_SECRET=${client_psk}" $tmpfile1 > $tmpfile2; mv $tmpfile2 $tmpfile1)
            [ -e "${flash}/$unitname/openvpn_client/config" ] && (client_config=`cat ${flash}/$unitname/openvpn_client/config|encode`;sed "/OPENVPN_CONFIG_FILE/ c\OPENVPN_CONFIG_FILE=${client_config}" $tmpfile1 > $tmpfile2; mv $tmpfile2 $tmpfile1)
            mv $tmpfile1 $setfile
        fi
        if [ -e "${flash}/$unitname/openvpn_server" ]; then
            echo "OpenVPN server config files are found. Writing to config."
            setfile=/mnt/rwfs/settings/settings.ovpns
            cp $setfile $tmpfile1
            [ -e "${flash}/$unitname/openvpn_server/ca.crt" ] && (server_ca_crt=`cat ${flash}/$unitname/openvpn_server/ca.crt|encode`;sed "/OVPNS_CA_CERT/ c\OVPNS_CA_CERT=${server_ca_crt}" $tmpfile1 > $tmpfile2; mv $tmpfile2 $tmpfile1)
            [ -e "${flash}/$unitname/openvpn_server/dh1024.pem" ] && (server_dh=`cat ${flash}/$unitname/openvpn_server/dh1024.pem|encode`;sed "/OVPNS_CA_CERT/ c\OVPNS_DH_PARAMS=${server_dh}" $tmpfile1 > $tmpfile2; mv $tmpfile2 $tmpfile1)
            [ -e "${flash}/$unitname/openvpn_server/local.crt" ] && (server_local_crt=`cat ${flash}/$unitname/openvpn_server/local.crt|encode`;sed "/OVPNS_LOCAL_CERT/ c\OVPNS_LOCAL_CERT=${server_local_crt}" $tmpfile1 > $tmpfile2; mv $tmpfile2 $tmpfile1)
            [ -e "${flash}/$unitname/openvpn_server/local.key" ] && (server_local_key=`cat ${flash}/$unitname/openvpn_server/local.key|encode`;sed "/OVPNS_LOCAL_KEY/ c\OVPNS_LOCAL_KEY=${server_local_key}" $tmpfile1 > $tmpfile2; mv $tmpfile2 $tmpfile1)
            [ -e "${flash}/$unitname/openvpn_server/config" ] && (server_config=`cat ${flash}/$unitname/openvpn_server/config|encode`;sed "/OVPNS_CONFIG/ c\OVPNS_CONFIG=${server_config}" $tmpfile1 > $tmpfile2; mv $tmpfile2 $tmpfile1)
            mv $tmpfile1 $setfile
        fi
    else
        ## Unitname does not exist
        if [ -e "${flash}/openvpn_client" ]; then
            echo "OpenVPN client config files are found. Writing to config."
            setfile=/mnt/rwfs/settings/settings.openvpn
            cp $setfile $tmpfile1
            [ -e "${flash}/openvpn_client/ca.crt" ] && (client_ca_crt=`cat ${flash}/openvpn_client/ca.crt|encode`; sed "/OPENVPN_CA_CERT/ c\OPENVPN_CA_CERT=${client_ca_crt}" $tmpfile1 > $tmpfile2; mv $tmpfile2 $tmpfile1)
            [ -e "${flash}/openvpn_client/dh1024.pem" ] && (client_dh=`cat ${flash}/openvpn_client/dh1024.pem|encode`;sed "/OPENVPN_DH_PARAMS/ c\OPENVPN_DH_PARAMS=${client_dh}" $tmpfile1 > $tmpfile2; mv $tmpfile2 $tmpfile1)

            files=`ls ${flash}/openvpn_client/*.crt|sed "/ca.crt/d"`
            if [ "`echo $files|wc -l`" = "1" ]; then
                (client_local_crt=`cat $files|encode`;sed "/OPENVPN_LOCAL_CERT/ c\OPENVPN_LOCAL_CERT=${client_local_crt}" $tmpfile1 > $tmpfile2; mv $tmpfile2 $tmpfile1)
            else
                echo "OpenVPN certificate not found, or there is more than one certificate in openvpn_client directory"
            fi
            if [ "`ls ${flash}/openvpn_client/*.key|wc -l`" = "1" ]; then
                (client_local_key=`cat ${flash}/openvpn_client/*.key|encode`;sed "/OPENVPN_LOCAL_KEY/ c\OPENVPN_LOCAL_KEY=${client_local_key}" $tmpfile1 > $tmpfile2; mv $tmpfile2 $tmpfile1)
            else
                echo "OpenVPN local key file not found, or there is more than one key file in openvpn_client directory"
            fi
            [ -e "${flash}/openvpn_client/psk" ] && (client_psk=`cat ${flash}/openvpn_client/psk|encode`;sed "/OPENVPN_SECRET/ c\OPENVPN_SECRET=${client_psk}" $tmpfile1 > $tmpfile2; mv $tmpfile2 $tmpfile1)
            [ -e "${flash}/openvpn_client/config" ] && (client_config=`cat ${flash}/openvpn_client/config|encode`;sed "/OPENVPN_CONFIG_FILE/ c\OPENVPN_CONFIG_FILE=${client_config}" $tmpfile1 > $tmpfile2; mv $tmpfile2 $tmpfile1)
            mv $tmpfile1 $setfile
        fi
        if [ -e "${flash}/openvpn_server" ]; then
            echo "OpenVPN server config files are found. Writing to config."
            setfile=/mnt/rwfs/settings/settings.ovpns
            cp $setfile $tmpfile1
            [ -e "${flash}/openvpn_server/ca.crt" ] && (server_ca_crt=`cat ${flash}/openvpn_server/ca.crt|encode`;sed "/OVPNS_CA_CERT/ c\OVPNS_CA_CERT=${server_ca_crt}" $tmpfile1 > $tmpfile2; mv $tmpfile2 $tmpfile1)
            [ -e "${flash}/openvpn_server/dh1024.pem" ] && (server_dh=`cat ${flash}/openvpn_server/dh1024.pem|encode`;sed "/OVPNS_CA_CERT/ c\OVPNS_DH_PARAMS=${server_dh}" $tmpfile1 > $tmpfile2; mv $tmpfile2 $tmpfile1)
            [ -e "${flash}/openvpn_server/local.crt" ] && (server_local_crt=`cat ${flash}/openvpn_server/local.crt|encode`;sed "/OVPNS_LOCAL_CERT/ c\OVPNS_LOCAL_CERT=${server_local_crt}" $tmpfile1 > $tmpfile2; mv $tmpfile2 $tmpfile1)
            [ -e "${flash}/openvpn_server/local.key" ] && (server_local_key=`cat ${flash}/openvpn_server/local.key|encode`;sed "/OVPNS_LOCAL_KEY/ c\OVPNS_LOCAL_KEY=${server_local_key}" $tmpfile1 > $tmpfile2; mv $tmpfile2 $tmpfile1)
            [ -e "${flash}/openvpn_server/config" ] && (server_config=`cat ${flash}/openvpn_server/config|encode`;sed "/OVPNS_CONFIG/ c\OVPNS_CONFIG=${server_config}" $tmpfile1 > $tmpfile2; mv $tmpfile2 $tmpfile1)
            mv $tmpfile1 $setfile
        fi
        #set openvpn files
    fi
    if [ -f /mnt/rwfs/settings/settings.eth ]; then
        . /mnt/rwfs/settings/settings.eth
        if [ ! -f /tmp/noreboot ]; then
            echo "Settings restored, rebooting..."
            echo "</pre><hr>Please wait one minute and <a href="http://$ETH_IPADDR">click here to return</a>"
            ( sleep 5 && reboot ) &
            exit 0
        else
            echo "Settings restored, but reboot is disabled by FW upgrade<br>"
            _exit
        fi
    else
        echo "Can't read updated settings!"
        _exit
    fi
else
    echo "No USB disk found"
    _exit
fi

