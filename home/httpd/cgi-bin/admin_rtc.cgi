#!/bin/sh

./begin $0

year=`date +%Y`
month=`date +%m`
day=`date +%d`
hours=`date +%H`
minutes=`date +%M`
seconds=`date +%S`

echo "</td><td colspan=\"3\" valign=\"top\">"
cat include/js.inc
cat << EOF
    function FocusNtp() {
        document.getElementById("rtc_ntp").checked = true;
    }

    function FocusMan() {
        document.getElementById("rtc_man").checked = true;
    }
      function CheckForm() {
	if (document.input.rtc[0].checked) {
		if (GetValue(document.input.ntp_server).length < 6) {
	  		alert("Invalid or missing NTP server address.");
	  		Focus(document.input.ntp_server);
	  		return false;
		}
		return true;
	} else {
		var year = document.input.rtc_year.value;
		if ((year.length != 4) || (parseInt(year) < 2000) || (parseInt(year, 10) > 2999)) {
			alert("Wrong or missing year");
			Focus(document.input.rtc_year);
			return false;
		}
		var month = document.input.rtc_month.value;
		if ( (parseInt(month, 10) < 10) && (month.length == 1) ) {
			document.input.rtc_month.value="0"+month;
		}
		var month = document.input.rtc_month.value;
        if ((month.length != 2) || (parseInt(month, 10) < 1) || (parseInt(month, 10) > 12)) {
            alert("Wrong or missing month");
            Focus(document.input.rtc_month);
            return false;
        }
		var day = document.input.rtc_day.value;
        if ( (parseInt(day, 10) < 10) && (day.length == 1) ) {
            document.input.rtc_day.value="0"+day;
        }
		var day = document.input.rtc_day.value;
        if ((day.length != 2) || (parseInt(day, 10) < 1) || (parseInt(day, 10) > 31))  {
            alert("Wrong or missing day");
            Focus(document.input.rtc_day);
            return false;
        }
		var hours = document.input.rtc_hours.value;
        if ( (parseInt(hours, 10) < 10) && (hours.length == 1) ) {
            document.input.rtc_hours.value="0"+hours;
        }
		var hours = document.input.rtc_hours.value;
        if ((hours.length != 2) || (parseInt(hours, 10) < 0) || (parseInt(hours, 10) > 23))  {
            alert("Wrong or missing hours");
            Focus(document.input.rtc_hours);
            return false;
        }
		var minutes = document.input.rtc_minutes.value;
        if ( (parseInt(minutes, 10) < 10) && (minutes.length == 1) ) {
            document.input.rtc_minutes.value="0"+minutes;
        }
		var minutes = document.input.rtc_minutes.value;
        if ((minutes.length != 2) || (parseInt(minutes, 10) < 0) || (parseInt(minutes, 10) > 59)) {
            alert("Wrong or missing minutes");
            Focus(document.input.rtc_minutes);
            return false;
        }
		var seconds = document.input.rtc_seconds.value;
        if ( (parseInt(seconds, 10) < 10) && (seconds.length == 1) ) {
            document.input.rtc_seconds.value="0"+seconds;
        }
        var seconds = document.input.rtc_seconds.value;
        if ((seconds.length != 2) || (parseInt(seconds, 10) < 0) || (parseInt(seconds, 10) > 59)) {
            alert("Wrong or missing seconds");
            Focus(document.input.rtc_seconds);
            return false;
        }

		return true;
    }
	  }
      //-->
      </script>
      <form name="input" onsubmit="return CheckForm();" action="admin_rtc_set.cgi" method="post">
      <table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
	  <td class="title" align="center">
	    <b>Set Real Time Clock</b>
	  </td>
	</tr>
	<tr>
	  <td>
	  Current date and time:&nbsp;
EOF

echo `date`

cat << EOF
	  </td>
	</tr>
	<tr>
	  <td>
	    <table>
	      <tr>
		<td nowrap><input type="radio" name="rtc" id="rtc_ntp" value="ntp" checked>NTP Server Address</td>
		<td><input name="ntp_server" value="0.pool.ntp.org" onclick="FocusNtp()"></td>
	      </tr>
		  <tr>
		<td nowrap><input type="radio" name="rtc" id="rtc_man" value="man">Enter manually</td>
		<td>
		  <table>
			<tr>
			  <td>Year</td><td> </td><td>Month</td><td> </td><td>Day</td><td>&nbsp;&nbsp;&nbsp;</td>
			  <td>Hours</td><td> </td><td>Minutes</td><td> </td><td>Seconds</td>
			</tr>
			<tr>
			  <td><input name="rtc_year"	maxlength="4" size="4" value="$year"    onclick="FocusMan()"></td><td>-</td>
			  <td><input name="rtc_month"	maxlength="2" size="2" value="$month"   onclick="FocusMan()"></td><td>-</td>
			  <td><input name="rtc_day"		maxlength="2" size="2" value="$day"     onclick="FocusMan()"></td><td>&nbsp;&nbsp;&nbsp;</td>
			  <td><input name="rtc_hours"	maxlength="2" size="2" value="$hours"   onclick="FocusMan()"></td><td>:</td>
			  <td><input name="rtc_minutes" maxlength="2" size="2" value="$minutes" onclick="FocusMan()"></td><td>:</td>
			  <td><input name="rtc_seconds" maxlength="2" size="2" value="$seconds" onclick="FocusMan()"></td>
			</tr>
		  </table>
		</td>
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
      document.input.ntp_server.focus();
      //-->
      </script>
EOF

cat include/end.inc

