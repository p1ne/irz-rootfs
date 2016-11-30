#!/bin/sh
[ -e /mnt/rwfs/settings/settings.openvpn ] && . /mnt/rwfs/settings/settings.openvpn

[ "$OPENVPN_ENABLED" = "1" ] && enabled="checked"
[ "$OPENVPN_DEVICE" = "tap0" ] && devtap="selected" || devtun="selected"
[ "$OPENVPN_PROTO" = "udp" ] && udp="selected"
[ "$OPENVPN_PROTO" = "tcp-server" ] && tcps="selected"
[ "$OPENVPN_PROTO" = "tcp-client" ] && tcpc="selected"
[ "$OPENVPN_COMP" = "lzo" ] && comp_lzo="selected"
[ "$OPENVPN_COMP" = "none" ] && comp_none="selected"
[ "$OPENVPN_NAT" = "0" ] && nat0="selected"
[ "$OPENVPN_NAT" = "1" ] && nat1="selected"
[ "$OPENVPN_REDIRECT_GW" = "1" ] && redirect_gw="selected"
[ "$OPENVPN_AUTH" = "none" ] && auth_none="selected"
[ "$OPENVPN_AUTH" = "secret" ] && auth_secret="selected"
[ "$OPENVPN_AUTH" = "passwd" ] && auth_passwd="selected"
[ "$OPENVPN_AUTH" = "tls-client" ] && auth_tlsc="selected"
[ "$OPENVPN_AUTH" = "tls-server" ] && auth_tlss="selected"
[ "$OPENVPN_AUTH" = "tls-mclient" ] && auth_tlsm="selected"

./begin $0

echo "</td><td colspan=\"3\" valign=\"top\">"

cat << EOF
      <script language="JavaScript" type="text/javascript">
      <!--
      function Error(msg, obj) {
	alert(msg); obj.focus(); obj.select(); return false;
      }
      function GetValue(obj) {
	return obj.value.replace(/\s/g, '');
      }
      function IsEmpty(obj) {
	return GetValue(obj).length == 0;
      }
      function IsInRange(obj, low, high, empty) {
	var str = GetValue(obj);
	if (empty && str.length == 0) return true;
	return (parseInt(str) >= low) && (parseInt(str) <= high);
      }
      function IsValidMAC(obj, empty) {
	var str = GetValue(obj);
	if (empty && str.length == 0) return true;
	return str.search(/^[0-9a-fA-F]{1,2}(:[0-9a-fA-F]{1,2}){5}$/) >= 0;
      }
      function IsValidIP(obj, empty) {
	var str = GetValue(obj);
	if (empty && str.length == 0) return true;
	var fields = str.match(/^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$/);
	if (fields != null) {
	  var tmp = fields[1] | fields[2] | fields[3] | fields[4];
	  return (tmp < 256) && (empty || tmp > 0);
	} else {
	  return false;
	}
      }
    function IsValidURL(obj, zero) {
        var str = GetValue(obj);
        if (zero && str.length == 0) {
                return true;
        }
        re = /(www\.)?([^\.]+)\.(\w{2}|(com|net|org|edu|int|mil|gov|arpa|biz|aero|name|coop|info|pro|museum))$/;
        if (re.test(obj.value)) {
                return true;
        } else {
                return false;
        }
    }
      function IsValidPort(obj, empty) {
	var str = GetValue(obj);
	if (empty && str.length == 0) return true;
	var value = parseInt(str);
	return (value > 0) && (value < 65536);
      }
      function CheckForm() {

    var noremote = (document.input.openvpn_proto.value != 'tcp-client');
    if (!IsValidIP(document.input.openvpn_remote_ipaddr, noremote)) {
		if (!IsValidURL(document.input.openvpn_remote_ipaddr, noremote)) {
      		return Error("Invalid remote IP address or URL", document.input.openvpn_remote_ipaddr);
		}
    }
	if (!IsValidPort(document.input.openvpn_port, !document.input.openvpn_enabled.checked)) {
	  return Error("Missing or invalid TCP/UDP port", document.input.openvpn_port);
	}
	if (!IsValidIP(document.input.openvpn_remote_network, true)) {
	  return Error("Invalid remote subnet", document.input.openvpn_remote_network);
	}
	if (!IsValidIP(document.input.openvpn_remote_netmask, true)) {
	  return Error("Invalid remote subnet mask", document.input.openvpn_remote_netmask);
	}

	if (!IsInRange(document.input.openvpn_ping_intvl, 1, 86400, true)) {
	  return Error("Invalid keepalive interval", document.input.openvpn_ping_intvl);
	}
	if (!IsInRange(document.input.openvpn_ping_tout, 1, 86400, true)) {
	  return Error("Invalid keepalive timeout", document.input.openvpn_ping_tout);
	}
	if (!IsInRange(document.input.openvpn_reneg_sec, 0, 86400, true)) {
	  return Error("Invalid renegotiate interval", document.input.openvpn_reneg_sec);
	}
	if (!IsInRange(document.input.openvpn_hand_window, 1, 86400, true)) {
	  return Error("Invalid handshake window", document.input.openvpn_hand_window);
	}
	if (!IsInRange(document.input.openvpn_inactive, 0, 86400, true)) {
	  return Error("Invalid inactivity timeout", document.input.openvpn_inactive);
	}
	if (!IsInRange(document.input.openvpn_fragment, 128, 16384, true)) {
	  return Error("Invalid max fragment size", document.input.openvpn_fragment);
	}
	if (document.input.openvpn_enabled.checked) {
	  if (document.input.openvpn_auth.value == 'secret') {
	    if (IsEmpty(document.input.openvpn_secret) || document.input.openvpn_secret.value.length > 3000) {
	      return Error("Missing or invalid pre-shared secret", document.input.openvpn_secret);
	    }
	  } else if (document.input.openvpn_auth.value != 'none') {
	    if (IsEmpty(document.input.openvpn_ca_cert) || document.input.openvpn_ca_cert.value.length > 6000) {
	      return Error("Missing or invalid CA certificate", document.input.openvpn_ca_cert);
	    }
	    if (document.input.openvpn_auth.value == 'tls-server') {
	      if (IsEmpty(document.input.openvpn_dh_params) || document.input.openvpn_dh_params.value.length > 6000) {
		return Error("Missing or invalid DH parameters", document.input.openvpn_dh_params);
	      }
	    }
	    if (document.input.openvpn_auth.value != 'passwd') {
	      if (IsEmpty(document.input.openvpn_local_cert) || document.input.openvpn_local_cert.value.length > 6000) {
		return Error("Missing or invalid local certificate", document.input.openvpn_local_cert);
	      }
	      if (IsEmpty(document.input.openvpn_local_key) || document.input.openvpn_local_key.value.length > 6000) {
		return Error("Missing or invalid local private key", document.input.openvpn_local_key);
	      }
	    } else {
	      if (IsEmpty(document.input.openvpn_username)) {
		return Error("Missing username", document.input.openvpn_username);
	      }
	      if (IsEmpty(document.input.openvpn_password)) {
		return Error("Missing password", document.input.openvpn_password);
	      }
	    }
	  }
	}
    if (!IsValidIP(document.input.openvpn_ping2_ip, true)) {
      return Error("Invalid Ping IP Address", document.input.openvpn_ping2_ip);
    }
    if (!IsInRange(document.input.openvpn_ping2_int, 1, 1440, true)) {
      return Error("Invalid ping interval", document.input.openvpn_ping2_int);
    }
    if (!IsInRange(document.input.openvpn_ping2_allow, 0, 100, true)) {
      return Error("Invalid number of failures", document.input.openvpn_ping2_allow);
    }
	return true;
      }
      function ProtoChanged() {
	var udp = document.input.openvpn_proto.value == "udp";
	document.getElementById('port').innerHTML = udp ? "UDP port" : "TCP port";
      }
      function AuthChanged() {
	var secret  = document.input.openvpn_auth.value == "secret";
	var passwd  = document.input.openvpn_auth.value == "passwd";
	var mclient = document.input.openvpn_auth.value == "tls-mclient";
	var client  = document.input.openvpn_auth.value == "tls-client";
	var server  = document.input.openvpn_auth.value == "tls-server";
	document.input.openvpn_local_if_ipaddr.disabled = (passwd | mclient );
	document.input.openvpn_remote_if_ipaddr.disabled = (passwd | mclient );
	document.input.openvpn_reneg_sec.disabled = !(passwd | mclient | client | server);
	document.input.openvpn_secret.disabled = !secret;
	document.input.openvpn_ca_cert.disabled = !(passwd | mclient | client | server);
	document.input.openvpn_dh_params.disabled = !server;
	document.input.openvpn_local_cert.disabled = !(mclient | client | server);
	document.input.openvpn_local_key.disabled = !(mclient | client | server);
	document.input.openvpn_username.disabled = !passwd;
	document.input.openvpn_password.disabled = !passwd;
	document.getElementById('local_if').style.color = (passwd | mclient ) ? "gray" : "";
	document.getElementById('remote_if').style.color = (passwd | mclient ) ? "gray" : "";
	document.getElementById('reneg_sec').style.color = (passwd | mclient | client | server) ? "" : "gray";
	document.getElementById('secret').style.color = secret ? "" : "gray";
	document.getElementById('ca_cert').style.color = (passwd | mclient | client | server) ? "" : "gray";
	document.getElementById('dh_params').style.color = server ? "" : "gray";
	document.getElementById('local_cert').style.color = (mclient | client | server) ? "" : "gray";
	document.getElementById('local_key').style.color = (mclient | client | server) ? "" : "gray";
	document.getElementById('username').style.color = passwd ? "" : "gray";
	document.getElementById('password').style.color = passwd ? "" : "gray";
    }
    function devChanged() {
        var dev = document.input.openvpn_device.value == "tun0";
        document.getElementById('remote_if').innerHTML = dev ? "Remote Interface IP Address" : "Local Interface Network Mask";
    }
      //-->
      </script>
      <form name="input" onsubmit="return CheckForm();" action="config_openvpn_set.cgi" method="post">
      <table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
	  <td class="title" align="center"><b>OpenVPN Tunnel Configuration</b></td>
	</tr>
	<tr>
	  <td>
<!-- chechbox table -->
	    <table>
	      <tr>
		<td><input type="checkbox" name="openvpn_enabled" $enabled></td>
		<td nowrap>Create OpenVPN tunnel</td>
	      </tr>
	    </table>
<!-- settings table -->
	    <table>
		  <tr>
			<td>
<table>
		  <tr>
        <td nowrap>Device</td>
        <td><select onChange="devChanged()" class="input" name="openvpn_device"><option value="tun0" $devtun>TUN0<option value="tap0" $devtap>TAP0</select></td>
          </tr>
          <tr>
		<td nowrap>Protocol</td>
		<td><select class="input" name="openvpn_proto" onChange="ProtoChanged()"><option value="udp" $udp>UDP<option value="tcp-server" $tcps>TCP server<option value="tcp-client" $tcpc>TCP client</select></td>
	      </tr>
	      <tr>
		<td nowrap id="port">TCP/UDP Port</td>
		<td><input class="input" name="openvpn_port" maxlength="5" value="$OPENVPN_PORT"></td>
		</tr><tr>
		<td nowrap>Remote IP Address *</td>
		<td><input class="input" name="openvpn_remote_ipaddr" value="$OPENVPN_REMOTE_IPADDR"></td>
	      </tr>
	      <tr>
		<td nowrap>Remote Subnet *</td>
		<td><input class="input" name="openvpn_remote_network" value="$OPENVPN_REMOTE_NETWORK"></td>
		</tr><tr>
		<td nowrap>Remote Subnet Mask *</td>
		<td><input class="input" name="openvpn_remote_netmask" value="$OPENVPN_REMOTE_NETMASK"></td>
	      </tr>
	      <tr>
		<td nowrap>Redirect Gateway</td>
		<td><select class="input" name="openvpn_redirect_gw"><option value="0">no<option value="1" $redirect_gw>yes</select></td>
		</tr><tr>
        <td nowrap>NAT Rules</td>
        <td><select class="input" name="openvpn_nat"><option value="0" $nat0>not applied<option value="1" $nat1>applied</select></td>
        </tr><tr>
		<td nowrap id="local_if">Local Interface IP Address</td>
		<td><input class="input" name="openvpn_local_if_ipaddr" value="$OPENVPN_LOCAL_IF_IPADDR"></td>
	      </tr>
	      <tr>
		<td nowrap id="remote_if">Remote Interface IP Address</td>
		<td><input class="input" name="openvpn_remote_if_ipaddr" value="$OPENVPN_REMOTE_IF_IPADDR"></td>
		</tr>
        <tr>
        <td nowrap>Authenticate Mode</td>
        <td><select class="input" name="openvpn_auth" onChange="AuthChanged()">
            <option value="none" $auth_none>Tunnel: none
            <option value="secret" $auth_secret>Tunnel: pre-shared secret
            <option value="tls-client" $auth_tlsc>Tunnel: X.509 certificate (client)
            <option value="tls-server" $auth_tlss>Tunnel: X.509 certificate (server)
            <option value="passwd" $auth_passwd>Client: username / password
            <option value="tls-mclient" $auth_tlsm>Client: X.509 certificate
        </select></td>
          </tr>
        <tr>
        <td nowrap>Compression</td>
        <td><select class="input" name="openvpn_comp"><option value="none" $comp_none>none<option value="lzo" $comp_lzo>LZO</select></td>
        </tr>
</table>
        </td><td width="20">&nbsp;</td><td>
<table>
        <tr>
        <td nowrap>Keepalive Interval *</td>
        <td><input class="input" name="openvpn_ping_intvl" value="$OPENVPN_PING_INTVL"> sec</td>
          </tr>
          <tr>
        <td nowrap>Keepalive Timeout *</td>
        <td><input class="input" name="openvpn_ping_tout" value="$OPENVPN_PING_TOUT"> sec</td>
        </tr>
		<tr><td nowrap id="reneg_sec">Renegotiate Interval *</td>
		<td><input class="input" name="openvpn_reneg_sec" value="$OPENVPN_RENEG_SEC"> sec</td></tr>
	      <tr>
		<td nowrap id="hand_window">Handshake Window *</td>
		<td><input class="input" name="openvpn_hand_window" value="$OPENVPN_HAND_WINDOW"> sec</td>
		</tr><tr>
		<td nowrap id="hand_window">Inactivity Timeout *</td>
		<td><input class="input" name="openvpn_inactive" value="$OPENVPN_INACTIVE"> sec</td>
	      </tr>
	      <tr>
		<td nowrap>Max Fragment Size *</td>
		<td><input class="input" name="openvpn_fragment" value="$OPENVPN_FRAGMENT"> bytes</td>
		</tr>
          <tr>
        <td nowrap id="username">Username</td>
        <td><input class="input" name="openvpn_username" value="$OPENVPN_USERNAME"></td>
        </tr><tr>
		<td nowrap id="password">Password</td>
        <td><input class="input" name="openvpn_password" value="$OPENVPN_PASSWORD"></td>
          </tr>
        <tr><td nowrap>Ping IP Address</td>
        <td><input class="input" name="openvpn_ping2_ip" value="$OPENVPN_PING2_IP"></td></tr>
        <tr><td nowrap>Ping Interval</td>
        <td><input class="input" name="openvpn_ping2_int" value="$OPENVPN_PING2_INT"> min</td></tr>
        <tr><td nowrap>Allow failures</td>
        <td><input class="input" name="openvpn_ping2_allow" value="$OPENVPN_PING2_ALLOW"></td></tr>
</table>
	</td>
	</tr>
		</table><br>
		<table>
	      <tr>
		<td nowrap id="secret">Pre-shared Secret</td>
		<td nowrap>
<textarea cols="80" rows="4" name="openvpn_secret">
EOF
echo "$OPENVPN_SECRET" | base64 -d 
cat << EOF
</textarea>
		</td>
	      </tr>
	      <tr>
		<td nowrap id="ca_cert">CA Certificate</td>
		<td nowrap>
<textarea cols="80" rows="4" name="openvpn_ca_cert">
EOF
echo -n "$OPENVPN_CA_CERT" | base64 -d
cat << EOF
</textarea>
		</td>
	      </tr>
	      <tr>
		<td nowrap id="dh_params">DH Parameters</td>
		<td nowrap>
<textarea cols="80" rows="4" name="openvpn_dh_params">
EOF
echo -n "$OPENVPN_DH_PARAMS" | base64 -d
cat << EOF
</textarea>
		</td>
	      </tr>
	      <tr>
		<td nowrap id="local_cert">Local Certificate</td>
		<td nowrap>
<textarea cols="80" rows="4" name="openvpn_local_cert">
EOF
echo -n "$OPENVPN_LOCAL_CERT" |base64 -d
cat << EOF
</textarea>
		</td>
	      </tr>
	      <tr>
		<td nowrap id="local_key">Local Private Key</td>
		<td nowrap>
<textarea cols="80" rows="4" name="openvpn_local_key">
EOF
echo -n "$OPENVPN_LOCAL_KEY" |base64 -d
cat << EOF
</textarea>
		</td>
	      </tr>
          <tr>
        <td nowrap id="config_file">Configuration File</td>
        <td nowrap>
<textarea cols="80" rows="5" name="openvpn_config_file">
EOF
echo -n "$OPENVPN_CONFIG_FILE" |base64 -d
cat << EOF
</textarea>
        </td>
          </tr>

	      <tr>
		<td nowrap>* <i>can be blank</i></td>
	      </tr>
	    </table>
<!-- outer table with separation -->
	  </td>
	</tr>
	<tr>
	  <td><input type="submit" name="apply" value="Apply"></td>
	</tr>
      </table>
      </form>
      <script language="JavaScript" type="text/javascript">
      <!--
      document.input.openvpn_enabled.focus();
      devChanged();
      ProtoChanged();
      AuthChanged();
      //-->
      </script>

EOF

cat include/end.inc
