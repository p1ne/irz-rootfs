#!/bin/sh /usr/lib/irz-web/setscript
if [ "`formq rtc`" = "ntp" ]; then
    NTP_SERVER=`formq ntp_server`
	ntpdate -u -p 3 -t 10 $NTP_SERVER > /dev/null
	if [ $? = "0" ]; then
		hwclock -w -u
		echo "<br>RTC succesfully synchronized with "$NTP_SERVER
	else
		echo "<br>Failed to synchronize  RTC with "$NTP_SERVER
	fi
else
    rtc_year=`formq rtc_year`
    rtc_month=`formq rtc_month`
    rtc_day=`formq rtc_day`
    rtc_hours=`formq rtc_hours`
    rtc_minutes=`formq rtc_minutes`
    rtc_seconds=`formq rtc_seconds`
	date $rtc_month$rtc_day$rtc_hours$rtc_minutes$rtc_year.$rtc_seconds > /dev/null
    if [ $? = "0" ]; then
        hwclock -w -u
        echo "<br>RTC succesfully set to $rtc_year-$rtc_month-$rtc_day $rtc_hours:$rtc_minutes:$rtc_seconds"
    else
        echo "<br>Failed to set  RTC to $rtc_year-$rtc_month-$rtc_day $rtc_hours:$rtc_minutes:$rtc_seconds"
    fi

fi

echo "<hr><a href=\"admin_rtc.cgi\">Return</a>"
