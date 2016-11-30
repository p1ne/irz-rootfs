#!/bin/sh
# html starts
echo "Content-type: text/html"
echo ""

echo "<!DOCTYPE html>"
echo "<html><body>"
echo "Please wait...<hr>"
echo "<pre>"

## remove header
echo -n "Reading package... "
mkdir /tmp/update
sed '1,4d;$d;$d;$d;$d;$d;$d;' - | tar xf - -C /tmp/update

[ "$?" = "0" ] && echo "OK" || echo "Failed"

firmware_update.start /tmp/update

if [ "$?" = "0" ]; then
    echo "</pre>"
    echo "<hr>Please wait one minute and "
    echo "<a href=\"/\">click here to return</a>"
    echo '<META HTTP-EQUIV="REFRESH" CONTENT="60;URL=/">'
else
    echo "There were problems during firmware upgrade!"
    echo "</pre>"
    echo "<h1>You must upload firmware again!</h1>"
    echo "<hr><a href=\"/\">Click here to return</a>"
fi
echo "</body></html>"
