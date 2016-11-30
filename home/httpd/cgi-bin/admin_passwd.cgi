#!/bin/sh

./begin $0

echo "</td><td colspan=\"3\" valign=\"top\">"
cat include/js.inc
cat << EOF
      function CheckForm() {
	var p1 = GetValue(document.input.new_passwd);
	var p2 = GetValue(document.input.new_passwd2);
	if (((p1.length > 0) && (p1.length < 4)) || ((p2.length > 0) && (p2.length < 4))) {
	  alert("Password is too short.");
	  Focus(document.input.new_passwd);
	  return false;
	}
	if (p1 != p2) {
	  alert("Passwords do not match.");
	  Focus(document.input.new_passwd);
	  return false;
	}
	return true;
      }
      //-->
      </script>
      <form name="input" onsubmit="return CheckForm();" action="admin_passwd_set.cgi" method="post">
      <table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
	  <td class="title" align="center">
	    <b>Change Password</b>
	  </td>
	</tr>
	<tr>
	  <td>
	    <table>
		  <tr>
		<td>Current root name:</td>
		<td><input type="text" readonly name="old_root" value="`grep ":0:0:" /etc/passwd | sed -e 's/\:.*//'`"/></td>
		  </tr>
		  <tr>
		<td>New root name:</td>
		<td><input type="text" name="new_root"/></td>
		  </tr>
          <tr>
        <td nowrap>Old Password</td>
        <td><input type="password" name="old_passwd"></td>
          </tr>
	      <tr>
		<td nowrap>New Password</td>
		<td><input type="password" name="new_passwd"></td>
	      </tr>
	      <tr>
		<td nowrap>Confirm Password</td>
		<td><input type="password" name="new_passwd2"></td>
	      </tr>
	    </table>
	  </td>
	</tr>
	<tr>
	  <td><input type="submit" name="apply" value="Apply"></td>
	</tr>
      </table>
      </form>
      <script language="JavaScript" type="text/javascript">
      <!--
      document.input.new_root.focus();
      //-->
      </script>
EOF

cat include/end.inc

