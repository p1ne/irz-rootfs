#!/bin/sh
[ -e /tmp/sendsms ] && . /tmp/sendsms && rm /tmp/sendsms
./begin $0

echo "</td><td colspan=\"3\" valign=\"top\">"
cat << EOF
<script language="JavaScript" type="text/javascript">
<!--
    function GetValue(obj) {
	    return obj.value.replace(/\s/g, '');
    }
    function Focus(obj) {
    	obj.focus(); obj.select();
    }

	function CheckForm() {
 		var len1 = GetValue(document.input.sendsms_number).length;
		var len2 = GetValue(document.input.sendsms_message).length;
		if ( len1 < 9 ) {
        	alert("Wrong phone number");
	        Focus(document.input.sendsms_number);
			return false;
		}
		
		if (len2 == 0) {
	    	alert("Message too short");
			Focus(document.input.sendsms_message);
		return false;
		}
		if (len2 > 200) {
	    	alert("Message too long");
			Focus(document.input.sendsms_message);
			return false;
		}
		return true;
    }
//-->
</script>
      <form name="input" onsubmit="return CheckForm();" action="admin_sendsms_set.cgi" method="post">
      <table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
	  <td class="title" align="center">
	    <b>Send SMS</b>
	  </td>
	</tr>
	<tr>
	  <td>
	    <table>
	      <tr>
		<td nowrap>Phone Number</td>
		<td>+<input name="sendsms_number" value="$SENDSMS_NUMBER"></td>
	      </tr>
	      <tr>
		<td nowrap>Message Text</td>
		<td><textarea cols="65" rows="4" name="sendsms_message">
EOF
echo -n $SENDSMS_MESSAGE
cat << EOF
</textarea></td>
	      </tr>
	    </table>
	  </td>
	</tr>
	<tr>
	  <td><input type="submit" name="apply" value="Send"></td>
	</tr>
      </table>
      </form>
      <script language="JavaScript" type="text/javascript">
      <!--
      document.input.sendsms_number.focus();
      //-->
      </script>
EOF

cat include/end.inc

