#!/bin/sh

if [ -e /mnt/rwfs/settings/settings.remote ]; then
    . /mnt/rwfs/settings/settings.remote
else 
    . /etc/defaults/settings.remote
fi

[ "$REMOTE_HTTP_EXT" = "1" ] && HTTP_EXT_CHECKED=checked;
[ "$REMOTE_SSH" = "1" ] && SSH_CHECKED=checked;
[ "$REMOTE_SSH_EXT" = "1" ] && SSH_EXT_CHECKED=checked;
[ "$REMOTE_SSH_PORT" = "" ] && REMOTE_SSH_PORT=22;
[ "$REMOTE_TELNET" = "1" ] && TELNET_CHECKED=checked;
[ "$REMOTE_TELNET_EXT" = "1" ] && TELNET_EXT_CHECKED=checked;
[ "$REMOTE_TELNET_PORT" = "" ] && REMOTE_TELNET_PORT=23;
[ "$REMOTE_SNMP_EXT" = "1" ] && SNMP_EXT_CHECKED=checked;
[ "$REMOTE_ALLOW_PING" != "0" ] && ALLOW_PING=checked;

./begin $0

echo "</td><td colspan=\"3\" valign=\"top\">"

cat << EOF

<script>
<!--

function form_check(){
    if( document.input.remote_http_ext.checked && document.input.remote_http_ext_port.value == "") {
        alert("Enter HTTP port for external access");
        return false;
    }

    if( document.input.remote_ssh_ext.checked && document.input.remote_ssh_ext_port.value == "") {
        alert("Enter SSH port for external access");
        return false;
    }

    if( document.input.remote_telnet_ext.checked && document.input.remote_telnet_ext_port.value == "") {
        alert("Enter Telnet port for external access");
        return false;
    }

    if( document.input.remote_snmp_ext.checked && document.input.remote_snmp_ext_port.value == "") {
        alert("Enter SNMP port for external access");
        return false;
    }
}

function http_changed() {
    var secret = !document.input.remote_http_ext.checked;
    document.input.remote_http_ext_port.disabled = secret;
    document.input.remote_http_ext_port.style.color = (secret) ? "grey" : "";
}

function ssh_changed() {
    var secret = !document.input.remote_ssh.checked;
    var secret2 = !document.input.remote_ssh_ext.checked;
    secret2 = secret2 + secret;
    document.input.remote_ssh_port.disabled = secret;
    document.input.remote_ssh_ext.disabled = secret;
    document.input.remote_ssh_ext_port.disabled = secret2;
    document.input.remote_ssh_port.style.color = (secret) ? "grey" : "";
    document.input.remote_ssh_ext.style.color = (secret) ? "grey" : "";
    document.input.remote_ssh_ext_port.style.color = (secret2) ? "grey" : "";
}

function telnet_changed() {
    var secret = !document.input.remote_telnet.checked;
    var secret2 = !document.input.remote_telnet.checked;
    secret2 = secret2 + secret;
    document.input.remote_telnet_port.disabled = secret;
    document.input.remote_telnet_ext.disabled = secret;
    document.input.remote_telnet_ext_port.disabled = secret2;
    document.input.remote_telnet_port.style.color = (secret) ? "grey" : "";
    document.input.remote_telnet_ext.style.color = (secret) ? "grey" : "";
    document.input.remote_telnet_ext_port.style.color = (secret2) ? "grey" : "";
}

function snmp_changed() {
    var secret = !document.input.remote_snmp_ext.checked;
    document.input.remote_snmp_ext_port.disabled = secret;
    document.input.remote_snmp_ext_port.style.color = (secret) ? "grey" : "";
}

function window_onload(){
    http_changed();
    ssh_changed();
    telnet_changed();
    snmp_changed();
}

window.onload=window_onload;
-->
</script>

<form name="input" onsubmit="return form_check();" action="admin_remote_set.cgi" method="post">
<table width="100%" cellspacing="0" cellpadding="5" border="3">
    <tr>
        <td class="title" align="center">
            <b>Remote access</b>
        </td>
    </tr>
    <tr>
        <td>
            <table width="100%">
                 <tr align="center">
                    <td class="menu">HTTP</td>
                </tr>
                <tr>
                    <td>
                        <input type="checkbox" name="remote_http_ext" onclick="http_changed();" $HTTP_EXT_CHECKED >&nbsp;Enable WAN access to HTTP &nbsp;on port <input name="remote_http_ext_port" size="5" maxlength="5" value="$REMOTE_HTTP_EXT_PORT">
                    </td>
                </tr>
            </table>
            <table width="100%">
                <tr align="center">
                    <td class="menu">SSH</td>
                </tr>
                <tr>
                    <td>
                        <input type="checkbox" name="remote_ssh" onclick="ssh_changed();" $SSH_CHECKED >&nbsp;Enable SSH&nbsp;on port <input name="remote_ssh_port" size="5" maxlength="5" value="$REMOTE_SSH_PORT">
                    </td>
                </tr>
                <tr>
                    <td>
                        <input type="checkbox" name="remote_ssh_ext" size="5" maxlength="5" onclick="ssh_changed();" $SSH_EXT_CHECKED >&nbsp;Enable WAN access to SSH &nbsp;on port <input name="remote_ssh_ext_port" size="5" maxlength="5" value="$REMOTE_SSH_EXT_PORT">
                    </td>
                </tr>
                <tr align="center">
                    <td class="menu">Telnet</td>
                </tr>
                <tr>
                    <td>
                        <input type="checkbox" name="remote_telnet" onclick="telnet_changed();" $TELNET_CHECKED >&nbsp;Enable Telnet&nbsp;on port <input name="remote_telnet_port" size="5" maxlength="5" value="$REMOTE_TELNET_PORT">
                    </td>
                </tr>
                <tr>
                    <td>
                        <input type="checkbox" name="remote_telnet_ext" onclick="ssh_changed();" $TELNET_EXT_CHECKED >&nbsp;Enable WAN access to Telnet &nbsp;on port <input name="remote_telnet_ext_port" size="5" maxlength="5" value="$REMOTE_TELNET_EXT_PORT">
                    </td>
                </tr>
            </table>
          <table width="100%">
                 <tr align="center">
                    <td class="menu">SNMP</td>
                </tr>
                <tr>
                    <td>
                        <input type="checkbox" name="remote_snmp_ext" onclick="snmp_changed();" $SNMP_EXT_CHECKED >&nbsp;Enable WAN access to SNMP &nbsp;on port <input name="remote_snmp_ext_port" size="5" maxlength="5" value="$REMOTE_SNMP_EXT_PORT">
                    </td>
                </tr>
            </table>
          <table width="100%">
                 <tr align="center">
                    <td class="menu">Ping</td>
                </tr>
                <tr>
                    <td>
                        <input type="checkbox" name="remote_allow_ping" $ALLOW_PING >&nbsp;Allow remote ping
                    </td>
                </tr>
            </table>
        </td>
    </tr>
<tr>
    <td><input type="submit" value="Save"></td>
</tr>
</table>
</form>
EOF

cat include/end.inc
