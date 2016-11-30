#!/bin/sh

[ -e /mnt/rwfs/settings/settings.wifi ] && . /mnt/rwfs/settings/settings.wifi

[ "$WIFI_DHCP_ENABLED" = "1" ] && DHCP="checked"
[ "$WIFI_DHCP_STATIC" = "1" ] && STATIC="checked"
[ -z "$WIFI_DHCP_DEF" ] && WIFI_DHCP_DEF=3600
[ -z "$WIFI_DHCP_MAX" ] && WIFI_DHCP_MAX=86400

[ "$WIFI_MODE" = "DISABLED" ] && wifi_mode_selected_disabled=selected
[ "$WIFI_MODE" = "AP" ] && wifi_mode_selected_ap=selected
[ "$WIFI_MODE" = "CLIENT" ] && wifi_mode_selected_client=selected
[ "$WIFI_MODE" = "AUTO" ] && wifi_mode_selected_auto=selected
[ "$WIFI_AP_AUTH" = "WPA" ] && wifi_ap_auth_wpa=selected
[ "$WIFI_AP_AUTH" = "WPA2" ] && wifi_ap_auth_wpa2=selected
[ "$WIFI_CLIENT_AUTH" = "WPA" ] && wifi_client_auth_wpa=selected
[ "$WIFI_CLIENT_AUTH" = "WPA2" ] && wifi_client_auth_wpa2=selected

./begin $0

echo "</td><td colspan=\"3\" valign=\"top\">"

cat << EOF

      <script language="JavaScript" type="text/javascript">
      <!--
      function Focus(obj) {
    obj.focus(); obj.select();
      }
      function GetValue(obj) {
    return obj.value.replace(/\s/g, '');
      }
      function IsValidIP(obj, zero) {
    var str = GetValue(obj);
    if (zero && str.length == 0) {
      return true;
    }
    var fields = str.match(/^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$/);
    if (fields != null) {
      var tmp = fields[1] | fields[2] | fields[3] | fields[4];
      return (tmp < 256) && (zero || tmp > 0);
    } else {
      return false;
    }
      }

      function IsValidMAC(obj, zero) {
        var str = GetValue(obj);
        if (zero && str.length == 0) {
            return true;
        }
        re = /((\d|([a-f]|[A-F])){2}:){5}(\d|([a-f]|[A-F])){2}/;
        if (re.test(obj.value)) {
            return true;
        } else {
            return false;
        }
      }

      function IsValidTime(obj, zero) {
        var str = GetValue(obj);
        if (zero && str.length == 0) {
            return true;
        }
        if (str.length > 0 && str.length < 9) {
            if (parseInt(str) >= 0) {
                return true;
            }
        }
        return false;
      }



      function CheckForm() {
    var dhcp_enabled = document.input.dhcp_enabled.checked;

    if (!IsValidIP(document.input.wifi_ipaddr, false)) {
      alert("Invalid or missing IP address.");
      Focus(document.input.wifi_ipaddr);
      return false;
    }
    if (!IsValidIP(document.input.wifi_netmask, false)) {
      alert("Invalid or missing subnet mask.");
      Focus(document.input.wifi_netmask);
      return false;
    }
    if (!IsValidIP(document.input.dhcp_pool_lo, !dhcp_enabled)) {
      alert("Invalid or missing IP pool start.");
      Focus(document.input.dhcp_pool_lo);
      return false;
    }
    if (!IsValidIP(document.input.dhcp_pool_hi, !dhcp_enabled)) {
      alert("Invalid or missing IP pool end.");
      Focus(document.input.dhcp_pool_hi);
      return false;
    }
    if (!IsValidTime(document.input.dhcp_def)) {
        alert("Invalid default lease time");
        Focus(document.input.dhcp_def);
        return false;
    }
    if (!IsValidTime(document.input.dhcp_max)) {
        alert("Invalid maximum lease time");
        Focus(document.input.dhcp_max);
        return false;
    }

    for (i=1;i<=5;i=i+1)
    {
        mac_name = eval("document.input.dhcp_mac"+i);
        ip_name = eval("document.input.dhcp_ip"+i);
        if (!IsValidMAC(mac_name, true)) {
            alert("Invalid MAC address "+i);
            Focus(mac_name);
            return false;
        }
       if (!IsValidIP(ip_name, true)) {
            alert("Invalid IP address "+i);
            Focus(ip_name);
            return false;
        }

    }
    return true;
      }
      //-->
      </script>
      <form name="input" onsubmit="return CheckForm();" action="config_wifi_set.cgi" method="post">

<table width="100%" cellspacing="0" cellpadding="3" border="3">
 <tr><td class="title" align="center"><b>LAN Configuration</b></td></tr>
 <tr><td align="center">

<table width="100%"><!-- page content table -->
<tr><td align="center">
<!-- page content, row 1 -->
  <table width="100%"><!-- wifi table -->
  <tr><td align="center" class="menu">Local WiFi Interface</td></tr>
  <tr><td>
        <table width="100%"><!-- wifi inner table -->
        <tr><td width="32%"><table>
          <tr><td nowrap>IP Address</td> <td><input class="input" name="wifi_ipaddr" value="$WIFI_IPADDR"></td></tr>
          <tr><td nowrap>Subnet Mask</td><td><input class="input" name="wifi_netmask" value="$WIFI_NETMASK"></td></tr>
          </table></td>
        <td width="2%" rowspan="3">&nbsp;</td>
        <td width="32%"><table>
          <tr>
            <td nowrap>WiFi Mode</td>
            <td>
              <select name="wifi_mode">
                <option value="DISABLED" $wifi_mode_selected_disabled>Disabled</option>
                <option value="AP" $wifi_mode_selected_ap>Access Point</option>
                <option value="CLIENT" $wifi_mode_selected_client>Client</option>
                <option value="AUTO" $wifi_mode_selected_auto>Auto</option>
              </select>
            </td>
          </tr>
          <tr><td nowrap>AP SSID</td><td><input class="input" name="wifi_ap_ssid" value="$WIFI_AP_SSID"></td></tr>
          <tr><td nowrap>AP Password</td><td><input class="input" name="wifi_ap_pass" value="$WIFI_AP_PASS"></td></tr>
          <tr><td nowrap>AP Authentication</td>
            <td>
              <select name="wifi_ap_auth">
                <option value="WPA" $wifi_ap_auth_wpa>WPA</option>
                <option value="WPA2" $wifi_ap_auth_wpa2>WPA2</option>
              </select>
            </td>
          </tr>

          <tr><td nowrap>Client SSID</td><td><input class="input" name="wifi_client_ssid" value="$WIFI_CLIENT_SSID"></td></tr>
          <tr><td nowrap>Client BSSID</td><td><input class="input" name="wifi_client_bssid" value="$WIFI_CLIENT_BSSID"></td></tr>
          <tr><td nowrap>Client Password</td><td><input class="input" name="wifi_client_pass" value="$WIFI_CLIENT_PASS"></td></tr>
          <tr><td nowrap>Client Authentication</td>
            <td>
              <select name="wifi_client_auth">
                <option value="WPA" $wifi_client_auth_wpa>WPA</option>
                <option value="WPA2" $wifi_client_auth_wpa2>WPA2</option>
              </select>
            </td>
          </tr>

          </table></td>
</tr>
        </table> <!-- wifi inner table -->
  </td></tr>
  <tr><td colspan="3">&nbsp;</td></tr>
  </table> <!-- wifi table -->
</td></tr>
<!-- page content, row 2 -->
<tr><td>
<table width="100%"><!-- dhcp inner table -->
  <tr><td colspan="2" align="center" class="menu">DHCP Server</td></tr>
  <tr><td colspan="2"><input type="checkbox" name="dhcp_enabled" $DHCP>&nbsp;Enable DHCP server</td></tr>
  <tr><td width="50%">
    <table>
      <tr><td nowrap>IP Pool Start</td><td><input class="input" name="dhcp_pool_lo" value="$WIFI_DHCP_POOL_LO"></td></tr>
      <tr><td nowrap>IP Pool End</td><td><input class="input" name="dhcp_pool_hi" value="$WIFI_DHCP_POOL_HI"></td></tr>
    </table></td>
    <td width="50%"><table>
      <tr><td nowrap>Default Lease Time</td><td><input class="input" name="dhcp_def" value="$WIFI_DHCP_DEF"> sec</td></tr>
      <tr><td nowrap>Maximum Lease Time</td><td><input class="input" name="dhcp_max" value="$WIFI_DHCP_MAX"> sec</td></tr>
    </table></td>
  </tr><tr>
    <td colspan="2">
      <table>
        <tr><td colspan="4"><input type="checkbox" name="dhcp_static" $STATIC>&nbsp;Enable static addresses</td></tr>
        <tr>
            <td>#</td>
            <td>Host name</td>
            <td>MAC address</td>
            <td>IP address</td>
        </tr>
        <tr>
            <td>1</td>
            <td><input class="input" name="dhcp_name1" value="$WIFI_DHCP_NAME1"></td>
            <td><input class="input" name="dhcp_mac1" value="$WIFI_DHCP_MAC1"></td>
            <td><input class="input" name="dhcp_ip1" value="$WIFI_DHCP_IP1" ></td>
        </tr>
        <tr>
            <td>2</td>
            <td><input class="input" name="dhcp_name2" value="$WIFI_DHCP_NAME2"></td>
            <td><input class="input" name="dhcp_mac2" value="$WIFI_DHCP_MAC2"></td>
            <td><input class="input" name="dhcp_ip2" value="$WIFI_DHCP_IP2" ></td>
        </tr>
        <tr>
            <td>3</td>
            <td><input class="input" name="dhcp_name3" value="$WIFI_DHCP_NAME3"></td>
            <td><input class="input" name="dhcp_mac3" value="$WIFI_DHCP_MAC3"></td>
            <td><input class="input" name="dhcp_ip3" value="$WIFI_DHCP_IP3" ></td>
        </tr>
        <tr>
            <td>4</td>
            <td><input class="input" name="dhcp_name4" value="$WIFI_DHCP_NAME4"></td>
            <td><input class="input" name="dhcp_mac4" value="$WIFI_DHCP_MAC4"></td>
            <td><input class="input" name="dhcp_ip4" value="$WIFI_DHCP_IP4" ></td>
        </tr>
        <tr>
            <td>5</td>
            <td><input class="input" name="dhcp_name5" value="$WIFI_DHCP_NAME5"></td>
            <td><input class="input" name="dhcp_mac5" value="$WIFI_DHCP_MAC5"></td>
            <td><input class="input" name="dhcp_ip5" value="$WIFI_DHCP_IP5" ></td>
        </tr>
      </table>
    </td>
  </tr>
</table><!-- dhcp inner table -->
</tr>
</table>
<!-- page content table -->
</td></tr>
<tr><td><input type="submit" name="apply" value="Apply"></td> </tr>
</table>
      </form>
      <script language="JavaScript" type="text/javascript">
      <!--
      document.input.wifi_ipaddr.focus();
      //-->
      </script>
EOF

cat include/end.inc
