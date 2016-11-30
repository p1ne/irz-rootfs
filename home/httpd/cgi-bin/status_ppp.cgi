#!/bin/sh

./begin $0 $0

echo "</td><td colspan=\"3\" valign=\"top\">"

cat << EOF
      <table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
	  <td class="title" align="center">
	    <b>Internet Status</b>
	  </td>
	</tr>
	<tr>
	  <td>
	    <table width="100%">
	      <tr align="center">
		<td class="menu">Actual GSM Info</td>
	      </tr>
	      <tr>
		<td>
<table width="100%">
<tr><td valign="top"><table cellspacing="5">
EOF
gsminfo | sed -e 's|^|<tr><td>|g' | sed -e 's|: |:</td><td>|g' | sed -e 's|$|</td></tr>|g'
cat << EOF
</table></td><td valign="top"><table cellspacing="5">
EOF
pppinfo | sed -e 's|^|<tr><td>|g' | sed -e 's|: |:</td><td>|g' | sed -e 's|$|</td></tr>|g'
cat << EOF
</table></td></tr></table>
		</td>
	      </tr>
	      <tr align="center">
		<td class="menu">Connection Log</td>
	      </tr>
	      <tr>
		<td>
<center>
<textarea rows="20" cols="110" id="connection" readonly>
EOF

if [ -s /mnt/rwfs/settings/connection.log ]; then
	cat /mnt/rwfs/settings/connection.log
else
	echo "Log is empty."
fi

cat << EOF

</textarea>
</center>
<script language="javascript">
textareaelem = document.getElementById('connection');
textareaelem.scrollTop = textareaelem.scrollHeight;
</script>
<script language="javascript">
    function OnSubmitClear(frm){
	frm.action="status_ppp_clear.cgi"
	frm.submit();
    }
    
    function OnSubmitSave(frm){
	frm.action="status_ppp_save.cgi"
	frm.submit();
    }
</script>
		</td>
	      </tr>
	    </table>
	  </td>
	</tr>
	<tr>
	  <td>
		 <form name="input" action="status_ppp_save.cgi" method="post">
		 <input type="button" name="refresh" value="Refresh" onclick="javascript:document.location.reload();">
		 <input type="button" name="Save log" value="Save log" onclick="OnSubmitSave(this.form);">
		 <input type="button" name="clear" value="Clear Log" onclick="OnSubmitClear(this.form);">
		</form>
	  </td>
	</tr>
      </table>
EOF

cat include/end.inc

