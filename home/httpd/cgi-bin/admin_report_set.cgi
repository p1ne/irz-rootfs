#!/bin/sh

# html starts
echo "Content-type: text/html"
echo ""

echo "Please wait...<hr>"
genreport > /tmp/report
echo "<hr><a href=\"admin_report.cgi\">Return</a>"
echo "<meta http-equiv=\"refresh\" content=\"0;url=admin_report.cgi\"/>"
