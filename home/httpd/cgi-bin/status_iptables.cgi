#!/bin/sh

./begin $0 $0

echo "</td><td colspan=\"3\" valign=\"top\">"

cat << EOF
      <table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
	  <td class="title" align="center">
	    <b>Iptables Status</b>
	  </td>
	</tr>
	<tr>
	  <td>
	    <table width="100%">
	      <tr align="center">
		<td class="menu">Table: filter</td>
	      </tr>
	      <tr>
		<td>
<center>
<textarea readonly="yes" rows="15" cols="110" wrap="off" id="ipt_filter">
EOF
 
iptables -L -t filter -v -n
 
cat << EOF
</textarea>
</center>
		</td>
	      </tr>
	      <tr align="center">
		<td class="menu">Table: nat</td>
	      </tr>
	      <tr>
		<td>
<center>
<textarea readonly="yes" rows="15" cols="110" wrap="off" id="ipt_nat">
EOF

iptables -L -t nat -v -n

cat << EOF
</textarea>
</center>
		</td>
	      </tr>
	    </table>
	  </td>
	</tr>
    <tr><td>
		<form name="input" action="status_iptables_save.cgi" method="post">
        	<input type="button" name="refresh" value="Refresh" onclick="javascript:document.location.reload();">
			<input type="submit" name="saveipt" value="Save Status">
		</form>
    </td></tr>
      </table>
EOF

cat include/end.inc

