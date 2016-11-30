#!/bin/sh

./begin $0

echo "</td><td colspan=\"3\" valign=\"top\">"
cat << EOF
      <form action="admin_reboot_exec.cgi" method="post">
      <table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
	  <td class="title" align="center">
	    <b>Reboot</b>
	  </td>
	</tr>
	<tr>
	  <td><input type="checkbox" name="reboot_defaults">Reset configuration to defaults<br><br>
	  The reboot process will take about 60 seconds to complete.</td>
	</tr>
	<tr>
	  <td><input type="submit" name="reboot" value="Reboot"></td>
	</tr>
      </table>
      </form>
EOF

cat include/end.inc

