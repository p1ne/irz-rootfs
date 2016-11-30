#!/bin/sh
# html starts

read POST_STRING

FD=`post_decode "$POST_STRING" | sed -n 's/^.*delete=\([^&]*\).*$/\1/p' | sed "s/ /_/g"`
FE=`post_decode "$POST_STRING" | sed -n 's/^.*exec=\([^&]*\).*$/\1/p' | sed "s/ /_/g"`
FL=`post_decode "$POST_STRING" | sed -n 's/^.*load=\([^&]*\).*$/\1/p' | sed "s/ /_/g"`

if [ -n "$FD" ]; then
	echo "Content-type: text/html"
	echo ""
	echo "Please wait...<hr>"
	echo "<pre>"
	rm -f "/mnt/rwfs/upload/$FD"
	echo "$FD: deleted"
	echo "</pre>"
	echo "<meta http-equiv=\"refresh\" content=\"2;url=admin_upload.cgi\"/>"
	echo "<hr><a href=\"admin_upload.cgi\">Return</a>"
elif [ -n "$FE" ]; then
	echo "Content-type: text/html"
	echo ""
	echo "Please wait...<hr>"
	echo "<pre>"
	if [ -x "/mnt/rwfs/upload/$FE" ]; then 
		chmod -x "/mnt/rwfs/upload/$FE";
		echo "$FE: cleared executable"
	else 
		chmod +x "/mnt/rwfs/upload/$FE";
		echo "$FE: set executable"
	fi
	echo "</pre>"
	echo "<meta http-equiv=\"refresh\" content=\"2;url=admin_upload.cgi\"/>"
	echo "<hr><a href=\"admin_upload.cgi\">Return</a>"
elif [ -n "$FL" ]; then
cat << EOF
Content-Type: application/octet-stream
Content-Description: File Transfer
Content-Disposition: attachment; filename="$FL"

EOF
cat "/mnt/rwfs/upload/$FL"

fi
