#!/bin/sh

[ -e /mnt/rwfs/settings/settings.gre ] && . /mnt/rwfs/settings/settings.gre

[ "$GRE01_ENABLED" = "1" ] && selected01="selected"
[ "$GRE02_ENABLED" = "1" ] && selected02="selected"
[ "$GRE03_ENABLED" = "1" ] && selected03="selected"
[ "$GRE04_ENABLED" = "1" ] && selected04="selected"
[ "$GRE05_ENABLED" = "1" ] && selected05="selected"
[ "$GRE06_ENABLED" = "1" ] && selected06="selected"
[ "$GRE07_ENABLED" = "1" ] && selected07="selected"
[ "$GRE08_ENABLED" = "1" ] && selected08="selected"
[ "$GRE09_ENABLED" = "1" ] && selected09="selected"
[ "$GRE10_ENABLED" = "1" ] && selected10="selected"

GRE01_DESC=`decode $GRE01_DESC`
GRE02_DESC=`decode $GRE02_DESC`
GRE03_DESC=`decode $GRE03_DESC`
GRE04_DESC=`decode $GRE04_DESC`
GRE05_DESC=`decode $GRE05_DESC`
GRE06_DESC=`decode $GRE06_DESC`
GRE07_DESC=`decode $GRE07_DESC`
GRE08_DESC=`decode $GRE08_DESC`
GRE09_DESC=`decode $GRE09_DESC`
GRE10_DESC=`decode $GRE10_DESC`


./begin $0

echo "</td><td colspan=\"3\" valign=\"top\">"

cat << EOF
      <form name="input" onsubmit="return CheckForm();" action="config_gre_set.cgi" method="post">
      <table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
	  <td class="title" align="center"><b>GRE Tunnel Configuration</b></td>
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
			<th>&nbsp;</th>
		  </tr>
		  <tr>
			<td align="right">1.</td>
			<td><select name="gre01_enabled"><option value="">no</option><option value="on" $selected01>yes</option></select></td>
			<td><input name="gre01_description" value="$GRE01_DESC" readonly></td>
			<td><input name="gre01_remote_ipaddr" size="15" value="$GRE01_REMOTE_IPADDR" readonly></td>
			<td><input name="gre01_remote_network" size="15" value="$GRE01_REMOTE_NETWORK" readonly></td>
			<td><a href="config_gren.cgi?tun=01"><b>[ Edit ]</b></a></td>
		  </tr>
          <tr>
            <td align="right">2.</td>
            <td><select name="gre02_enabled"><option value="">no</option><option value="on" $selected02>yes</option></select></td>
            <td><input name="gre02_description" value="$GRE02_DESC" readonly></td>
            <td><input name="gre02_remote_ipaddr" size="15" value="$GRE02_REMOTE_IPADDR" readonly></td>
            <td><input name="gre02_remote_network" size="15" value="$GRE02_REMOTE_NETWORK" readonly></td>
            <td><a href="config_gren.cgi?tun=02"><b>[ Edit ]</b></a></td>
          </tr>
          <tr>
            <td align="right">3.</td>
            <td><select name="gre03_enabled"><option value="">no</option><option value="on" $selected03>yes</option></select></td>
            <td><input name="gre03_description" value="$GRE03_DESC" readonly></td>
            <td><input name="gre03_remote_ipaddr" size="15" value="$GRE03_REMOTE_IPADDR" readonly></td>
            <td><input name="gre03_remote_network" size="15" value="$GRE03_REMOTE_NETWORK" readonly></td>
            <td><a href="config_gren.cgi?tun=03"><b>[ Edit ]</b></a></td>
          </tr>
          <tr>
            <td align="right">4.</td>
            <td><select name="gre04_enabled"><option value="">no</option><option value="on" $selected04>yes</option></select></td>
            <td><input name="gre04_description" value="$GRE04_DESC" readonly></td>
            <td><input name="gre04_remote_ipaddr" size="15" value="$GRE04_REMOTE_IPADDR" readonly></td>
            <td><input name="gre04_remote_network" size="15" value="$GRE04_REMOTE_NETWORK" readonly></td>
            <td><a href="config_gren.cgi?tun=04"><b>[ Edit ]</b></a></td>
          </tr>
          <tr>
            <td align="right">5.</td>
            <td><select name="gre05_enabled"><option value="">no</option><option value="on" $selected05>yes</option></select></td>
            <td><input name="gre05_description" value="$GRE05_DESC" readonly></td>
            <td><input name="gre05_remote_ipaddr" size="15" value="$GRE05_REMOTE_IPADDR" readonly></td>
            <td><input name="gre05_remote_network" size="15" value="$GRE05_REMOTE_NETWORK" readonly></td>
            <td><a href="config_gren.cgi?tun=05"><b>[ Edit ]</b></a></td>
          </tr>
          <tr>
            <td align="right">6.</td>
            <td><select name="gre06_enabled"><option value="">no</option><option value="on" $selected06>yes</option></select></td>
            <td><input name="gre06_description" value="$GRE06_DESC" readonly></td>
            <td><input name="gre06_remote_ipaddr" size="15" value="$GRE06_REMOTE_IPADDR" readonly></td>
            <td><input name="gre06_remote_network" size="15" value="$GRE06_REMOTE_NETWORK" readonly></td>
            <td><a href="config_gren.cgi?tun=06"><b>[ Edit ]</b></a></td>
          </tr>
          <tr>
            <td align="right">7.</td>
            <td><select name="gre07_enabled"><option value="">no</option><option value="on" $selected07>yes</option></select></td>
            <td><input name="gre07_description" value="$GRE07_DESC" readonly></td>
            <td><input name="gre07_remote_ipaddr" size="15" value="$GRE07_REMOTE_IPADDR" readonly></td>
            <td><input name="gre07_remote_network" size="15" value="$GRE07_REMOTE_NETWORK" readonly></td>
            <td><a href="config_gren.cgi?tun=07"><b>[ Edit ]</b></a></td>
          </tr>
          <tr>
            <td align="right">8.</td>
            <td><select name="gre08_enabled"><option value="">no</option><option value="on" $selected08>yes</option></select></td>
            <td><input name="gre08_description" value="$GRE08_DESC" readonly></td>
            <td><input name="gre08_remote_ipaddr" size="15" value="$GRE08_REMOTE_IPADDR" readonly></td>
            <td><input name="gre08_remote_network" size="15" value="$GRE08_REMOTE_NETWORK" readonly></td>
            <td><a href="config_gren.cgi?tun=08"><b>[ Edit ]</b></a></td>
          </tr>
          <tr>
            <td align="right">9.</td>
            <td><select name="gre09_enabled"><option value="">no</option><option value="on" $selected09>yes</option></select></td>
            <td><input name="gre09_description" value="$GRE09_DESC" readonly></td>
            <td><input name="gre09_remote_ipaddr" size="15" value="$GRE09_REMOTE_IPADDR" readonly></td>
            <td><input name="gre09_remote_network" size="15" value="$GRE09_REMOTE_NETWORK" readonly></td>
            <td><a href="config_gren.cgi?tun=09"><b>[ Edit ]</b></a></td>
          </tr>
          <tr>
            <td align="right">10.</td>
            <td><select name="gre10_enabled"><option value="">no</option><option value="on" $selected10>yes</option></select></td>
            <td><input name="gre10_description" value="$GRE10_DESC" readonly></td>
            <td><input name="gre10_remote_ipaddr" size="15" value="$GRE10_REMOTE_IPADDR" readonly></td>
            <td><input name="gre10_remote_network" size="15" value="$GRE10_REMOTE_NETWORK" readonly></td>
            <td><a href="config_gren.cgi?tun=10"><b>[ Edit ]</b></a></td>
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

