#!/bin/sh

#[ -e /mnt/rwfs/settings/settings.ovpns ] && . /mnt/rwfs/settings/settings.ovpns

tun=`echo "$QUERY_STRING" | sed -n 's/^.*tun=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
## GRE example
OVPN_ENABLED=`cat /mnt/rwfs/settings/settings.ovpns | grep "OVPN${tun}_ENABLED" | sed -e 's/^.*=//'`
OVPN_BASE64=`cat /mnt/rwfs/settings/settings.ovpns | grep "OVPN${tun}_DESC" | sed -e 's/^.*DESC=//'`
OVPN_DESC=`decode $OVPN_BASE64`
OVPN_BASE64=`cat /mnt/rwfs/settings/settings.ovpns | grep "OVPN${tun}_NAME" | sed -e 's/^.*NAME=//'`
OVPN_NAME=`decode $OVPN_BASE64`
OVPN_BASE64=`cat /mnt/rwfs/settings/settings.ovpns | grep "OVPN${tun}_CONFIG" | sed -e 's/^.*CONFIG=//'`
OVPN_CONFIG=`decode $OVPN_BASE64`

[ "$OVPN_ENABLED" = "1" ] && CHECKED="checked"

./begin $0

echo "</td><td colspan=\"3\" valign=\"top\">"
cat include/js.inc

cat << EOF
      function CheckForm() {
    var ovpn_enabled = document.input.ovpn_enabled.checked;
	return true;
      }
      //-->
      </script>
      <form name="input" onsubmit="return CheckForm();" action="config_ovpnservn_set.cgi" method="post">
      <table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
	  <td class="title" align="center">
	    <b>OpenVPN Client Configuration</b>
	  </td>
	</tr>
	<tr>
	  <td>
	    <table>
	      <tr>
		<td><input type="checkbox" name="ovpn_enabled" $CHECKED></td>
		<td nowrap>Enable client #<input name="ovpn_num" value="$tun" size="2" readonly></td>
	      </tr>
	    </table>
	    <table>
		  <tr>
 		<td nowrap>Description *</td>
		<td><input name="ovpn_desc" maxlength="20" value="$OVPN_DESC"></td>
		  </tr>
	      <tr>
		<td nowrap>Client Name</td>
		<td><input name="ovpn_name" maxlength="20" value="$OVPN_NAME"></td>
	      </tr>
	      <tr>
		<td nowrap class="td1">Configuration</td>
		<td><textarea cols="65" rows="10" name="ovpn_config">$OVPN_CONFIG</textarea></td>
	      </tr>
	      <tr>
		<td nowrap>* <i>can be blank</i></td>
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
      document.input.ovpn_enabled.focus();
      //-->
      </script>
EOF

cat include/end.inc

