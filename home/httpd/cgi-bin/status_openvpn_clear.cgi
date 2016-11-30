#!/bin/sh

# html starts
echo "Content-type: text/html"
echo ""

[ -f /var/log/openvpn.log ] && echo "" > /var/log/openvpn.log
echo "<a href=\"status_openvpn.cgi\">Return</a>"
echo "<meta http-equiv=\"refresh\" content=\"0;url=status_openvpn.cgi\"/>"

