#!/bin/sh /usr/lib/irz-web/setscript

cat <<EOF > /mnt/rwfs/settings/settings.remote
REMOTE_HTTP_EXT=$(isOn $(formq remote_http_ext))
REMOTE_HTTP_EXT_PORT=$(formq remote_http_ext_port)
REMOTE_SSH=$(isOn $(formq remote_ssh))
REMOTE_SSH_PORT=$(formq remote_ssh_port)
REMOTE_SSH_EXT=$(isOn $(formq remote_ssh_ext))
REMOTE_SSH_EXT_PORT=$(formq remote_ssh_ext_port)
REMOTE_TELNET=$(isOn $(formq remote_telnet))
REMOTE_TELNET_PORT=$(formq remote_telnet_port)
REMOTE_TELNET_EXT=$(isOn $(formq remote_telnet_ext))
REMOTE_TELNET_EXT_PORT=$(formq remote_telnet_ext_port)
REMOTE_SNMP_EXT=$(isOn $(formq remote_snmp_ext))
REMOTE_SNMP_EXT_PORT=$(formq remote_snmp_ext_port)
REMOTE_ALLOW_PING=$(isOn $(formq remote_allow_ping))
EOF

echo "<pre>"
/etc/init.d/dropbear restart
/etc/init.d/telnetd restart
/etc/init.d/remote restart
echo '</pre><hr><a href="admin_remote.cgi">Return</a>'
