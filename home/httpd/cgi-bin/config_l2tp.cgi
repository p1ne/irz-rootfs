#!/bin/sh

[ -e /mnt/rwfs/settings/settings.l2tp ] && . /mnt/rwfs/settings/settings.l2tp
[ "$L2TP_ENABLED" = "1" ] && en="checked"
[ "$L2TP_DEFAULT_ROUTE" = "1" ] && def="checked"
if [ "$L2TP_MODE" = "client" ]; then
    cl="selected"
else
    sr="selected"
fi
[ -z "$L2TP_PORT" ] && L2TP_PORT=1701

./begin $0

echo "</td><td colspan=\"3\" valign=\"top\">"
cat include/js.inc
echo "</script>"
cat << EOF
<form name="input" onsubmit="return CheckForm();" action="config_l2tp_set.cgi" method="post">
	<table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
		<td class="title" align="center">
			<b>L2TP settings</b>
		</td>
	</tr>
	<tr>
		<td>
			<table>
			<tr>
				<td><input name="l2tp_enabled"  type="checkbox" $en >L2TP enable</td>
			</tr>
			<tr>
				<td>L2TP mode</td>
				<td>
				    <select class="input" name="l2tp_mode" onChange="modeChange()">
                        <option value="client" $cl>Client</option>
                        <option value="server" $sr>Server</option>
				    </select>
                </td>
			</tr>
			<tr>
				<td>Server IP</td>
				<td><input name="l2tp_server_ip" class="input" value="$L2TP_SERVER_IP"></td>
			</tr>
			<tr>
				<td>Client Start IP Address</td>
				<td><input name="l2tp_client_start" class="input" value="$L2TP_CLIENT_START"></td>
			</tr>
			<tr>
				<td>Client End IP Address</td>
				<td><input name="l2tp_client_end" class="input" value="$L2TP_CLIENT_END"></td>
			</tr>
			<tr>
				<td>UDP Port</td>
				<td><input name="l2tp_port" class="input" value="$L2TP_PORT" ></td>
			</tr>
			<tr>
				<td>Redial Timeout (sec)</td>
				<td><input name="l2tp_redial_timeout" class="input" value="$L2TP_REDIAL_TIMEOUT" ></td>
			</tr>
			<tr>
				<td>Default route</td>
				<td><input name="l2tp_default_route" class="input" type=checkbox $def></td>
			</tr>
			<tr>
				<td>Username *</td>
				<td><input name="l2tp_username" class="input" value="$L2TP_USERNAME"></td>
			</tr>
			<tr>
				<td>Password *</td>
				<td><input name="l2tp_password" type="password" class="input" value="$L2TP_PASSWORD"></td>
			</tr>			
			<tr>
				<td>Local Interface IP Address *</td>
				<td><input name="l2tp_local_ip" class="input" value="$L2TP_LOCAL_IP"></td>
			</tr>
			<tr>
				<td>Remote Interface IP Address *</td>
				<td><input name="l2tp_remote_ip" class="input" value="$L2TP_REMOTE_IP"></td>
			</tr>
			<tr>
				<td>Remote Subnet *</td>
				<td><input name="l2tp_remote_network" class="input" value="$L2TP_REMOTE_NETWORK"></td>
			</tr>
			<tr>
				<td>Remote Subnet Mask *</td>
				<td><input name="l2tp_remote_netmask" class="input" value="$L2TP_REMOTE_NETMASK"></td>
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
function modeChange(){
    if(document.input.l2tp_mode.value == 'client'){
            document.getElementsByName('l2tp_server_ip')[0].disabled = false;
            document.getElementsByName('l2tp_redial_timeout')[0].disabled = false;
            document.getElementsByName('l2tp_default_route')[0].disabled = false;
            //document.getElementsByName('l2tp_remote_network')[0].disabled = false;
            //document.getElementsByName('l2tp_remote_netmask')[0].disabled = false;
            document.getElementsByName('l2tp_client_start')[0].disabled = true;
            document.getElementsByName('l2tp_client_end')[0].disabled = true;
        }
    else{
            document.getElementsByName('l2tp_server_ip')[0].disabled = true;
            document.getElementsByName('l2tp_redial_timeout')[0].disabled = true;
            document.getElementsByName('l2tp_default_route')[0].disabled = true;
            //document.getElementsByName('l2tp_remote_network')[0].disabled = true;
            //document.getElementsByName('l2tp_remote_netmask')[0].disabled = true;
            document.getElementsByName('l2tp_client_start')[0].disabled = false;
            document.getElementsByName('l2tp_client_end')[0].disabled = false;
        }
    }
    
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
        if(!document.getElementsByName('l2tp_enabled')[0].checked) {
            return true;
        }
        if( document.getElementsByName('l2tp_mode')[0].value == 'client' ) {
            if ( !IsValidIP(document.getElementsByName('l2tp_server_ip')[0], !document.getElementsByName('l2tp_enabled')[0].checked) ) {
                alert("Invalid or missing IP address.");
                document.input.l2tp_server_ip.focus();
                return false;
            }
            tout = parseInt(document.input.l2tp_redial_timeout.value);
            if( (tout == '' ) || ( tout < 1) || (tout != document.input.l2tp_redial_timeout.value) ){
                alert('Invalid redial timeout.');
                document.input.l2tp_redial_timeout.focus();
                return false;
            }
        }
        s = document.getElementsByName('l2tp_local_ip')[0];
        if( s.value.length > 0 )
            if ( !IsValidIP(s, !document.getElementsByName('l2tp_enabled')[0].checked) ) {
                alert("Invalid IP address.");
                document.input.l2tp_local_ip.focus();
                return false;
            }
        s = document.getElementsByName('l2tp_remote_ip')[0];
        if( s.value.length > 0 )
            if ( !IsValidIP(s, !document.getElementsByName('l2tp_enabled')[0].checked) ) {
                alert("Invalid IP address.");
                document.input.l2tp_remote_ip.focus();
                return false;
            }
        s = document.getElementsByName('l2tp_remote_network')[0];
        if( s.value.length > 0 )
            if ( !IsValidIP(s, !document.getElementsByName('l2tp_enabled')[0].checked) ) {
                alert("Invalid subnet address.");
                document.input.l2tp_remote_network.focus();
                return false;
            }
        s = document.getElementsByName('l2tp_remote_netmask')[0];
        if( s.value.length > 0 )
            if ( !IsValidIP(s, !document.getElementsByName('l2tp_enabled')[0].checked) ) {
                alert("Invalid subnet mask.");
                document.input.l2tp_remote_netmask.focus();
                return false;
            }

        port = parseInt(document.input.l2tp_port.value);
        if( (port > 65535) || (port < 1) || (port != document.input.l2tp_port.value) ){
            alert('Invalid port nubmer.');
            document.input.l2tp_port.focus();
            return false;
            }
		return true;
	}
    
window.onload = modeChange();
</script>

EOF
cat include/end.inc
