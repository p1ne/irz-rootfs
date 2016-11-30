#!/bin/sh

# html starts
echo "Content-type: text/html"
echo ""

[ -f /var/log/ovpn-serv.log ] && echo "" > /var/log/ovpn-serv.log
echo "<a href=\"status_ovpnserv.cgi\">Return</a>"
echo "<meta http-equiv=\"refresh\" content=\"0;url=status_ovpnserv.cgi\"/>"

