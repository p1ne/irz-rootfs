#!/bin/sh
SETS=/mnt/rwfs/settings/settings.ppp
[ ! -f $SETS ] && cp /etc/defaults/settings.ppp $SETS
. $SETS

if [ "$PPP_ENABLED" = "0" ]; then
    EN="selected"
elif [ "$PPP_SIMCARD" = "2" ]; then
    SIM2="selected"
else
    SIM1="selected"
fi

PPP_APN_DEC=`decode "$PPP_APN"`
PPP_APN2_DEC=`decode "$PPP_APN2"`
PPP_USERNAME_DEC=`decode "$PPP_USERNAME"`
PPP_USERNAME2_DEC=`decode "$PPP_USERNAME2"`
PPP_PASSWORD_DEC=`decode "$PPP_PASSWORD"`
PPP_PASSWORD2_DEC=`decode "$PPP_PASSWORD2"`

case $PPP_AUTH in
    pap)    PPP_AUTH_PAP="selected";;
    chap)   PPP_AUTH_CHAP="selected";;
    *)      PPP_AUTH_ANY="selected";;
esac
case $PPP_AUTH2 in
    pap)    PPP_AUTH_PAP2="selected";;
    chap)   PPP_AUTH_CHAP2="selected";;
    *)      PPP_AUTH_ANY2="selected";;
esac
[ -f /mnt/rwfs/settings/settings.pin1 ] && PPP_PIN=`cat /mnt/rwfs/settings/settings.pin1`
[ -f /mnt/rwfs/settings/settings.pin2 ] && PPP_PIN2=`cat /mnt/rwfs/settings/settings.pin2`

[ -z "$PPP_MTU" ] && PPP_MTU=1500
[ -z "$PPP_MRU" ] && PPP_MRU=1500
[ -z "$PPP_MTU2" ] && PPP_MTU2=1500
[ -z "$PPP_MRU2" ] && PPP_MRU2=1500

case $PPP_USEDNS in
    useowndns)  USEOWNDNS="selected";;
    usenonedns) USENONEDNS="selected";;
    *)          USEPEERDNS="selected";;
esac
case $PPP_USEDNS2 in
    useowndns)  USEOWNDNS2="selected";;
    usenonedns) USENONEDNS2="selected";;
    *)          USEPEERDNS2="selected";;
esac

if [ "$PPP_ALLOW_ROAMING" = "1" ]; then
    ROAMING="selected"
else
    NOROAMING="selected"
fi
if [ "$PPP_ALLOW_ROAMING2" = "1" ]; then
    ROAMING2="selected"
else
    NOROAMING2="selected"
fi
if [ "$PPP_PING" = "1" ]; then
    PING="selected"
    NPING=""
else
    PING=""
    NPING="selected"
fi
if [ "$PPP_PING2" = "1" ]; then
    PING2="selected"
    NPING2=""
else
    PING2=""
    NPING2="selected"
fi

[ "$PPP_SWITCH" = "1" ] && SWITCH="checked"
[ "$PPP_TRYPRIMARY" = "1" ] && TRYPRIMARY="checked"
[ "$PPP_REBOOT" = "1" ] && REBOOT="checked"
[ -z "$PPP_PERSIST" ] && PPP_PERSIST=1
[ "$PPP_PERSIST" = "1" ] && PERSIST="checked"
[ -z "$PPP_DIAL" ] && PPP_DIAL="*99#"
[ -z "$PPP_DIAL2" ] && PPP_DIAL2="*99#"
[ -z "$PPP_MAXFAIL" ] && PPP_MAXFAIL=3
[ -z "$PPP_RETRY" ] && PPP_RETRY=30
[ -z "$PPP_SOFTRETR" ] && PPP_SOFTRETR=3

if [ "$PPP_BAND" = "00000100" ]; then
    band_1="SELECTED"
elif [ "$PPP_BAND" = "00000080" ]; then
    band_2="SELECTED"
elif [ "$PPP_BAND" = "00200000" ]; then
    band_4="SELECTED"
elif [ "$PPP_BAND" = "00080000" ]; then
    band_8="SELECTED"
elif [ "$PPP_BAND" = "00200100" ]; then
    band_3="SELECTED"
elif [ "$PPP_BAND" = "00000180" ]; then
    band_5="SELECTED"
elif [ "$PPP_BAND" = "00080080" ]; then
    band_10="SELECTED"
elif [ "$PPP_BAND" = "00280000" ]; then
    band_12="SELECTED"
elif [ "$PPP_BAND" = "00400380" ]; then
    band_13="SELECTED"
else
    band_15="SELECTED"
fi

if [ "$PPP_BAND2" = "00000100" ]; then
    band2_1="SELECTED"
elif [ "$PPP_BAND2" = "00000080" ]; then
    band2_2="SELECTED"
elif [ "$PPP_BAND2" = "00200000" ]; then
    band2_4="SELECTED"
elif [ "$PPP_BAND2" = "00080000" ]; then
    band2_8="SELECTED"
elif [ "$PPP_BAND2" = "00200100" ]; then
    band2_3="SELECTED"
elif [ "$PPP_BAND2" = "00000180" ]; then
    band2_5="SELECTED"
elif [ "$PPP_BAND2" = "00080080" ]; then
    band2_10="SELECTED"
elif [ "$PPP_BAND2" = "00280000" ]; then
    band2_12="SELECTED"
elif [ "$PPP_BAND2" = "00400380" ]; then
    band2_13="SELECTED"
else
    band2_15="SELECTED"
fi

if [ "$PPP_MODE" = "2g" ]; then
    ppp_mode_2g="SELECTED"
elif [ "$PPP_MODE" = "2gp" ]; then
    ppp_mode_2gp="SELECTED"
elif [ "$PPP_MODE" = "3g" ]; then
    ppp_mode_3g="SELECTED"
elif [ "$PPP_MODE" = "3gp" ]; then
    ppp_mode_3gp="SELECTED" 
else
    ppp_mode_auto="SELECTED"
fi

if [ "$PPP_MODE2" = "2g" ]; then
    ppp2_mode_2g="SELECTED"
elif [ "$PPP_MODE2" = "2gp" ]; then
    ppp2_mode_2gp="SELECTED"
elif [ "$PPP_MODE2" = "3g" ]; then
    ppp2_mode_3g="SELECTED"
elif [ "$PPP_MODE2" = "3gp" ]; then
    ppp2_mode_3gp="SELECTED"    
else
    ppp2_mode_auto="SELECTED"
fi

./begin $0

echo "</td><td colspan=\"3\" valign=\"top\">"
cat include/js.inc

cat << EOF
      function IsValidHOSTS(obj, zero) {
	  var str = GetValue(obj);
	  if (zero && str.length == 0) {
	      return true;
	  }
	  re = /(www\.)?([^\.]+)\.(\w{2}|(com|net|org|edu|int|mil|gov|arpa|biz|aero|name|coop|info|pro|museum))$/;
	  var hosts = str.split(';');
	  for ( var i = 0, len = hosts.length; i < len; i++) {
	      if (!re.test(hosts[i])) {
		  var fields = hosts[i].match(/^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$/);
		  if (fields != null) {
		      var tmp = fields[1] | fields[2] | fields[3] | fields[4];
		      if (!((tmp < 256) && (zero || tmp > 0))) {
			      return false;
		      }
		  } else {
		      return false;
		  }
	      }
	  }
	  return true;
      }

      function CheckForm() {
    var ping_enabled = document.input.ppp_ping.selectedIndex;
    var ping_enabled2 = document.input.ppp_ping2.selectedIndex;
    var switch_enabled = document.input.ppp_switch.checked;
    var ping_intvl = parseInt(GetValue(document.input.ppp_ping_intvl));
    var ping_intvl2 = parseInt(GetValue(document.input.ppp_ping_intvl2));
    var ping_repeat_intvl = parseInt(GetValue(document.input.ppp_ping_repeat_intvl));
    var ping_repeat_intvl2 = parseInt(GetValue(document.input.ppp_ping_repeat_intvl2));
    var ping_count = parseInt(GetValue(document.input.ppp_ping_count));
    var ping_count2 = parseInt(GetValue(document.input.ppp_ping_count2));
    var maxfail_att = parseInt(GetValue(document.input.ppp_maxfail));
    var retry_cnt = parseInt(GetValue(document.input.ppp_retry));
    var ppp_dial = document.input.ppp_dial.value.length;
    var ppp_dial2 = document.input.ppp_dial2.value.length;
    var ppp_mru = parseInt(GetValue(document.input.ppp_mru));
    var ppp_mru2 = parseInt(GetValue(document.input.ppp_mru2));
    var ppp_mtu = parseInt(GetValue(document.input.ppp_mtu));
    var ppp_mtu2 = parseInt(GetValue(document.input.ppp_mtu2));
    if (!IsValidIP(document.input.ppp_ipaddr, true)) {
      alert("Invalid Local IP address 1");
      Focus(document.input.ppp_ipaddr);
      return false;
    }
    if (!IsValidIP(document.input.ppp_ripaddr, true)) {
      alert("Invalid Remote IP address 1");
      Focus(document.input.ppp_ripaddr);
      return false;
    }

    if (!IsValidIP(document.input.ppp_ipaddr2, true)) {
      alert("Invalid Local IP address 2");
      Focus(document.input.ppp_ipaddr2);
      return false;
    }
    if (!IsValidIP(document.input.ppp_ripaddr2, true)) {
      alert("Invalid Remote IP address 2");
      Focus(document.input.ppp_ripaddr2);
      return false;
    }


    if (ppp_dial < 1) {
      alert("Invalid or missing Dial Number 1");
      Focus(document.input.ppp_dial);
      return false;
    }
    if (ppp_dial2 < 1) {
      alert("Invalid or missing Dial Number 2");
      Focus(document.input.ppp_dial2);
      return false;
    }
    if (ppp_mru < 128 || isNaN(ppp_mru)) {
      alert("Invalid or missing MRU 1");
      Focus(document.input.ppp_mru);
      return false;
    }
    if (ppp_mru2 < 128 || isNaN(ppp_mru2)) {
      alert("Invalid or missing MRU 2");
      Focus(document.input.ppp_mru2);
      return false;
    }

    if (ppp_mtu < 128 || isNaN(ppp_mtu)) {
      alert("Invalid or missing MTU.");
      Focus(document.input.ppp_mtu);
      return false;
    }
    if (ppp_mtu2 < 128 || isNaN(ppp_mtu2)) {
      alert("Invalid or missing MTU 2");
      Focus(document.input.ppp_mtu2);
      return false;
    }

    if (document.input.ppp_dns.value == "useowndns") {
        if (!IsValidIP(document.input.ppp_dns_server, false)) {
          alert("Invalid DNS server 1");
          Focus(document.input.ppp_dns_server);
          return false;
        }
        if (!IsValidIP(document.input.ppp_dns_secondary, true)) {
          alert("Invalid DNS server 2");
          Focus(document.input.ppp_dns_secondary);
          return false;
        }
    }
    if (document.input.ppp_dns2.value == "useowndns") {
        if (!IsValidIP(document.input.ppp_dns_server2, false)) {
          alert("Invalid DNS server 1");
          Focus(document.input.ppp_dns_server2);
          return false;
        }
        if (!IsValidIP(document.input.ppp_dns_secondary2, true)) {
          alert("Invalid DNS server 2");
          Focus(document.input.ppp_dns_secondary2);
          return false;
        }
    }
    if (ping_enabled=="0") {
	if (!IsValidHOSTS(document.input.ppp_ping_ipaddr, false)) {
	    alert("Invalid ping URL or IP address #1");
	    Focus(document.input.ppp_ping_ipaddr);
	    return false;
	}
    }
    if (ping_enabled2=="0") {
	if (!IsValidHOSTS(document.input.ppp_ping_ipaddr2, false)) {
	    alert("Invalid ping URL or IP address #2");
	    Focus(document.input.ppp_ping_ipaddr2);
	    return false;
	}
    }

    if ((ping_enabled=="0") && (ping_intvl <= 0 || isNaN(ping_intvl))) {
      alert("Invalid or missing ping interval #1 (must be 1 or greater).");
      Focus(document.input.ppp_ping_intvl);
      return false;
    }
    if ((ping_enabled2=="0") && (ping_intvl2 <= 0 || isNaN(ping_intvl2))) {
      alert("Invalid or missing ping interval #2 (must be 1 or greater).");
      Focus(document.input.ppp_ping_intvl2);
      return false;
    }
    if ((ping_enabled=="0") && (ping_repeat_intvl <= 0 || isNaN(ping_repeat_intvl))) {
      alert("Invalid or missing ping repeat interval #1 (must be 1 or greater).");
      Focus(document.input.ppp_ping_repeat_intvl);
      return false;
    }
    if ((ping_enabled2=="0") && (ping_repeat_intvl2 <= 0 || isNaN(ping_repeat_intvl2))) {
      alert("Invalid or missing ping repeat interval #2 (must be 1 or greater).");
      Focus(document.input.ppp_ping_repeat_intvl2);
      return false;
    }
    if ((ping_enabled=="0") && (ping_count < 0 || isNaN(ping_count))) {
      alert("Invalid or missing ping failures #1.");
      Focus(document.input.ppp_ping_count);
      return false;
    }
    if ((ping_enabled2=="0") && (ping_count2 < 0 || isNaN(ping_count2))) {
      alert("Invalid or missing ping failures #2.");
      Focus(document.input.ppp_ping_count2);
      return false;
    }
    if (maxfail_att <= 0 || isNaN(maxfail_att)) {
        if (switch_enabled) {
            alert("Invalid or missing SIM switch attempts (must be 1 or greater).");
            Focus(document.input.ppp_maxfail);
            return false;
        } else {
            document.input.ppp_maxfail.value = 3;
        }
    }
    if (switch_enabled && (retry_cnt <= 0 || isNaN(retry_cnt))) {
      alert("Invalid or missing retry primary SIM interval (must be 1 or greater).");
      Focus(document.input.ppp_retry);
      return false;
    }


    return true;
      }
      //-->
      </script>
      <form name="input" onsubmit="return CheckForm();" action="config_ppp_set.cgi" method="post">
      <table width="100%" cellspacing="0" cellpadding="5" border="3">
    <tr>
      <td class="title" align="center">
        <b>Internet Configuration</b>
      </td>
    </tr>
    <tr>
      <td>
        <table width="100%" cellspacing="0" cellpadding="5"> 
          <tr>
            <td nowrap>&nbsp;
              <select name="simcard">
              <option value="0" $EN >Do not connect</option>
              <option value="1" $SIM1 >Connect using SIM 1&nbsp;</option>
              <option value="2" $SIM2 >Connect using SIM 2&nbsp;</option>
              </select>
            </td>
          </tr>                  
        </table>
      </td>
    </tr>
    <tr>
      <td>
        <table width="100%" cellspacing="0" cellpadding="5">
        <tr>
        <td valign="top">
            <table>
              <tr><th colspan="2" align=center><b>SIM card #1</b></th></tr>
              <tr>
            <td nowrap>APN *</td>
            <td><input class="input" name="ppp_apn" value="$PPP_APN_DEC"></td>
              </tr>
              <tr>
            <td nowrap>Username *</td>
            <td><input class="input" name="ppp_username" value="$PPP_USERNAME_DEC"></td>
              </tr>
              <tr>
            <td nowrap>Password *</td>
            <td><input class="input" name="ppp_password" value="$PPP_PASSWORD_DEC"></td>
              </tr>
              <tr>
            <td>Authentication</td>
            <td><select class="input" name="ppp_auth">
              <option value="any" $PPP_AUTH_ANY >Any</option>
              <option value="pap" $PPP_AUTH_PAP >PAP</option>
              <option value="chap" $PPP_AUTH_CHAP >CHAP</option>
            </select></td>
              </tr>
              <tr>
            <td nowrap>PIN *</td>
                <td><input class="input" type="password" name="ppp_pin" value="$PPP_PIN" maxlength="15"></td>
              </tr>
              <tr>
            <td nowrap>Local IP Address *</td>
                <td><input class="input" name="ppp_ipaddr" value="$PPP_IPADDR"></td>
              </tr>
              <tr>
            <td nowrap>Remote IP Address *</td>
                <td><input class="input" name="ppp_ripaddr" value="$PPP_RIPADDR"></td>
              </tr>
              <tr>
                <td nowrap>Dial Number</td>
            <td><input class="input" name="ppp_dial" value="$PPP_DIAL"></td>
              </tr>
              <tr>
            <td nowrap>MRU (bytes)</td>
            <td><input class="input" name="ppp_mru" value="$PPP_MRU"></td>
              </tr>
              <tr>
            <td nowrap>MTU (bytes)</td>
            <td><input class="input" name="ppp_mtu" value="$PPP_MTU"></td>
              </tr>
              <tr>
            <td>Allow roaming</td>
            <td><select class="input" name="ppp_roaming">
              <option value="1" $ROAMING >Enabled</option>
              <option value="0" $NOROAMING >Disabled</option>
            </select></td>
              </tr>
              <tr>
            <td nowrap>Set GSM bands to&nbsp;</td><td>
              <select class="input" name="ppp_band">
              <option value="3FFFFFFF"  $band_15 >All</option>
              <option value="00000100"  $band_1 >900 MHz</option>
              <option value="00000080"  $band_2 >1800 MHz</option>
              <option value="00200000" $band_4 >1900 MHz</option>
              <option value="00080000" $band_8 >850 MHz</option>
              <option value="00200100" $band_3 >900+1900 MHz</option>
              <option value="00000180" $band_5 >900+1800 MHz</option>
              <option value="00080080" $band_10 >850+1800 MHz</option>
              <option value="00280000" $band_12 >850+1900 MHz</option>
              <option value="00400380" $band_13 >900+1800+2100 MHz</option>
              </select>
            </td>
              </tr>
        <tr>
                <td nowrap>Set modem mode to&nbsp;</td>
                <td>
                    <select class="input" name="ppp_mode">
                        <option value="auto" $ppp_mode_auto>Auto</option>
                        <option value="2g" $ppp_mode_2g>2G only</option>
                        <option value="2gp" $ppp_mode_2gp>2G preferred</option>
                        <option value="3g" $ppp_mode_3g>3G only</option>
                        <option value="3gp" $ppp_mode_3gp>3G preferred</option>
                    </select>
                </td>
        </tr>
              <tr>                                                  
            <td nowrap>DNS Service</td>                             
            <td><select class="input" name="ppp_dns">
                <option value="usenonedns" $USENONEDNS>Do not use DNS service&nbsp;</option>
                <option value="usepeerdns" $USEPEERDNS>Get DNS from operator&nbsp;</option>
                <option value="useowndns" $USEOWNDNS>Set manually&nbsp;</option>
            </select>                                               
            </td>                                                   
            </tr>                                                 
            <tr>                                                  
            <td nowrap>DNS Server 1</td>
            <td><input class="input" name="ppp_dns_server" value="$PPP_DNS_SERVER">
            </tr>
            <tr>
            <td nowrap>DNS Server 2</td>
            <td><input class="input" name="ppp_dns_secondary" value="$PPP_DNS_SECONDARY">
            </tr>
          <tr>
        <td nowrap>Check connection</td>
        <td><select class="input" name="ppp_ping">
            <option value="on" $PING >Yes&nbsp;</option>
            <option value="off" $NPING>No&nbsp;</option>
        </select></td>
          </tr>
          <tr>
         <td nowrap>Ping IP Address(es)</td>
         <td><input class="input" maxlength="100" name="ppp_ping_ipaddr" value="$PPP_PING_IPADDR"></td>
          </tr>
          <tr>
        <td nowrap>Ping Interval (min)</td>
        <td><input class="input" maxlength="15" name="ppp_ping_intvl" value="$PPP_PING_INTVL"></td>
          </tr>
          <tr>
        <td nowrap>Ping Repeat Interval (min)</td>
        <td><input class="input" maxlength="15" name="ppp_ping_repeat_intvl" value="$PPP_PING_REPEAT_INTVL"></td>
          </tr>
          <tr>
        <td nowrap>Allow failures</td>
        <td><input class="input" maxlength="3" name="ppp_ping_count" value="$PPP_PING_COUNT"></td>  
          </tr>
              <tr>
            <td nowrap>* <i>can be blank</i></td>  
              </tr>
            </table>
        </td>
        <td valign="top">
            <table>
              <tr><th colspan="2" align=center><b>SIM card #2</b></th></tr>
              <tr>
            <td nowrap>APN *</td>
            <td><input class="input" name="ppp_apn2" value="$PPP_APN2_DEC"></td>
              </tr>
              <tr>
            <td nowrap>Username *</td>
            <td><input class="input" name="ppp_username2" value="$PPP_USERNAME2_DEC"></td>
              </tr>
              <tr>
            <td nowrap>Password *</td>
            <td><input class="input" name="ppp_password2" value="$PPP_PASSWORD2_DEC"></td>
              </tr>
              <tr>
            <td>Authentication</td>
            <td><select class="input" name="ppp_auth2">
              <option value="any" $PPP_AUTH_ANY2 >Any</option>
              <option value="pap" $PPP_AUTH_PAP2 >PAP</option>
              <option value="chap" $PPP_AUTH_CHAP2 >CHAP</option>
            </select></td>
              </tr>
              <tr>
            <td nowrap>PIN *</td>
                <td><input class="input" type="password" name="ppp_pin2" value="$PPP_PIN2" maxlength="15"></td>
              </tr>
              <tr>
            <td nowrap>Local IP Address *</td>
                <td><input class="input" name="ppp_ipaddr2" value="$PPP_IPADDR2"></td>
              </tr>
             <tr>
            <td nowrap>Remote IP Address *</td>
                <td><input class="input" name="ppp_ripaddr2" value="$PPP_RIPADDR2"></td>
              </tr>
              <tr>
                <td nowrap>Dial Number</td>
            <td><input class="input" name="ppp_dial2" value="$PPP_DIAL2"></td>
              </tr>
              <tr>
            <td nowrap>MRU (bytes)</td>
            <td><input class="input" name="ppp_mru2" value="$PPP_MRU2"></td>
              </tr>
              <tr>
            <td nowrap>MTU (bytes)</td>
            <td><input class="input" name="ppp_mtu2" value="$PPP_MTU2"></td>
              </tr>
             <tr>
            <td>Allow roaming</td>
            <td><select class="input" name="ppp_roaming2">
              <option value="1" $ROAMING2 >Enabled</option>
              <option value="0" $NOROAMING2 >Disabled</option>
            </select></td>
              </tr>
              <tr>
            <td nowrap>Set GSM bands to&nbsp;</td>
            <td><select class="input" name="ppp_band2">
              <option value="3FFFFFFF"  $band2_15 >All</option>
              <option value="00000100"  $band2_1 >900 MHz</option>
              <option value="00000080"  $band2_2 >1800 MHz</option>
              <option value="00200000" $band2_4 >1900 MHz</option>
              <option value="00080000" $band2_8 >850 MHz</option>
              <option value="00200100" $band2_3 >900+1900 MHz</option>
              <option value="00000180" $band2_5 >900+1800 MHz</option>
              <option value="00080080" $band2_10 >850+1800 MHz</option>
              <option value="00280000" $band2_12 >850+1900 MHz</option>
              <option value="00400380" $band2_13 >900+1800+2100 MHz</option>
              </select></td>
            </tr>
            <tr>
                <td nowrap>Set modem mode to&nbsp;</td>
                <td>
                    <select class="input" name="ppp_mode2">
                        <option value="auto" $ppp2_mode_auto>Auto</option>
                        <option value="2g" $ppp2_mode_2g>2G only</option>
                        <option value="2gp" $ppp2_mode_2gp>2G preferred</option>
                        <option value="3g" $ppp2_mode_3g>3G only</option>
                        <option value="3gp" $ppp2_mode_3gp>3G preferred</option>
                    </select>
                </td>
        </tr>
              <tr>    
              <tr>                                                  
            <td nowrap>DNS Service</td>                             
            <td><select class="input" name="ppp_dns2">
                <option value="usenonedns" $USENONEDNS2>Do not use DNS service&nbsp;</option>
                <option value="usepeerdns" $USEPEERDNS2>Get DNS from operator&nbsp;</option>
                <option value="useowndns" $USEOWNDNS2>Set manually&nbsp;</option>
            </select>                                               
            </td>                                                   
            </tr>                                                 
            <tr>                                                  
            <td nowrap>DNS Server 1</td>
            <td><input class="input" name="ppp_dns_server2" value="$PPP_DNS_SERVER2">
            </tr>                                                 
            <tr>                                                  
            <td nowrap>DNS Server 2</td>                      
            <td><input class="input" name="ppp_dns_secondary2" value="$PPP_DNS_SECONDARY2">
         </tr>                                                                 
          <tr>
        <td nowrap>Check connection</td>
        <td><select class="input" name="ppp_ping2">
            <option value="on" $PING2 >Yes&nbsp;</option>
            <option value="off" $NPING2>No&nbsp;</option>
        </select></td>
          </tr>
          <tr>
             <td nowrap>Ping IP Address(es)</td>
            <td><input class="input" maxlength="100" name="ppp_ping_ipaddr2" value="$PPP_PING_IPADDR2"></td>
          </tr>
          <tr>
        <td nowrap>Ping Interval (min)</td>
        <td><input class="input" maxlength="15" name="ppp_ping_intvl2" value="$PPP_PING_INTVL2"></td>
          </tr>
          <tr>
        <td nowrap>Ping Repeat Interval (min)</td>
        <td><input class="input" maxlength="15" name="ppp_ping_repeat_intvl2" value="$PPP_PING_REPEAT_INTVL2"></td>
          </tr>
          <tr>
        <td nowrap>Allow failures</td>
        <td><input class="input" maxlength="3" name="ppp_ping_count2" value="$PPP_PING_COUNT2"></td>  
          </tr>
              <tr>
            <td nowrap> </td>
              </tr>
            </table>
        </td>
        </tr>
        </table>
      </td>
    </tr>
    <tr>
      <td>
        <table cellspacing="0" cellpadding="5" border="0">
          <tr>

        <td>
        <table><tr>
        <td nowrap width="160"><input type="checkbox" name="ppp_switch" $SWITCH>
        Switch SIM after</td><td><input size="15" name="ppp_maxfail" value="$PPP_MAXFAIL"> failed attempts</td>
          </tr>
          <tr>
        <td nowrap width="160"><input type="checkbox" name="ppp_tryprimary" $TRYPRIMARY>
        Try primary SIM after</td><td><input size="15" name="ppp_retry" value="$PPP_RETRY"> minutes</td>
          </tr>
          <tr>
        <td nowrap width="160"><input type="checkbox" name="ppp_reboot" $REBOOT>
        Reboot after </td><td><input size="15" name="ppp_reboot_count" value="$PPP_REBOOT_COUNT"> failed registration attempts</td>
        </tr></table>
        </td>
        <td valign="top">
        <table><tr>
        <td nowrap><input type="checkbox" name="ppp_persist" $PERSIST>
        Number of soft retries</td><td><input size="15" name="ppp_softretr" value="$PPP_SOFTRETR"></td>
        </tr></table>
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
      document.input.simcard.focus();
      //-->
      </script>
EOF

cat include/end.inc

