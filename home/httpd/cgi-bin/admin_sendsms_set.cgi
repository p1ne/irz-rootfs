#!/bin/sh /usr/lib/irz-web/setscript
number=`formq sendsms_number`
message=`formq sendsms_message | tr '\n' ' ' | tr -d '\r'`

echo "<br>Message Text: $message"
echo "<br>Sending SMS to +$number ... "
sms send +$number "$message"
ret=$?
if [ "$ret" = "0" ]; then
	echo "done"
else
	echo "failed ($ret)"
	echo "SENDSMS_NUMBER=$number" > /tmp/sendsms
	echo "SENDSMS_MESSAGE=\"$message\"" >> /tmp/sendsms
fi

echo "<hr><a href=\"admin_sendsms.cgi\">Return</a>"
