#!/bin/sh

[ -r /mnt/rwfs/settings/settings.ntp ] && . /mnt/rwfs/settings/settings.ntp

[ "$NTPDATE_ENABLED" = "1" ] && CHECKED1="checked"
[ "$NTP_ENABLED" = "1" ] && CHECKED2="checked"
[ "$NTPSERVER_ENABLED" = "1" ] && CHECKED3="checked"
[ "$NTP_TZ" = "GMT+12" ] && selm12="selected" && flag=true
[ "$NTP_TZ" = "GMT+11" ] && selm11="selected" && flag=true
[ "$NTP_TZ" = "GMT+10" ] && selm10="selected" && flag=true
[ "$NTP_TZ" = "GMT+09" ] &&  selm9="selected" && flag=true
[ "$NTP_TZ" = "GMT+08" ] &&  selm8="selected" && flag=true
[ "$NTP_TZ" = "GMT+07" ] &&  selm7="selected" && flag=true
[ "$NTP_TZ" = "GMT+06" ] &&  selm6="selected" && flag=true
[ "$NTP_TZ" = "GMT+05" ] &&  selm5="selected" && flag=true
[ "$NTP_TZ" = "GMT+04" ] &&  selm4="selected" && flag=true
[ "$NTP_TZ" = "GMT+03" ] &&  selm3="selected" && flag=true
[ "$NTP_TZ" = "GMT+02" ] &&  selm2="selected" && flag=true
[ "$NTP_TZ" = "GMT+01" ] &&  selm1="selected" && flag=true
[ "$NTP_TZ" = "GMT+00" ] &&  selp0="selected" && flag=true
[ "$NTP_TZ" = "GMT-01" ] &&  selp1="selected" && flag=true
[ "$NTP_TZ" = "GMT-02" ] &&  selp2="selected" && flag=true
[ "$NTP_TZ" = "GMT-03" ] &&  selp3="selected" && flag=true
[ "$NTP_TZ" = "GMT-04" ] &&  selp4="selected" && flag=true
[ "$NTP_TZ" = "GMT-05" ] &&  selp5="selected" && flag=true
[ "$NTP_TZ" = "GMT-06" ] &&  selp6="selected" && flag=true
[ "$NTP_TZ" = "GMT-07" ] &&  selp7="selected" && flag=true
[ "$NTP_TZ" = "GMT-08" ] &&  selp8="selected" && flag=true
[ "$NTP_TZ" = "GMT-09" ] &&  selp9="selected" && flag=true
[ "$NTP_TZ" = "GMT-10" ] &&  selp10="selected" && flag=true
[ "$NTP_TZ" = "GMT-11" ] &&  selp11="selected" && flag=true
[ "$NTP_TZ" = "GMT-12" ] &&  selp12="selected" && flag=true
[ "$NTP_TZ" = "GMT-13" ] &&  selp13="selected" && flag=true
[ "$NTP_TZ" = "GMT-14" ] &&  selp14="selected" && flag=true
[ "$flag" != "true" ] && selp4="selected"

./begin $0

echo "</td><td colspan=\"3\" valign=\"top\">"
cat include/js.inc
cat << EOF

function ntp_changed() {
    var secret = !document.input.ntp_enabled.checked;
    document.input.ntpserver_enabled.disabled = secret;
    document.input.ntpserver_enabled.style.color = (secret) ? "grey" : "";
}

      function CheckForm() {
	if (document.input.ntp_enabled.checked || document.input.ntpdate_enabled.checked) {
	  var len1 = GetValue(document.input.ntp_primary_server).length;
	  var len2 = GetValue(document.input.ntp_secondary_server).length;
	  if (len1 == 0 && len2 == 0) {
	    alert("Missing primary NTP server address.");
	    Focus(document.input.ntp_primary_server);
	    return false;
	  }
	  if (len1 > 0 && len1 < 6) {
	    alert("Invalid primary NTP server address.");
	    Focus(document.input.ntp_primary_server);
	    return false;
	  }
	  if (len2 > 0 && len2 < 6) {
	    alert("Invalid secondary NTP server address.");
	    Focus(document.input.ntp_secondary_server);
	    return false;
	  }
	}
	return true;
      }

window.onload=ntp_changed;

      //-->
      </script>
      <form name="input" onsubmit="return CheckForm();" action="config_ntp_set.cgi" method="post">
      <table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
	  <td class="title" align="center">
	    <b>NTP Configuration</b>
	  </td>
	</tr>
	<tr>
	  <td>
	    <table>
          <tr>
        <td><input type="checkbox" name="ntpdate_enabled" $CHECKED1></td>
        <td nowrap>Synchronize clock with NTP server on first connect</td>
          </tr>
	      <tr>
		<td><input type="checkbox" onclick="ntp_changed();" name="ntp_enabled" $CHECKED2></td>
		<td nowrap>Enable clock synchronization with NTP</td>
	      </tr>
          <tr>
        <td><input type="checkbox" name="ntpserver_enabled" $CHECKED3></td>
        <td nowrap>Allow to use as NTP server</td>
          </tr>
	    </table>
	    <table>
	      <tr>
		<td nowrap>Primary NTP Server Address</td>
		<td><input name="ntp_primary_server" value="$NTP_PRIMARY_SERVER"></td>
	      </tr>
	      <tr>
		<td nowrap>Secondary NTP Server Address</td>
		<td><input name="ntp_secondary_server" value="$NTP_SECONDARY_SERVER"></td>
	      </tr>
		  <tr>
		<td nowrap>Local time zone </td>
		<td><select name="ntp_tz">
			<option value="GMT+12" $selm12>GMT-12 
			<option value="GMT+11" $selm11>GMT-11
            <option value="GMT+10" $selm10>GMT-10
            <option value="GMT+09" $selm9>GMT-09
            <option value="GMT+08" $selm8>GMT-08
            <option value="GMT+07" $selm7>GMT-07
            <option value="GMT+06" $selm6>GMT-06
            <option value="GMT+05" $selm5>GMT-05
            <option value="GMT+04" $selm4>GMT-04
            <option value="GMT+03" $selm3>GMT-03
            <option value="GMT+02" $selm2>GMT-02
            <option value="GMT+01" $selm1>GMT-01
            <option value="GMT+00" $selp0>GMT+00
            <option value="GMT-01" $selp1>GMT+01
            <option value="GMT-02" $selp2>GMT+02
            <option value="GMT-03" $selp3>GMT+03
            <option value="GMT-04" $selp4>GMT+04
            <option value="GMT-05" $selp5>GMT+05
            <option value="GMT-06" $selp6>GMT+06
            <option value="GMT-07" $selp7>GMT+07
            <option value="GMT-08" $selp8>GMT+08
            <option value="GMT-09" $selp9>GMT+09
            <option value="GMT-10" $selp10>GMT+10
            <option value="GMT-11" $selp11>GMT+11
            <option value="GMT-12" $selp12>GMT+12
            <option value="GMT-13" $selp13>GMT+13
            <option value="GMT-14" $selp14>GMT+14
		</select></td>
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
      document.input.ntp_enabled.focus();
      //-->
      </script>
EOF

cat include/end.inc

