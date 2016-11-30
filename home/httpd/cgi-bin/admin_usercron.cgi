#!/bin/sh
[ -x /mnt/rwfs/settings/usercron ] && ENABLED="checked"

./begin $0

echo "</td><td colspan=\"3\" valign=\"top\">"

cat << EOF
    <form name="input" action="admin_usercron_set.cgi" method="POST">
      <table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
	  <td class="title" align="center">
	    <b>User Crontab</b>
	  </td>
	</tr>
	<tr>
	  <td>
		<center>
		<table width="100%" border="0"><tr><td>
		<input type="checkbox" name="usercron_enabled" $ENABLED>&nbsp; Enable user crontab
		</td></tr><tr><td>
		<textarea rows="30" cols="110" name="usercron">
EOF

if [ -e "/mnt/rwfs/settings/usercron" ]; then
    cat /mnt/rwfs/settings/usercron
else
	echo "## MM HH DoM MON DoW Command"
fi
cat << EOF
</textarea>
		</td></tr></table>
    </center>
	  </td>
	</tr>
	<tr>
	  <td>
	  <input type="submit" name="saveuser" value="Save crontab">
	  </td>
	</tr>
    </table>
</form>
    <script language="JavaScript" type="text/javascript">
       <!--
       document.input.usercron.focus();
       //-->
    </script>
EOF

cat include/end.inc

