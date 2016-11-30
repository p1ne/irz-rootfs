#!/bin/sh

[ -e /mnt/rwfs/settings/settings.eth ] && . /mnt/rwfs/settings/settings.eth

#[ "$ETH_SECONDARY" = "1" ] && IP2="checked"
[ "$ETH_DHCP_ENABLED" = "1" ] && DHCP="checked"
[ "$ETH_DHCP_STATIC" = "1" ] && STATIC="checked"
[ -z "$ETH_DHCP_DEF" ] && ETH_DHCP_DEF=3600
[ -z "$ETH_DHCP_MAX" ] && ETH_DHCP_MAX=86400

[ "$ETH_MII_FORCE" = "1" ] && FORCE="checked"

[ "$ETH_RESERVE" = "1" ] && RESERVE="checked"
[ "$ETH_USB_LAN" = "1" ] && USB_LAN="checked"
[ "$ETH_SECONDARY" = "1" ] && SECONDARY="checked"

if [ "$ETH_MII_MEDIA" = "100BaseTx" ]; then
    media_selected1="selected"
    media_selected2=""
else
    media_selected1=""
    media_selected2="selected"
fi

if [ "$ETH_MII_DUPLEX" = "FD" ]; then
    duplex_selected1="selected"
    duplex_selected2=""
else
    duplex_selected1=""
    duplex_selected2="selected"
fi

if [ "$ETH_RESERVE_PPPON" = "1" ]; then
    pppon="selected"
else
    pppoff="selected"
fi

case ${ETH_RESERVE_IFACE} in
    eth0) eth0="selected" ;;
    'eth0:0') eth00="selected" ;;
    eth1) eth1="selected" ;;
esac

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
    var sec_enabled = document.input.eth_secondary.checked;
    var res_enabled = document.input.eth_reserve.checked;
    var usb_enabled = document.input.usb_lan.checked;

    if (!IsValidIP(document.input.eth_ipaddr, false)) {
      alert("Invalid or missing IP address.");
      Focus(document.input.eth_ipaddr);
      return false;
    }
    if (!IsValidIP(document.input.eth_netmask, false)) {
      alert("Invalid or missing subnet mask.");
      Focus(document.input.eth_netmask);
      return false;
    }
    if (!IsValidIP(document.input.eth_ipaddr2, !sec_enabled)) {
      alert("Invalid or missing secondary IP address.");
      Focus(document.input.eth_ipaddr2);
      return false;
    }
    if (!IsValidIP(document.input.eth_netmask2, !sec_enabled)) {
      alert("Invalid or missing secondary subnet mask.");
      Focus(document.input.eth_netmask2);
      return false;
    }
    if (!IsValidIP(document.input.eth_ipaddr3, !usb_enabled)) {
      alert("Invalid or missing USB-LAN IP address.");
      Focus(document.input.eth_ipaddr3);
      return false;
    }
    if (!IsValidIP(document.input.eth_netmask3, !usb_enabled)) {
      alert("Invalid or missing USB-LAN subnet mask.");
      Focus(document.input.eth_netmask3);
      return false;
    }
    if (!IsValidIP(document.input.eth_reserve_router, !res_enabled)) {
      alert("Invalid or missing reserve router IP address.");
      Focus(document.input.eth_reserve_router);
      return false;
    }
    if (!IsValidIP(document.input.eth_reserve_target, !res_enabled)) {
      alert("Invalid or missing reserve ping IP address.");
      Focus(document.input.eth_reserve_target);
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
      <form name="input" onsubmit="return CheckForm();" action="config_eth_set.cgi" method="post">

<table width="100%" cellspacing="0" cellpadding="3" border="3">
 <tr><td class="title" align="center"><b>LAN Configuration</b></td></tr>
 <tr><td align="center">

<table width="100%"><!-- page content table -->
<tr><td align="center">
<!-- page content, row 1 -->
  <table width="100%"><!-- eth table -->
  <tr><td align="center" class="menu">Local Ethernet Interface</td></tr>
  <tr><td>
        <table width="100%"><!-- eth inner table -->
        <tr><td width="32%"><table>
          <tr><td colspan="2">Primary IP Address:</td></tr>
          <tr><td nowrap>IP Address</td> <td><input class="input" name="eth_ipaddr" value="$ETH_IPADDR"></td></tr>
          <tr><td nowrap>Subnet Mask</td><td><input class="input" name="eth_netmask" value="$ETH_NETMASK"></td></tr>
          </table></td>
        <td width="2%" rowspan="3">&nbsp;</td>
        <td width="32%"><table>
          <tr><td colspan="2"><input type="checkbox" name="eth_secondary" $SECONDARY>&nbsp;Secondary IP address:</td></tr>
          <tr><td nowrap>Secondary IP</td><td><input class="input" name="eth_ipaddr2" value="$ETH_IPADDR2"></td></tr>
          <tr><td nowrap>Secondary Mask</td><td><input class="input" name="eth_netmask2" value="$ETH_NETMASK2"></td></tr>
          </table></td>
        <td width="2%" rowspan="3">&nbsp;</td>
        <td width="32%"><table>
         <tr><td nowrap colspan="2"><input type="checkbox" name="eth_force_media" $FORCE>&nbsp;Force media type&nbsp;               </td></tr>
         <tr><td nowrap>Media type&nbsp;</td>
           <td><select name="eth_force_media_type">
             <option value="100BaseTx" $media_selected1>100BaseTx</option>
             <option value="10BaseT" $media_selected2>10BaseT</option>
             </select></td></tr>
         <tr><td nowrap>Duplex type&nbsp;</td>
           <td><select name="eth_force_media_duplex">
             <option value="FD" $duplex_selected1>Full duplex</option>
             <option value="HD" $duplex_selected2>Half duplex</option>
             </select></td></tr>
             </table>
         </td></tr>
        </table> <!-- eth inner table -->
  </td></tr>
  <tr><td colspan="3">&nbsp;</td></tr>
  </table> <!-- eth table -->
</td></tr>
<!-- page content, row 2 -->
<tr><td>
<table width="100%"> <!-- row 2 inner table -->
<tr><td width="47%" align="center" class="menu">USB Ethernet Interface</td>
  <td width="6%">&nbsp;</td>
  <td width="47%" align="center" class="menu">Reserve Link</td></tr>
<tr><td valign="top">
 <table width="100%"><!-- USB-LAN table -->
    <tr><td colspan="2"><input type="checkbox" name="usb_lan" $USB_LAN>&nbsp;USB-LAN IP address:</td></tr>
    <tr><td nowrap>USB-LAN IP</td><td><input class="input" name="eth_ipaddr3" value="$ETH_IPADDR3"></td></tr>
    <tr><td nowrap>USB-LAN Mask</td><td><input class="input" name="eth_netmask3" value="$ETH_NETMASK3"></td></tr>
    </table><!-- USB-LAN table -->
 </td>
<td>&nbsp;</td>
<td valign="top">
        <table width="100%"><!-- reserve link table -->
            <tr>
                <td colspan="2">
                    <input type="checkbox" name="eth_reserve" $RESERVE>&nbsp;Activate reserve link mode&nbsp;
                </td>
            </tr>
            <tr>
                <td>Main router IP&nbsp;</td>
                <td><input type="input" name="eth_reserve_router" value="$ETH_RESERVE_ROUTER"></td>
            </tr>
            <tr>
                <td>IP address to ping&nbsp;</td>
                <td><input type="input" name="eth_reserve_target" value="$ETH_RESERVE_TARGET"></td>
          </tr>
        <tr>
        <td>Main interface</td>
        <td>
            <select type="input" name="eth_reserve_iface">
EOF
for i in `ifconfig -a | grep eth | awk '{print $1}' | tr '\n' ' '`
do
    case $i in
        eth0) selected=$eth0 ;;
        'eth0:0') selected=$eth00 ;;
        eth1) selected=$eth1 ;;
    esac
    echo "<option value=\"$i\" $selected >$i</option>"
done;
cat << EOF
            </select>
            </td>
        </tr><tr>
            <td>PPP link mode&nbsp;</td>
            <td><select type="input" name=eth_reserve_pppon>
                <option value="0" $pppoff>Disconnect when not used</option>
                <option value="1" $pppon>Always connected</option>
            </select></td>
        </tr>
        </table><!-- reserve link table -->
</td></tr><tr><td colspan="3">&nbsp;</td></tr></table> <!-- inner table -->
  </td>
 </tr>
<!-- page content, row 3 -->
<tr><td>
<table width="100%"><!-- dhcp inner table -->
  <tr><td colspan="2" align="center" class="menu">DHCP Server</td></tr>
  <tr><td colspan="2"><input type="checkbox" name="dhcp_enabled" $DHCP>&nbsp;Enable DHCP server</td></tr>
  <tr><td width="50%">
    <table>
      <tr><td nowrap>IP Pool Start</td><td><input class="input" name="dhcp_pool_lo" value="$ETH_DHCP_POOL_LO"></td></tr>
      <tr><td nowrap>IP Pool End</td><td><input class="input" name="dhcp_pool_hi" value="$ETH_DHCP_POOL_HI"></td></tr>
    </table></td>
    <td width="50%"><table>
      <tr><td nowrap>Default Lease Time</td><td><input class="input" name="dhcp_def" value="$ETH_DHCP_DEF"> sec</td></tr>
      <tr><td nowrap>Maximum Lease Time</td><td><input class="input" name="dhcp_max" value="$ETH_DHCP_MAX"> sec</td></tr>
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
            <td><input class="input" name="dhcp_name1" value="$ETH_DHCP_NAME1"></td>
            <td><input class="input" name="dhcp_mac1" value="$ETH_DHCP_MAC1"></td>
            <td><input class="input" name="dhcp_ip1" value="$ETH_DHCP_IP1" ></td>
        </tr>
        <tr>
            <td>2</td>
            <td><input class="input" name="dhcp_name2" value="$ETH_DHCP_NAME2"></td>
            <td><input class="input" name="dhcp_mac2" value="$ETH_DHCP_MAC2"></td>
            <td><input class="input" name="dhcp_ip2" value="$ETH_DHCP_IP2" ></td>
        </tr>
        <tr>
            <td>3</td>
            <td><input class="input" name="dhcp_name3" value="$ETH_DHCP_NAME3"></td>
            <td><input class="input" name="dhcp_mac3" value="$ETH_DHCP_MAC3"></td>
            <td><input class="input" name="dhcp_ip3" value="$ETH_DHCP_IP3" ></td>
        </tr>
        <tr>
            <td>4</td>
            <td><input class="input" name="dhcp_name4" value="$ETH_DHCP_NAME4"></td>
            <td><input class="input" name="dhcp_mac4" value="$ETH_DHCP_MAC4"></td>
            <td><input class="input" name="dhcp_ip4" value="$ETH_DHCP_IP4" ></td>
        </tr>
        <tr>
            <td>5</td>
            <td><input class="input" name="dhcp_name5" value="$ETH_DHCP_NAME5"></td>
            <td><input class="input" name="dhcp_mac5" value="$ETH_DHCP_MAC5"></td>
            <td><input class="input" name="dhcp_ip5" value="$ETH_DHCP_IP5" ></td>
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
      document.input.eth_ipaddr.focus();
      //-->
      </script>
EOF

cat include/end.inc

