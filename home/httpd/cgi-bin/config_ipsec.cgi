#!/bin/sh

[ -e /mnt/rwfs/settings/settings.ipsec ] && . /mnt/rwfs/settings/settings.ipsec

[ "$IPSEC1_ENABLED" = "1" ] && selected01="selected"
[ "$IPSEC2_ENABLED" = "1" ] && selected02="selected"
[ "$IPSEC3_ENABLED" = "1" ] && selected03="selected"
[ "$IPSEC4_ENABLED" = "1" ] && selected04="selected"
[ "$IPSEC5_ENABLED" = "1" ] && selected05="selected"
IPSEC1_DESC=`decode $IPSEC1_DESC`
IPSEC2_DESC=`decode $IPSEC2_DESC`
IPSEC3_DESC=`decode $IPSEC3_DESC`
IPSEC4_DESC=`decode $IPSEC4_DESC`
IPSEC5_DESC=`decode $IPSEC5_DESC`

./begin $0

echo "</td><td colspan=\"3\" valign=\"top\">"

cat << EOF
      <form name="input" onsubmit="return CheckForm();" action="config_ipsec_set.cgi" method="post">
      <table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
	  <td class="title" align="center"><b>IPSEC Tunnel Configuration</b></td>
	</tr>        
	<tr>
	  <td>
		<table cellspacing="5">
                    <tr>
			<th>#</th>
			<th>Create</th>
			<th>Description</th>
			<th>Remote IP Address</th>
			<th>Remote Subnet</th>
			<th>Remote Netmask</th>
			<th>&nbsp;</th>
                    </tr>
                    <tr>
			<td>1.</td>
			<td><select name="ipsec1_enabled"><option value="">no</option><option value="on" $selected01>yes</option></select></td>
			<td><input name="ipsec1_desc" size="20" value="$IPSEC1_DESC" readonly></td>
			<td><input name="ipsec1_remote_ipaddr" size="15" value="$IPSEC1_REMOTE_IPADDR" readonly></td>
			<td><input name="ipsec1_remote_network" size="15" value="$IPSEC1_REMOTE_NETWORK" readonly></td>
			<td><input name="ipsec1_remote_netmask" size="15" value="$IPSEC1_REMOTE_NETMASK" readonly></td>
			<td><a href="config_ipsecn.cgi?tun=1"><b>[ Edit ]</b></a></td>
                    </tr>
                    <tr>
			<td>2.</td>
			<td><select name="ipsec2_enabled"><option value="">no</option><option value="on" $selected02>yes</option></select></td>
			<td><input name="ipsec2_desc" size="20" value="$IPSEC2_DESC" readonly></td>
			<td><input name="ipsec2_remote_ipaddr" size="15" value="$IPSEC2_REMOTE_IPADDR" readonly></td>
			<td><input name="ipsec2_remote_network" size="15" value="$IPSEC2_REMOTE_NETWORK" readonly></td>
			<td><input name="ipsec2_remote_netmask" size="15" value="$IPSEC2_REMOTE_NETMASK" readonly></td>
			<td><a href="config_ipsecn.cgi?tun=2"><b>[ Edit ]</b></a></td>
                    </tr>
                    <tr>
			<td>3.</td>
			<td><select name="ipsec3_enabled"><option value="">no</option><option value="on" $selected03>yes</option></select></td>
            <td><input name="ipsec3_desc" size="20" value="$IPSEC3_DESC" readonly></td>
			<td><input name="ipsec3_remote_ipaddr" size="15" value="$IPSEC3_REMOTE_IPADDR" readonly></td>
			<td><input name="ipsec3_remote_network" size="15" value="$IPSEC3_REMOTE_NETWORK" readonly></td>
			<td><input name="ipsec3_remote_netmask" size="15" value="$IPSEC3_REMOTE_NETMASK" readonly></td>
			<td><a href="config_ipsecn.cgi?tun=3"><b>[ Edit ]</b></a></td>
                    </tr>
                    <tr>
			<td>4.</td>
			<td><select name="ipsec4_enabled"><option value="">no</option><option value="on" $selected04>yes</option></select></td>
            <td><input name="ipsec4_desc" size="20" value="$IPSEC4_DESC" readonly></td>	
			<td><input name="ipsec4_remote_ipaddr" size="15" value="$IPSEC4_REMOTE_IPADDR" readonly></td>
			<td><input name="ipsec4_remote_network" size="15" value="$IPSEC4_REMOTE_NETWORK" readonly></td>
			<td><input name="ipsec4_remote_netmask" size="15" value="$IPSEC4_REMOTE_NETMASK" readonly></td>
			<td><a href="config_ipsecn.cgi?tun=4"><b>[ Edit ]</b></a></td>
                    </tr>
                    <tr>
			<td>5</td>
			<td><select name="ipsec5_enabled"><option value="">no</option><option value="on" $selected05>yes</option></select></td>
            <td><input name="ipsec5_desc" size="20" value="$IPSEC5_DESC" readonly></td>	
			<td><input name="ipsec5_remote_ipaddr" size="15" value="$IPSEC5_REMOTE_IPADDR" readonly></td>
			<td><input name="ipsec5_remote_network" size="15" value="$IPSEC5_REMOTE_NETWORK" readonly></td>
			<td><input name="ipsec5_remote_netmask" size="15" value="$IPSEC5_REMOTE_NETMASK" readonly></td>
			<td><a href="config_ipsecn.cgi?tun=5"><b>[ Edit ]</b></a></td>
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

