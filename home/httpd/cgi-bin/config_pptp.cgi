#!/bin/sh

[ -e /mnt/rwfs/settings/settings.pptp ] && . /mnt/rwfs/settings/settings.pptp
[ "$PPTP_ENABLED" = "1" ] && en="checked"
[ "$PPTP_PAP" = "1" ] && pap="checked"
[ "$PPTP_CHAP" = "1" ] && chap="checked"
[ "$PPTP_MPPE" = "1" ] && mppe="checked"


./begin $0

echo "</td><td colspan=\"3\" valign=\"top\">"
cat include/js.inc
echo "</script>"
cat << EOF
<form name="input" onsubmit="return CheckForm();" action="config_pptp_set.cgi" method="post">
	<table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
		<td class="title" align="center">
			<b>PPTP client settings</b>
		</td>
	</tr>
	<tr>
		<td>
			<table>
			<tr>
				<td><input name="pptp_enabled"  type="checkbox" $en >Enable PPTP</td>
			</tr>
			<tr>
				<td>Server IP</td>
				<td><input name="pptp_server_ip" class="input" value="$PPTP_SERVER_IP"></td>
			</tr>
            <tr>
                <td>Username *</td>
                <td><input name="pptp_username" class="input" value="$PPTP_USERNAME"></td>
            </tr>
            <tr>
                <td>Password *</td>
                <td><input name="pptp_password" type="password" class="input" value="$PPTP_PASSWORD"></td>
            </tr>          
			<tr>
				<td>Options</td>
				<td>
                    <input name="pptp_pap" type=checkbox $pap>PAP&nbsp;
                    <input name="pptp_chap" type=checkbox $chap>CHAP&nbsp;
                    <input name="pptp_mppe" type=checkbox $mppe>MPPE&nbsp;
                </td>
			</tr>
			<tr>
				<td>Local Interface IP Address *</td>
				<td><input name="pptp_local_ip" class="input" value="$PPTP_LOCAL_IP"></td>
			</tr>
			<tr>
				<td>Remote Interface IP Address *</td>
				<td><input name="pptp_remote_ip" class="input" value="$PPTP_REMOTE_IP"></td>
			</tr>
			<tr>
				<td>Remote Subnet *</td>
				<td><input name="pptp_remote_network" class="input" value="$PPTP_REMOTE_NETWORK"></td>
			</tr>
			<tr>
				<td>Remote Subnet Mask *</td>
				<td><input name="pptp_remote_netmask" class="input" value="$PPTP_REMOTE_NETMASK"></td>
			</tr>
            <tr>
                <td>Additional PPP options *</td>
                <td><input name="pptp_ppp_options" class="input" value="$PPTP_PPP_OPTIONS"></td>
            </tr>
			</table>
		</td>
	</tr>
	<tr>
		<td><input type="submit" name="apply" value="Apply"></td>
	</tr>
	</table>
</form>

<script language="JavaScript" type="text/javascript">
    
function GetValue(obj) {
		return obj.value.replace(/\s/g, '');
	}

function IsValidIP(obj, zero) {
		var str = GetValue(obj);
		if (zero && str.length == 0) {
			return true;
		}
		var fields = str.match(/^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$/);
		if (fields != null) {
			var tmp = fields[1] | fields[2] | fields[3] | fields[4];
			return (tmp < 256) && (zero || tmp > 0);
		} else {
			return false;
		}
	}
    
function CheckForm() {
        if(!document.getElementsByName('pptp_enabled')[0].checked) {
            return true;
        }
        if( document.getElementsByName('pptp_mode')[0].value == 'client' ) {
            if ( !IsValidIP(document.getElementsByName('pptp_server_ip')[0], !document.getElementsByName('pptp_enabled')[0].checked) ) {
                alert("Invalid or missing IP address.");
                document.input.pptp_server_ip.focus();
                return false;
            }
            tout = parseInt(document.input.pptp_redial_timeout.value);
            if( (tout == '' ) || ( tout < 1) || (tout != document.input.pptp_redial_timeout.value) ){
                alert('Invalid redial timeout.');
                document.input.pptp_redial_timeout.focus();
                return false;
            }
        }
        s = document.getElementsByName('pptp_local_ip')[0];
        if( s.value.length > 0 )
            if ( !IsValidIP(s, !document.getElementsByName('pptp_enabled')[0].checked) ) {
                alert("Invalid IP address.");
                document.input.pptp_local_ip.focus();
                return false;
            }
        s = document.getElementsByName('pptp_remote_ip')[0];
        if( s.value.length > 0 )
            if ( !IsValidIP(s, !document.getElementsByName('pptp_enabled')[0].checked) ) {
                alert("Invalid IP address.");
                document.input.pptp_remote_ip.focus();
                return false;
            }
        s = document.getElementsByName('pptp_remote_network')[0];
        if( s.value.length > 0 )
            if ( !IsValidIP(s, !document.getElementsByName('pptp_enabled')[0].checked) ) {
                alert("Invalid subnet address.");
                document.input.pptp_remote_network.focus();
                return false;
            }
        s = document.getElementsByName('pptp_remote_netmask')[0];
        if( s.value.length > 0 )
            if ( !IsValidIP(s, !document.getElementsByName('pptp_enabled')[0].checked) ) {
                alert("Invalid subnet mask.");
                document.input.pptp_remote_netmask.focus();
                return false;
            }

        port = parseInt(document.input.pptp_port.value);
        if( (port > 65535) || (port < 1) || (port != document.input.pptp_port.value) ){
            alert('Invalid port nubmer.');
            document.input.pptp_port.focus();
            return false;
            }
		return true;
	}
    
</script>

EOF
cat include/end.inc
