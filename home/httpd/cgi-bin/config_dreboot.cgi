#!/bin/sh

[ -e /mnt/rwfs/settings/settings.dreboot ] && . /mnt/rwfs/settings/settings.dreboot

[ "$DREBOOT_ENABLED" = "1" ] && ENABLED="checked"

./begin $0

echo "</td><td colspan=\"3\" valign=\"top\">"
cat include/js.inc

cat << EOF
	function CheckForm() {
		if (document.input.dreboot_enabled.checked) {
	  		if ((document.input.dreboot_hours.value > 23) || (document.input.dreboot_hours.value < 0 )) {
				alert("Wrong hour");
				Focus(document.input.dreboot_hours);
				return false;
			}
            if ((document.input.dreboot_minutes.value > 59) || (document.input.dreboot_minutes.value < 0 )) {
                alert("Wrong minute");
                Focus(document.input.dreboot_minutes);
                return false;
            }

		}		
		return true;
    }
      //-->
      </script>
      <form name="input" onsubmit="return CheckForm();" action="config_dreboot_set.cgi" method="post">
      <table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
	  <td class="title" align="center">
	    <b>Daily Reboot Configuration</b>
	  </td>
	</tr>
	<tr>
	  <td>
	    <table>
	      <tr>
		<td><input type="checkbox" name="dreboot_enabled" $ENABLED></td>
		<td nowrap>Reboot daily at given time</td>
	      </tr>
	    </table>
	    <table>
	      <tr>
		<td>Reboot at <input name="dreboot_hours" size="2" maxlength="2" value="$DREBOOT_HOURS"> :
		<input name="dreboot_minutes" size="2" maxlength="2" value="$DREBOOT_MINUTES"></td>
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
      document.input.dreboot_enabled.focus();
      //-->
      </script>
EOF

cat include/end.inc

