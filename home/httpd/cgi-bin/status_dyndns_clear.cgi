#!/bin/sh

# html starts
echo "Content-type: text/html"
echo ""
[ -f /var/log/inadyn.log.2.gz ] && rm /var/log/inadyn.log.2.gz
[ -f /var/log/inadyn.log.1.gz ] && rm /var/log/inadyn.log.1.gz
[ -f /var/log/inadyn.log.1.gz ] && /var/log/inadyn.log
kill -HUP `cat /var/run/inadyn/inadyn.pid 2>/dev/null` 2>/dev/null || true 
echo "<a href=\"status_dyndns.cgi\">Return</a>"
echo "<meta http-equiv=\"refresh\" content=\"0;url=status_dyndns.cgi\"/>"

