#!/bin/sh

[ -e /mnt/rwfs/settings/settings.eth ] && . /mnt/rwfs/settings/settings.eth

./begin $0 $0
echo "</td><td colspan=\"3\" valign=\"top\">"

cat << EOF
      <table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
	  <td class="title" align="center"><b>DHCP Status</b></td>
	</tr>
	<tr>
	  <td>
	    <table width="100%">
	      <tr>
		<td>
<center>
<textarea readonly="yes" rows="25" cols="110" id="leases">
EOF
LEASES=/var/lib/dhcp/dhcpd.leases
if [ "$ETH_DHCP_ENABLED" = "1" ]; then
	lines=`cat $LEASES |wc -l`
	if [ $(($lines)) -lt $((5)) ]; then
        	echo  "No active DHCP leases"
	else
		cat $LEASES |grep -v \#
	fi
else
    echo "DHCP server is disabled"
fi

cat << EOF
</textarea>
</center>
		</td>
	      </tr>
		  <tr>
		<td>
		 <i>All time marks in this file are in UTC (GMT), not your local timezone.</i><br>
		 <i>Static leases are not shown.</i><br>
		</td>
		  </tr>
	    </table>
	  </td>
	</tr>
    <tr><td>
        <input type="button" name="refresh" value="Refresh" onclick="javascript:document.location.reload();">
    </td></tr>
      </table>
EOF

cat include/end.inc

