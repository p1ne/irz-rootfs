#!/bin/sh

# html starts
echo "Content-type: text/html"
echo ""
/etc/init.d/connection clear
echo "<a href=\"status_ppp.cgi\">Return</a>"
echo "<meta http-equiv=\"refresh\" content=\"0;url=status_ppp.cgi\"/>"

