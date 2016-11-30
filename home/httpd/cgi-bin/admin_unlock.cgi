#!/bin/sh

./begin $0

echo "</td><td colspan=\"3\" valign=\"top\">"
cat include/js.inc

cat << EOF
      function CheckForm() {

	var l1=GetValue(document.input.sim_pin).length;
	if ((l1 < 1) || (l1 > 15)) {
       	alert("Invalid SIM PIN");
  		document.input.sim_pin.focus();
  		return false;
	}

	return true;
      }
      //-->
      </script>
      <form name="input" onsubmit="return CheckForm();" action="admin_unlock_set.cgi" method="post">
      <table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
	  <td class="title" align="center">
	    <b>Disable PIN</b>
	  </td>
	</tr>
	<tr>
	  <td>
	    <table>
	      <tr>
		<td>SIM card: </td>
		<td>
              <select name="simcard">
              <option value="1" >SIM 1</option>
              <option value="2" >SIM 2</option>
              </select>
		</td>
		  </tr>
		  <tr>
        <td>SIM PIN: </td>
        <td><input name="sim_pin" maxlength="15"></td>
		  </tr>
	    </table>
	  </td>
	</tr>
	<tr>
	  <td nowrap>
	  	<input type="submit" name="unlock" value="Disable PIN on selected SIM card">
	  </td>
	</tr>
      </table>
      </form>
      <script language="JavaScript" type="text/javascript">
      <!--
      document.input.sim_pin.focus();
      //-->
      </script>
EOF

cat include/end.inc

