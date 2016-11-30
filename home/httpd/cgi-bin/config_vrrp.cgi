#!/bin/sh

[ -e /mnt/rwfs/settings/settings.vrrp ] && . /mnt/rwfs/settings/settings.vrrp

./begin $0


[ "$VRRP_ENABLE" = "1" ] && ENABLE="checked"

[ "$VRRP_AUTH" = "none" ] && none_selected="selected"
[ "$VRRP_AUTH" = "simple" ] && simple_selected="selected"
[ "$VRRP_AUTH" = "ah" ] && ah_selected="selected"

echo "</td><td colspan=\"3\" valign=\"top\">"
cat << EOF
<script language="JavaScript" type="text/javascript">
<!--
	function Focus(obj) {
		obj.focus(); obj.select();
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
		if ( !IsValidIP(vrrp_ip, !vrrp_enable) ) {
			alert("Invalid or missing IP address.");
			Focus(document.input.vrrp_ip);
			return false;
		}
		
		if ( GetValue(vrrp_priority) > 255 || GetValue(vrrp_priority) < 0 ){
			alert("Invalid priority.");
			Focus(document.input.vrrp_priority);
			return false;
		}
		
		return true;
	}
	
	function AuthChanged() {
	var secret = document.input.vrrp_auth.value == "none";
	document.input.vrrp_password.disabled = secret;
	document.getElementById('vrrp_password').style.color = (secret) ? "gray" : "";	
      }
    window.onload=AuthChanged();
//-->
</script>

<form name="input" onsubmit="return CheckForm();" action="config_vrrp_set.cgi" method="post">
	<table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
		<td class="title" align="center">
			<b>VRRP settings</b>
		</td>
	</tr>
	<tr>
		<td>
			<table>
			<tr>
				<td><input name="vrrp_enable"  type="checkbox" $ENABLE> VRRP enable</td>
			</tr>
			<tr>
				<td>Instance name</td>
				<td><input name="vrrp_instance" class="input" value="$VRRP_INSTANCE"></td>
			</tr>
			<tr>
				<td>Instance IP</td>
				<td><input name="vrrp_ip" class="input" value="$VRRP_IP"></td>
			</tr>
			<tr>
				<td>Instance router ID</td>
				<td><input name="vrrp_router_id" class="input" value="$VRRP_ROUTER_ID"></td>
			</tr>
			<tr>
				<td>Instance priority</td>
				<td><input name="vrrp_priority" class="input" value="$VRRP_PRIORITY"></td>
			</tr>			
			<tr>
				<td>Instance authentication:</td>
				<td>
				    <select class="input" name="vrrp_auth" onChange="AuthChanged()">
					<option value="none" $none_selected>None</option>
					<option value="simple" $simple_selected>Simple</option>
					<option value="ah" $ah_selected>AH</option>
				    </select>
				</td>
			</tr>
			<tr>
				<td>Instance password</td>
				<td><input name="vrrp_password" class="input" type="password" value="`decode "$VRRP_PASSWORD"`"></td>
			</tr>
			<tr>
				<td>SMTP server</td>
				<td><input name="vrrp_smtp" class="input" value="$VRRP_SMTP"></td>
			</tr>
			<tr>
				<td>From mail</td>
				<td><input name="vrrp_srv_mail" class="input" value="$VRRP_SRV_MAIL"></td>
			</tr>
			<tr>
				<td>To mail</td>
				<td><input name="vrrp_email" class="input" value="$VRRP_EMAIL"></td>
			</tr>
			</table>
		</td>
	</tr>
	<tr>
		<td><input type="submit" name="apply" value="Apply"></td>
	</tr>
	</table>
</form>
EOF

cat include/end.inc
