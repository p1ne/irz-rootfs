#!/bin/sh
[ -x /mnt/rwfs/settings/ipup ] && ENABLED="checked"

./begin $0

echo "</td><td colspan=\"3\" valign=\"top\">"

cat << EOF
    <form name="input" action="admin_ipup_set.cgi" method="POST">
      <table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
	  <td class="title" align="center">
	    <b>IP-Up Script</b>
	  </td>
	</tr>
	<tr>
	  <td>
		<center>
		<table width="100%" border="0"><tr><td>
		<input type="checkbox" name="script_enabled" $ENABLED>&nbsp; Run script when connected
		</td></tr><tr><td>
		<textarea rows="30" cols="110" name="upscript">
EOF

if [ -e "/mnt/rwfs/settings/ipup" ]; then
    cat /mnt/rwfs/settings/ipup
else
    echo "#!/bin/sh"
	echo "## This script will be executed when Internet is connected"
fi
cat << EOF
</textarea>
		</td></tr></table>
        </center>
	  </td>
	</tr>
	<tr>
	  <td>
	  <input type="submit" name="saveipup" value="Save Script">
	  </td>
	</tr>
    </table>
</form>
    <script language="JavaScript" type="text/javascript">
       <!--
       document.input.upscript.focus();
       //-->
    </script>
EOF

cat include/end.inc

