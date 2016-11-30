#!/bin/sh

./begin $0 $0

echo "</td><td colspan=\"3\" valign=\"top\">"

cat << EOF
      <table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
	  <td class="title" align="center">
	    <b>OpenVPN Server Log</b>
	  </td>
	</tr>
	<tr>
	  <td>
	    <table width="100%">
	    <tr>
		<td>
<center>
<textarea readonly="yes" rows="30" cols="110" id="ovpn-serv">
EOF

if [ -e /var/log/ovpn-serv.log ]; then
    cat /var/log/ovpn-serv.log
else
    echo "OpenVPN Server is stopped"
fi

cat << EOF
</textarea>
</center>
<script language="javascript">
textareaelem = document.getElementById('ovpn-serv');
textareaelem.scrollTop = textareaelem.scrollHeight;
</script>
<script language="javascript">
    function OnSubmitClear(frm){
        frm.action="status_ovpnserv_clear.cgi";
        frm.submit();
    }
    function OnSubmitSave(frm){
        frm.action="status_ovpnserv_save.cgi";
        frm.submit();
    }
</script>

		</td>
	      </tr>
	    </table>
	  </td>
	</tr>
	<tr>
	<td><form name="input" action="status_ovpnserv_save.cgi" method="post">
	<input type="button" name="refresh" value="Refresh" onclick="javascript:document.location.reload();">
	<input type="submit" name="ovpns_save" value="Save Log">
    <input type="submit" name="ovpns_clear" value="Clear Log" onclick="OnSubmitClear(this.form);">
	</form></td>
	</tr>
      </table>
      
EOF

cat include/end.inc

