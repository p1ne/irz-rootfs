#!/bin/sh

./begin $0
ifconfig eth0|grep -q UP ; ret=$?

if [ "$ret" = "0" ]; then
    CHECKED="checked"
fi
echo "</td><td colspan=\"3\" valign=\"top\">"
cat << EOF
      <form action="manageeth_set.cgi" method="post">
      <table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
	  <td class="title" align="center">
	    <b>Manage Ethernet</b>
	  </td>
	</tr>
	<tr>
	  <td><input type="checkbox" name="eth_enable" $CHECKED>&nbsp;Enable Ethernet interface.</td>
	</tr>
	<tr>
	  <td><input type="submit" name="apply" value="Apply"></td>
	</tr>
      </table>
      </form>
EOF

cat include/end.inc

