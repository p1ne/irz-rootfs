#!/bin/sh /usr/lib/irz-web/setscript
#check old pass
old_pw=`formq old_passwd`
old_root=`grep ":0:0:" /etc/passwd | sed -e 's/\:.*//'|head -n 1`
old_hash_loc=`cat /etc/shadow| awk -F: "/^$old_root/{print(\\$2);}" `
old_salt=`echo $old_hash_loc | awk -F\$ '{print $3}'`
old_hash_rem=`cryptpw -m md5 -S "$old_salt" $old_pw`

if [ "$old_hash_rem" != "$old_hash_loc" ]; then
    echo "Incorrect old password!<br>"
	echo "<hr><a href=\"admin_passwd.cgi\">Return</a>"
    exit 0
fi

## Define root name
root_name=`formq new_root`
if [ -n "$root_name" ]; then
	echo "Setting root name to: $root_name<br>"
else
	root_name=$old_root
fi

new_pw=`formq new_passwd`
new_pw2=`formq new_passwd2`
## Define password
hash_to_write=`httpd -m $old_pw`;
if [ -n "$new_pw" ]; then
	if [ "$new_pw" != "$new_pw2" ]; then
		echo "New passwords do not match! Do NOT changing password.<br>"
	else
	    hash_to_write=`httpd -m $new_pw`;
		CHPW="yes"
		echo "Changing password!<br>"
	fi
else
	echo "Do not changing password<br>"
fi

## Change root name in system
sed "s/^$old_root:/$root_name:/" /etc/passwd > /tmp/passwd 
sed "s/^$old_root:/$root_name:/" /etc/shadow > /tmp/shadow
cat /tmp/passwd > /etc/passwd
cat /tmp/shadow > /etc/shadow

## Change password in system
[ "$CHPW" = "yes" ] && echo "$root_name:$new_pw" | chpasswd -m > /dev/null

## Change root name ang password in httpd
echo "/cgi-bin:$root_name:$hash_to_write" > /etc/httpd.conf

## Add symlink for crontab
cd /var/spool/cron/crontabs/
ln -s root $root_name
cd $OLDPWD

echo "<hr><a href=\"admin_passwd.cgi\">Return</a>"
## Force httpd to reload settings
killall -HUP httpd
