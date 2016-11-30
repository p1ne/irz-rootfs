#!/bin/sh

./begin $0

echo "</td><td colspan=\"3\" valign=\"top\">"
cat << EOF
<script language="JavaScript" type="text/javascript">
<!--
      function Focus(obj) {
     obj.focus(); obj.select();
       }
      function CheckForm() {
	var a = document.input.ping_address.value;
	var c = document.input.ping_count.value;
	if (a.length < 3) {
	  alert("Bad IP/URL number");
	  Focus(document.input.ping_address);
	  return false;
	}
	if ( (c.length == 0) || (parseInt(c, 10) < 5) || (parseInt(c, 10) > 100)) {
	  alert("Ping count must be 5 to 100");
	  Focus(document.input.ping_count);
	  return false;
	}
	return true;
      }
      //-->
      </script>
      <form name="input" onsubmit="return CheckForm();" action="admin_pingtest_set.cgi" method="post">
      <table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
	  <td class="title" align="center">
	    <b>Ping Test</b>
	  </td>
	</tr>
	<tr>
	  <td>
	    <table>
	      <tr>
		<td>Ping Address/URL:&nbsp;</td>
		<td><input name="ping_address"></td>
		<td>&nbsp;&nbsp;</td>
		<td>Count:&nbsp;</td>
		<td><input name="ping_count" maxlength="3" size="3" value="10" ></td>
        <td>&nbsp;&nbsp;</td>
		<td>Datagram size:&nbsp;</td>
		<td><input name="ping_size" maxlength="4" size="4" value="56" ></td>
	      </tr>
	    </table>
	  </td>
	</tr>
	<tr>
	  <td><input type="submit" name="apply" value="Ping"></td>
	</tr>
      </table>
      </form>
      <script language="JavaScript" type="text/javascript">
      <!--
      document.input.ping_address.focus();
      //-->
      </script>
EOF

cat include/end.inc

