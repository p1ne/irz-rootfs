#!/bin/sh

[ -e /mnt/rwfs/settings/settings.sms ] && . /mnt/rwfs/settings/settings.sms

[ "$SMS_SEND_POWERUP" = "1" ] && POWERUP="checked"
[ "$SMS_SEND_CONNECT" = "1" ] && CONNECT="checked"
[ "$SMS_SEND_DISCONNECT" = "1" ] && DISCONNECT="checked"
[ "$SMS_SEND_ETH_DISCONNECT" = "1" ] && ETH_DISCONNECT="checked"
[ "$SMS_SEND_ETH_CONNECT" = "1" ] && ETH_CONNECT="checked"

./begin $0

echo "</td><td colspan=\"3\" valign=\"top\">"
cat include/js.inc

cat << EOF
      function CheckForm() {
	if ((document.input.sms_send_powerup.checked || document.input.sms_send_connect.checked || document.input.sms_send_disconnect.checked) &&
	    GetValue(document.input.sms_phone_no1) == 0 && GetValue(document.input.sms_phone_no2) == 0) {
	  alert("Missing phone number.");
	  Focus(document.input.sms_phone_no1);
	  return false;
	}
	return true;
      }
      //-->
      </script>
      <form name="input" onsubmit="return CheckForm();" action="config_sms_set.cgi" method="post">
      <table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
	  <td class="title" align="center">
	    <b>SMS Configuration</b>
	  </td>
	</tr>
	<tr>
	  <td>
	    <table>
	      <tr>
		<td><input type="checkbox" name="sms_send_powerup" $POWERUP></td>
		<td nowrap>Send SMS on power up</td>
	      </tr>
	    </table>
        <table>
          <tr>
        <td><input type="checkbox" name="sms_send_connect" $CONNECT></td>
        <td nowrap>Send SMS on GPRS connect</td>
          </tr>
        </table>
	    <table>
	      <tr>
		<td><input type="checkbox" name="sms_send_disconnect" $DISCONNECT></td>
		<td nowrap>Send SMS on GPRS disconnect</td>
	      </tr>
	    </table>
	    <table>
    		<tr>
		    <td><input type="checkbox" name="sms_send_eth_connect" $ETH_CONNECT></td>
		    <td nowrap>Send SMS on USB-Ethernet connect</td>
		</tr>
	    </table>
	    <table>
		 <tr>
		    <td><input type="checkbox" name="sms_send_eth_disconnect" $ETH_DISCONNECT></td>
		    <td nowrap>Send SMS on USB-Ethernet disconnect</td>
		</tr>
	    </table>
	    <table>
	      <tr>
		<td nowrap>Phone Number 1 +</td>
		<td><input name="sms_phone_no1" value="$SMS_PHONE_NO1"></td>
	      </tr>
	      <tr>
		<td nowrap>Phone Number 2 +</td>
		<td><input name="sms_phone_no2" value="$SMS_PHONE_NO2"></td>
	      </tr>
	      <tr>
		<td nowrap>Unit ID*</td>
		<td><input name="sms_unit_id" value="$SMS_UNIT_ID"></td>
	      </tr>
	      <tr>
		<td nowrap>* <i>can be blank</i></td>
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
      document.input.sms_send_powerup.focus();
      //-->
      </script>
EOF

cat include/end.inc

