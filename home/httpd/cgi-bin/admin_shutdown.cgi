#!/bin/sh
[ -x /mnt/rwfs/settings/shutdown ] && ENABLED="checked"

./begin $0

echo "</td><td colspan=\"3\" valign=\"top\">"

cat << EOF
<form name="input" action="admin_shutdown_set.cgi" method="POST">
<table width="100%" cellspacing="0" cellpadding="5" border="3">
  <tr>
    <td class="title" align="center"><b>Shutdown Script</b></td>
  </tr>
  <tr>
    <td>
      <center>
        <table width="100%" border="0">
          <tr><td><input type="checkbox" name="script_enabled" $ENABLED>&nbsp; Run script at shutdown</td></tr>
          <tr><td>
<textarea rows="30" cols="110" name="script">
EOF

if [ -e "/mnt/rwfs/settings/shutdown" ]; then
    cat /mnt/rwfs/settings/shutdown
else
    echo "#!/bin/sh"
    echo "## This script will be executed at system shutdown"
fi
cat << EOF
</textarea>
          </td></tr>
        </table>
      </center>
    </td>
  </tr>
  <tr><td><input type="submit" name="saveshutdown" value="Save Script"></td></tr>
</table>
</form>
<script language="JavaScript" type="text/javascript">
<!--
document.input.script.focus();
//-->
</script>
EOF

cat include/end.inc

