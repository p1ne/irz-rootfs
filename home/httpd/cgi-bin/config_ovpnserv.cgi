#!/bin/sh
[ -e /mnt/rwfs/settings/settings.ovpns ] && . /mnt/rwfs/settings/settings.ovpns

[ "$OVPNS_ENABLED" = "1" ] && checked="checked"
[ "$OVPNS_PROTO" = "tcp" ] && tcp="selected"
[ "$OVPNS_PROTO" = "udp" ] && udp="selected"
[ "$OVPN1_ENABLED" = "1" ] && selected1="selected"
[ "$OVPN2_ENABLED" = "1" ] && selected2="selected"
[ "$OVPN3_ENABLED" = "1" ] && selected3="selected"
[ "$OVPN4_ENABLED" = "1" ] && selected4="selected"
[ "$OVPN5_ENABLED" = "1" ] && selected5="selected"

OVPN1_DESC=`decode $OVPN1_DESC`
OVPN1_NAME=`decode $OVPN1_NAME`
OVPN2_DESC=`decode $OVPN2_DESC`
OVPN2_NAME=`decode $OVPN2_NAME`
OVPN3_DESC=`decode $OVPN3_DESC`
OVPN3_NAME=`decode $OVPN3_NAME`
OVPN4_DESC=`decode $OVPN4_DESC`
OVPN4_NAME=`decode $OVPN4_NAME`
OVPN5_DESC=`decode $OVPN5_DESC`
OVPN5_NAME=`decode $OVPN5_NAME`

./begin $0

echo "</td><td colspan=\"3\" valign=\"top\">"

cat << EOF
<script language="JavaScript" type="text/javascript">
<!--

function Error(msg, obj) {
	alert(msg); obj.focus(); obj.select(); return false;
}

function IsEmpty(obj) {
	return GetValue(obj).length == 0;
}

function CheckForm() {
	if (document.input.ovpns_enabled.checked) {
      if (IsEmpty(document.input.ovpns_config) || document.input.ovpns_config.value.length > 3000) {
        return Error("Missing or invalid server configuration", document.input.ovpns_config);
      }
      if (IsEmpty(document.input.ovpns_ca_cert) || document.input.ovpns_ca_cert.value.length > 3000) {
        return Error("Missing or invalid CA Certificate", document.input.ovpns_ca_cert);
      }
      if (IsEmpty(document.input.ovpns_dh_params) || document.input.ovpns_dh_params.value.length > 3000) {
		return Error("Missing or invalid DH parameters", document.input.ovpns_dh_params);
      }
      if (IsEmpty(document.input.ovpns_local_cert) || document.input.ovpns_local_cert.value.length > 3000) {
		return Error("Missing or invalid local certificate", document.input.ovpns_local_cert);
      }
      if (IsEmpty(document.input.ovpns_local_key) || document.input.ovpns_local_key.value.length > 3000) {
		return Error("Missing or invalid local private key", document.input.ovpns_local_key);
      }
	}
	return true;
}
//-->
</script>
      <form name="input" onsubmit="return CheckForm();" action="config_ovpnserv_set.cgi" method="post">
      <table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
	  <td align="center" class="title"><b>OpenVPN Server Configuration</b></td>
	</tr>
	<tr>
	  <td>
        <table width="100%">
            <tr><td class="menu" align="center">Server Configuration</td></tr>
        </table>
	 	<table>
	    <tr><td><input type="checkbox" name="ovpns_enabled" $checked></td>
		<td nowrap>Start OpenVPN Server</td></tr>
	    </table>
	    <table>
		  <tr><td>Protocol</td><td><select name="ovpns_proto"><option value="udp" $udp>UDP&nbsp;<option value="tcp" $tcp>TCP&nbsp;</select></td></tr>
		  <tr><td>Port</td><td><input name="ovpns_port" maxlength="5" value="$OVPNS_PORT"></td></tr>
	      <tr>
        <td nowrap id="config" class="td1">Server Configuration</td>
        <td nowrap>
<textarea cols="65" rows="7" name="ovpns_config">
EOF
echo "$OVPNS_CONFIG" | base64 -d  
cat << EOF
</textarea>
        </td>
	      </tr>
	      <tr>
		<td nowrap id="ca_cert" class="td1">CA Certificate</td>
		<td nowrap>
<textarea cols="65" rows="3" name="ovpns_ca_cert">
EOF
echo -n "$OVPNS_CA_CERT" | base64 -d
cat << EOF
</textarea>
		</td>
	      </tr>
	      <tr>
		<td nowrap id="dh_params" class="td1">DH Parameters</td>
		<td nowrap>
<textarea cols="65" rows="3" name="ovpns_dh_params">
EOF
echo -n "$OVPNS_DH_PARAMS" | base64 -d
cat << EOF
</textarea>
		</td>
	      </tr>
	      <tr>
		<td nowrap id="local_cert" class="td1">Local Certificate</td>
		<td nowrap>
<textarea cols="65" rows="3" name="ovpns_local_cert">
EOF
echo -n "$OVPNS_LOCAL_CERT" |base64 -d
cat << EOF
</textarea>
		</td>
	      </tr>
	      <tr>
		<td nowrap id="local_key" class="td1">Local Private Key</td>
		<td nowrap>
<textarea cols="65" rows="3" name="ovpns_local_key">
EOF
echo -n "$OVPNS_LOCAL_KEY" |base64 -d
cat << EOF
</textarea>
		</td>
	      </tr>
	    </table>
		<table width="100%">
			<tr><td class="menu" align="center">Clients Configuration</td></tr>
		</table>
        <table cellspacing="5">
          <tr>
            <th>#</th>
            <th>Enable</th>
            <th>Description</th>
            <th>Client Name</th>
            <th>&nbsp;</th>
          </tr>
          <tr>
            <td>1.</td>
            <td><select name="ovpn1_enabled"><option value="">no&nbsp;</option><option value="on" $selected1>yes&nbsp;</option></select></td>
            <td><input name="ovpn1_description" value="$OVPN1_DESC" readonly></td>
            <td><input name="ovpn1_name" value="$OVPN1_NAME" readonly></td>
            <td><a href="config_ovpnservn.cgi?tun=1"><font color="#000000"><b>[ Edit ]</b></font></a></td>
          </tr>
          <tr>
            <td>2.</td>
            <td><select name="ovpn2_enabled"><option value="">no&nbsp;</option><option value="on" $selected2>yes&nbsp;</option></select></td>
            <td><input name="ovpn2_description" value="$OVPN2_DESC" readonly></td>
            <td><input name="ovpn2_name" value="$OVPN2_NAME" readonly></td>
            <td><a href="config_ovpnservn.cgi?tun=2"><font color="#000000"><b>[ Edit ]</b></font></a></td>
          </tr>
          <tr>
            <td>3.</td>
            <td><select name="ovpn3_enabled"><option value="">no&nbsp;</option><option value="on" $selected3>yes&nbsp;</option></select></td>
            <td><input name="ovpn3_description" value="$OVPN3_DESC" readonly></td>
            <td><input name="ovpn3_name" value="$OVPN3_NAME" readonly></td>
            <td><a href="config_ovpnservn.cgi?tun=3"><font color="#000000"><b>[ Edit ]</b></font></a></td>
          </tr>
          <tr>
            <td>4.</td>
            <td><select name="ovpn4_enabled"><option value="">no&nbsp;</option><option value="on" $selected4>yes&nbsp;</option></select></td>
            <td><input name="ovpn4_description" value="$OVPN4_DESC" readonly></td>
            <td><input name="ovpn4_name" value="$OVPN4_NAME" readonly></td>
            <td><a href="config_ovpnservn.cgi?tun=4"><font color="#000000"><b>[ Edit ]</b></font></a></td>
          </tr>
          <tr>
            <td>5.</td>
            <td><select name="ovpn5_enabled"><option value="">no&nbsp;</option><option value="on" $selected5>yes&nbsp;</option></select></td>
            <td><input name="ovpn5_description" value="$OVPN5_DESC" readonly></td>
            <td><input name="ovpn5_name" value="$OVPN5_NAME" readonly></td>
            <td><a href="config_ovpnservn.cgi?tun=5"><font color="#000000"><b>[ Edit ]</b></font></a></td>
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
      <!--
      document.input.ovpns_enabled.focus();
      //-->
      </script>

EOF

cat include/end.inc
