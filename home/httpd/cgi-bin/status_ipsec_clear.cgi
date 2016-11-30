#!/bin/sh

# html starts
echo "Content-type: text/html"
echo ""

[ -f /var/log/racoon.log ] && echo "" > /var/log/racoon.log
echo "<a href=\"status_ipsec.cgi\">Return</a>"
echo "<meta http-equiv=\"refresh\" content=\"0;url=status_ipsec.cgi\"/>"

