#!/bin/sh

./begin $0 $0

echo "</td><td colspan=\"3\" valign=\"top\">"

cat << EOF
      <table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
	  <td class="title" align="center">
	    <b>System Log</b>
	  </td>
	</tr>
	<tr>
	  <td>
	    <table width="100%">
	      <tr>
		<td>
<center>
<textarea readonly="yes" rows="30" cols="110" wrap="off" id="syslog">
EOF
if [ -e "/mnt/usb/messages" ]; then
    tail -n 1000 /mnt/usb/messages
else
    cat /var/log/messages|tail -n 1000
fi

cat << EOF
</textarea>
</center>
<script language="javascript">
textareaelem = document.getElementById('syslog');
textareaelem.scrollTop = textareaelem.scrollHeight;
</script>
		</td>
	      </tr>
	    </table>
	  </td>
	</tr>
	<tr>
	<td><form name="input" action="status_syslog_save.cgi" method="post">
	<input type="button" name="refresh" value="Refresh" onclick="javascript:document.location.reload();">
	<input type="submit" name="savelog" value="Save Log">
	</form></td>
	</tr>
      </table>
      
EOF

cat include/end.inc

