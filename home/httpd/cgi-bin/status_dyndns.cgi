#!/bin/sh

[ -e /mnt/rwfs/settings/settings.dyndns ] && . /mnt/rwfs/settings/settings.dyndns

./begin $0 $0
echo "</td><td colspan=\"3\" valign=\"top\">"

cat << EOF
      <table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
	  <td class="title" align="center">
	    <b>DynDNS Status</b>
	  </td>
	</tr>
	<tr>
	  <td>
	    <table width="100%">
	      <tr>
		<td>
<textarea readonly="yes" rows="30" cols="110" wrap="off" id="dyndns">
EOF

if [ "$DYNDNS_ENABLED" = "1" ]; then
    if [ -s /var/log/inadyn.log ]; then
	cat /var/log/inadyn.log
    else
	echo "No update performed yet."
    fi
else
    echo "DynDNS client is disabled."
fi

cat << EOF

</textarea>
<script language="javascript">
textareaelem = document.getElementById('dyndns');
textareaelem.scrollTop = textareaelem.scrollHeight;

function OnSubmitClear(frm){
    frm.action="status_dyndns_clear.cgi"
    frm.submit();
}
function OnSubmitSave(frm){
    frm.action="status_dyndns_save.cgi"
    frm.submit();
}
</script>

		</td>
	      </tr>
	    </table>
	  </td>
	</tr>
	<tr><td>
        <form name="input" action="status_dyndns_save.cgi" method="post">
		<input type="button" name="refresh" value="Refresh" onclick="javascript:document.location.reload();">
        <input type="button" name="save" value="Save log" onclick="OnSubmitSave(this.form);">
        <input type="button" name="clear" value="Clear Log" onclick="OnSubmitClear(this.form);">
        </form>
	</td></tr>
      </table>
EOF

cat include/end.inc

