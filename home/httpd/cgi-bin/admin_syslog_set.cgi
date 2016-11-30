#!/bin/sh /usr/lib/irz-web/setscript
F=/mnt/rwfs/settings/settings.syslog
case `formq syslog_mode` in
    1)
        echo "SYSLOG_LOCALLY=1"
        echo "SYSLOG_NETWORK=0"
    ;;
    2)
        echo "SYSLOG_LOCALLY=0"
        echo "SYSLOG_NETWORK=1"
    ;;
    3)
        echo "SYSLOG_LOCALLY=1"
        echo "SYSLOG_NETWORK=1"
    ;;
esac > $F
echo "SYSLOG_NETWORK_ADDRESS=`formq syslog_server`" >> $F
echo "SYSLOG_NETWORK_PORT=`formq syslog_server_port`" >> $F

echo "<pre>"
/etc/init.d/syslog restart
echo "</pre><hr><a href=\"admin_syslog.cgi\">Return</a>"
