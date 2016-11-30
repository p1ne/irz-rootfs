#!/bin/sh

[ -e /mnt/rwfs/settings/settings.ipsec ] && . /mnt/rwfs/settings/settings.ipsec

./begin $0 $0

echo "</td><td colspan=\"3\" valign=\"top\">"

cat << EOF
      <table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
	  <td class="title" align="center">
	    <b>IPSec Status</b>
	  </td>
	</tr>
	<tr>
	  <td>
	    <table width="100%">
	      <tr>
		<td>
<center>
<textarea readonly="yes" rows="35" cols="110" id="ipsec_status">
EOF

if [ ! "$IPSEC1_ENABLED" = "1" ] && [ ! "$IPSEC2_ENABLED" = "1" ] && [ ! "$IPSEC3_ENABLED" = "1" ] && \
[ ! "$IPSEC4_ENABLED" = "1" ] && [ ! "$IPSEC5_ENABLED" = "1" ]; then
	echo "IPsec is disabled."
else
    cat /var/log/racoon.log
fi


cat << EOF
</textarea>
</center>
<script language="javascript">
textareaelem = document.getElementById('ipsec_status');
textareaelem.scrollTop = textareaelem.scrollHeight;
</script>
<script language="javascript">
    function OnSubmitClear(frm){
        frm.action="status_ipsec_clear.cgi";
        frm.submit();
    }
    function OnSubmitSave(frm){
        frm.action="status_ipsec_save.cgi";
        frm.submit();
    }
</script>
		</td>
	      </tr>
	    </table>
	  </td>
	</tr>
    <tr>
    <td><form name="input" action="status_ipsec_save.cgi" method="post">
    <input type="button" name="refresh" value="Refresh" onclick="javascript:document.location.reload();">
    <input type="submit" name="savelog" value="Save Log">
    <input type="submit" name="ipsec_clear" value="Clear Log" onclick="OnSubmitClear(this.form);">
    </form></td>
    </tr>
      </table>
EOF

cat include/end.inc

