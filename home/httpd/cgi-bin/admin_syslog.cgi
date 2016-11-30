#!/bin/sh

[ -e /mnt/rwfs/settings/settings.syslog ] && . /mnt/rwfs/settings/settings.syslog

[ "$SYSLOG_LOCALLY" = "1" -a "$SYSLOG_NETWORK" = "0" ] && sel1="selected" && flag=true
[ "$SYSLOG_LOCALLY" = "0" -a "$SYSLOG_NETWORK" = "1" ] && sel2="selected" && flag=true
[ "$SYSLOG_LOCALLY" = "1" -a "$SYSLOG_NETWORK" = "1" ] && sel3="selected" && flag=true
[ "$flag" != "true" ] && sel1="selected"

./begin $0

echo "</td><td colspan=\"3\" valign=\"top\">"
cat include/js.inc
cat << EOF
            function ModeChanged() {
                if (document.input.syslog_mode.value == "1") {
                    document.input.syslog_server.disabled = true;
                    document.input.syslog_server.value = "";
                    document.input.syslog_server_port.disabled = true;
                    document.input.syslog_server_port.value = "";
                } else {
                    document.input.syslog_server.disabled = false;
                    document.input.syslog_server_port.disabled = false;
                }
            }

            function CheckForm() {
                if (document.input.syslog_mode.value != "1") {
                    if (IsEmpty(document.input.syslog_server)) {
                        alert("Remote Syslog server address can't be blank");
                        Focus(document.input.syslog_server);
                        return false;
                    }
                }
                if (!IsValidIP(document.input.syslog_server, true)) {
                    re = /(www\.)?([^\.]+)\.(\w{2}|(com|net|org|edu|int|mil|gov|arpa|biz|aero|name|coop|info|pro|museum))$/;
                    if (!re.test(document.input.syslog_server.value)) {
                        alert("Invalid Remote Syslog server address");
                        Focus(document.input.syslog_server);
                        return false;
                    }
                }
                if (!IsValidPort(document.input.syslog_server_port, true)) {
                    alert("Invalid Remote Syslog server port");
                    Focus(document.input.syslog_server_port);
                    return false;
                }
                return true;
            }
            //-->
        </script>
        <form name="input" onsubmit="return CheckForm();" action="admin_syslog_set.cgi" method="post">
            <table width="100%" cellspacing="0" cellpadding="5" border="3">
                <tr>
                    <td class="title" align="center">
                        <b>Syslog Configuration</b>
                    </td>
                </tr>
                <tr>
                    <td>
                        <table>
                            <tr>
                                <td nowrap>Syslog mode</td>
                                <td>
                                    <select name="syslog_mode" onchange="ModeChanged()">
                                        <option value="1" $sel1>Log locally only
                                        <option value="2" $sel2>Log via network only
                                        <option value="3" $sel3>Log locally and via network
                                    </select>
                                </td>
                            </tr>
                            <tr>
                                <td nowrap>Syslog server address</td>
                                <td><input name="syslog_server" value="$SYSLOG_NETWORK_ADDRESS" /></td>
                            </tr>
                            <tr>
                                <td nowrap>Syslog server port *</td>
                                <td><input name="syslog_server_port" value="$SYSLOG_NETWORK_PORT" /></td>
                            </tr>
                            <tr>
                                <td colspan="6"><i>* can be blank</i></td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr>
                    <td><input type="submit" name="apply" value="Apply" /></td>
                </tr>
            </table>
        </form>
        <script language="JavaScript" type="text/javascript">
            <!--
            document.input.syslog_mode.focus();
            ModeChanged()
            //-->
        </script>
EOF

cat include/end.inc

