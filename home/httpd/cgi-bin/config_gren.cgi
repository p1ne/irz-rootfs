#!/bin/sh
#[ -e /mnt/rwfs/settings/settings.gre ] && . /mnt/rwfs/settings/settings.gre

#$QUERY_STRING
tun=`echo "$QUERY_STRING" | sed -n 's/^.*tun=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`

#get all values from file
GREN_ENABLED=`cat /mnt/rwfs/settings/settings.gre | grep "GRE${tun}_ENABLED" | sed -e 's/^.*=//'`
GREN_BASE64=`cat /mnt/rwfs/settings/settings.gre | grep "GRE${tun}_DESC" | sed -e 's/^.*DESC=//'`
GREN_DESC=`decode $GREN_BASE64`
GREN_REMOTE_IPADDR=`cat /mnt/rwfs/settings/settings.gre | grep "GRE${tun}_REMOTE_IPADDR" | sed -e 's/^.*=//'`
GREN_SRC_IPADDR=`cat /mnt/rwfs/settings/settings.gre | grep "GRE${tun}_SRC_IPADDR" | sed -e 's/^.*=//'`
GREN_DST_IPADDR=`cat /mnt/rwfs/settings/settings.gre | grep "GRE${tun}_DST_IPADDR" | sed -e 's/^.*=//'`
GREN_REMOTE_NETWORK=`cat /mnt/rwfs/settings/settings.gre | grep "GRE${tun}_REMOTE_NETWORK" | sed -e 's/^.*=//'`
GREN_REMOTE_NETMASK=`cat /mnt/rwfs/settings/settings.gre | grep "GRE${tun}_REMOTE_NETMASK" | sed -e 's/^.*=//'`
GREN_TUNNEL_MASK=`cat /mnt/rwfs/settings/settings.gre | grep "GRE${tun}_TUNNEL_MASK" | sed -e 's/^.*=//'`
GREN_TUNNEL_MTU=`cat /mnt/rwfs/settings/settings.gre | grep "GRE${tun}_TUNNEL_MTU" | sed -e 's/^.*=//'`

[ "$GREN_ENABLED" = "1" ] && CHECKED="checked"
./begin $0

echo "</td><td colspan=\"3\" valign=\"top\">"
cat include/js.inc

cat << EOF
      function CheckForm() {
	var gre_enabled = document.input.gre_enabled.checked;
	if (!IsValidIP(document.input.gre_remote_ipaddr, !gre_enabled)) {
	  alert("Invalid or missing remote external IP address.");
	  Focus(document.input.gre_remote_ipaddr);
	  return false;
	}
	if (!IsValidIP(document.input.gre_remote_network, !gre_enabled)) {
	  alert("Invalid or missing remote subnet.");
	  Focus(document.input.gre_remote_network);
	  return false;
	}
	if (!IsValidIP(document.input.gre_remote_netmask, !gre_enabled)) {
	  alert("Invalid or missing remote subnet mask.");
	  Focus(document.input.gre_remote_netmask);
	  return false;
	}
	if (!IsValidIP(document.input.gre_src_ipaddr, true)) {
	  alert("Invalid local internal IP address.");
	  Focus(document.input.gre_src_ipaddr);
	  return false;
	}
	if (!IsValidIP(document.input.gre_dst_ipaddr, true)) {
	  alert("Invalid remote internal IP address.");
	  Focus(document.input.gre_dst_ipaddr);
	  return false;
	}
	return true;
      }
      //-->
      </script>
      <form name="input" onsubmit="return CheckForm();" action="config_gren_set.cgi" method="post">
      <table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
	  <td class="title" align="center">
	    <b>GRE Tunnel Configuration</b>
	  </td>
	</tr>
	<tr>
	  <td>
	    <table>
	      <tr>
		<td><input type="checkbox" name="gre_enabled" $CHECKED></td>
		<td nowrap>Create GRE tunnel #<input name="gre_num" value="$tun" size="2" readonly></td>
	      </tr>
	    </table>
	    <table>
		 <tr>
        <td nowrap>Description *</td>
        <td><input name="gre_desc" maxlength="20" value="$GREN_DESC"></td>
          </tr>
	      <tr>
		<td nowrap>Remote External IP Address</td>
		<td><input name="gre_remote_ipaddr" value="$GREN_REMOTE_IPADDR"></td>
	      </tr>
	      <tr>
		<td nowrap>Remote Subnet</td>
		<td><input name="gre_remote_network" value="$GREN_REMOTE_NETWORK"></td>
	      </tr>
	      <tr>
		<td nowrap>Remote Subnet Mask</td>
		<td><input name="gre_remote_netmask" value="$GREN_REMOTE_NETMASK"></td>
	      </tr>
	      <tr>
		<td nowrap>Local Internal IP Address *</td>
		<td><input name="gre_src_ipaddr" value="$GREN_SRC_IPADDR"></td>
	      </tr>
	      <tr>
		<td nowrap>Remote Internal IP Address *</td>
		<td><input name="gre_dst_ipaddr" value="$GREN_DST_IPADDR"></td>
	      </tr>
          <tr>
        <td nowrap>Tunnel Mask *</td>
        <td><input name="gre_tunnel_mask" value="$GREN_TUNNEL_MASK"></td>
          </tr>
          <tr>
        <td nowrap>Tunnel MTU *</td>
        <td><input name="gre_tunnel_mtu" value="$GREN_TUNNEL_MTU"></td>
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
      document.input.gre_enabled.focus();
      //-->
      </script>
EOF

cat include/end.inc

