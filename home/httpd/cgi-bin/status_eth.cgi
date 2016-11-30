#!/bin/sh

./begin $0 $0

echo "</td><td colspan=\"3\" valign=\"top\">"

cat << EOF
      <table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
	  <td class="title" align="center">
	    <b>Network Status</b>
	  </td>
	</tr>
	<tr>
	  <td>
	    <table width="100%">
	      <tr align="center">
		<td class="menu">Interfaces</td>
	      </tr>
	      <tr>
		<td>
<center>
<textarea readonly="yes" rows="25" cols="110" id="interfaces">
EOF
ifconfig
cat << EOF
</textarea>
</center>
		</td>
	      </tr>
	      <tr align="center">
		<td class="menu">Route Table</td>
	      </tr>
	      <tr>
		<td>
<center>
<textarea readonly="yes" rows="5" cols="110" id="routes">
EOF
route -n | grep -v "127.0.0" | tail -n+2
cat << EOF
</textarea>
</center>
		</td>
	      </tr>
          <tr align="center">
        <td class="menu">Ethernet Link
          </tr>
          <tr>
        <td>
<center>
<textarea readonly="yes" rows="5" cols="110" id="ethernet">
EOF
mii-diag eth0
cat << EOF
</textarea>
</center>
        </td>
          </tr>

	    </table>
	  </td>
	</tr>
    <tr><td>
	<form action="status_eth_save.cgi" >
        <input type="button" name="refresh" value="Refresh" onclick="javascript:document.location.reload();">
        <input type="submit" name="save" value="Save Status" >
        </form>
    </td></tr>
      </table>
EOF

cat include/end.inc

