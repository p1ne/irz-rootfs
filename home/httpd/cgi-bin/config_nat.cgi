#!/bin/sh

[ -e /mnt/rwfs/settings/settings.nat ] && . /mnt/rwfs/settings/settings.nat

[ "$NAT_DISABLE_MASQ" = "1" ] && MASQ="checked"
[ "$NAT_DEFAULT_ENABLED" = "1" ] && DEFAULT="checked"
[ "$NAT_UPNP_ENABLED" = "1" ] && UPNP="checked"
for i in `seq 1 10`; do
	eval val="$"NAT_PORT${i}_TYPE
	case $val in
	tcp)
		eval var=PORT${i}T
		eval $var="selected"	
	;;
	udp)
        eval var=PORT${i}U
        eval $var="selected" 
	;;
	icmp)
        eval var=PORT${i}I
        eval $var="selected" 
	;;
	*)
        eval var=PORT${i}TU
        eval $var="selected" 
	;;
	esac

done

./begin $0

echo "</td><td colspan=\"3\" valign=\"top\">"
cat include/js.inc
cat << EOF
      function CheckForm() {
	if (!IsValidIP(document.input.nat_port1_ipaddr, true)) {
	  alert("Invalid 1. server IP address.");
	  Focus(document.input.nat_port1_ipaddr);
	  return false;
	}
	if (!IsValidIP(document.input.nat_port2_ipaddr, true)) {
	  alert("Invalid 2. server IP address.");
	  Focus(document.input.nat_port2_ipaddr);
	  return false;
	}
	if (!IsValidIP(document.input.nat_port3_ipaddr, true)) {
	  alert("Invalid 3. server IP address.");
	  Focus(document.input.nat_port3_ipaddr);
	  return false;
	}
	if (!IsValidIP(document.input.nat_port4_ipaddr, true)) {
	  alert("Invalid 4. server IP address.");
	  Focus(document.input.nat_port4_ipaddr);
	  return false;
	}
	if (!IsValidIP(document.input.nat_port5_ipaddr, true)) {
	  alert("Invalid 5. server IP address.");
	  Focus(document.input.nat_port5_ipaddr);
	  return false;
	}
	if (!IsValidIP(document.input.nat_port6_ipaddr, true)) {
	  alert("Invalid 6. server IP address.");
	  Focus(document.input.nat_port6_ipaddr);
	  return false;
	}
	if (!IsValidIP(document.input.nat_port7_ipaddr, true)) {
	  alert("Invalid 7. server IP address.");
	  Focus(document.input.nat_port7_ipaddr);
	  return false;
	}
	if (!IsValidIP(document.input.nat_port8_ipaddr, true)) {
	  alert("Invalid 8. server IP address.");
	  Focus(document.input.nat_port8_ipaddr);
	  return false;
	}
    if (!IsValidIP(document.input.nat_port9_ipaddr, true)) {
      alert("Invalid 9. server IP address.");
      Focus(document.input.nat_port9_ipaddr);
      return false;
    }
    if (!IsValidIP(document.input.nat_port10_ipaddr, true)) {
      alert("Invalid 10. server IP address.");
      Focus(document.input.nat_port10_ipaddr);
      return false;
    }

	if (!IsValidIP(document.input.nat_default_ipaddr, !document.input.nat_default_enabled.checked)) {
	  alert("Invalid or missing default server IP address.");
	  Focus(document.input.nat_default_ipaddr);
	  return false;
	}
	return true;
      }
      //-->
      </script>
      <form name="input" onsubmit="return CheckForm();" action="config_nat_set.cgi" method="post">
      <table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
	  <td class="title" align="center">
	    <b>Port Forwarding</b>
	  </td>
	</tr>
	<tr>
	  <td>
	    <table>
	      <tr>
		<td>#</td>
		<td>Public Port</td>
		<td>Private Port</td>
		<td>Type</td>
		<td>Server IP Address</td>
	      </tr>
	      <tr>
		<td>1</td>
		<td><input name="nat_port1_public" size="8" maxlength="5" value="$NAT_PORT1_PUBLIC"></td>
		<td><input name="nat_port1_private" size="8" maxlength="5" value="$NAT_PORT1_PRIVATE"></td>
		<td><select name="nat_port1_type"><option value="tcp" $PORT1T>TCP<option value="udp" $PORT1U>UDP
			<option value="icmp" $PORT1I>ICMP<option value="tcpudp" $PORT1TU>TCP/UDP</select></td>
		<td><input name="nat_port1_ipaddr" value="$NAT_PORT1_IPADDR"></td>
	      </tr>
	      <tr>
		<td>2</td>
		<td><input name="nat_port2_public" size="8" maxlength="5" value="$NAT_PORT2_PUBLIC"></td>
		<td><input name="nat_port2_private" size="8" maxlength="5" value="$NAT_PORT2_PRIVATE"></td>
        <td><select name="nat_port2_type"><option value="tcp" $PORT2T>TCP<option value="udp" $PORT2U>UDP
			<option value="icmp" $PORT2I>ICMP<option value="tcpudp" $PORT2TU>TCP/UDP</select></td>
		<td><input name="nat_port2_ipaddr" value="$NAT_PORT2_IPADDR"></td>
	      </tr>
	      <tr>
        <td>3</td>
		<td><input name="nat_port3_public" size="8" maxlength="5" value="$NAT_PORT3_PUBLIC"></td>
		<td><input name="nat_port3_private" size="8" maxlength="5" value="$NAT_PORT3_PRIVATE"></td>
		<td><select name="nat_port3_type"><option value="tcp" $PORT3T>TCP<option value="udp" $PORT3U>UDP
			<option value="icmp" $PORT3I>ICMP<option value="tcpudp" $PORT3TU>TCP/UDP</select></td>
		<td><input name="nat_port3_ipaddr" value="$NAT_PORT3_IPADDR"></td>
	      </tr>
	      <tr>
        <td>4</td>
		<td><input name="nat_port4_public" size="8" maxlength="5" value="$NAT_PORT4_PUBLIC"></td>
		<td><input name="nat_port4_private" size="8" maxlength="5" value="$NAT_PORT4_PRIVATE"></td>
        <td><select name="nat_port4_type"><option value="tcp" $PORT4T>TCP<option value="udp" $PORT4U>UDP
            <option value="icmp" $PORT4I>ICMP<option value="tcpudp" $PORT4TU>TCP/UDP</select></td>
		<td><input name="nat_port4_ipaddr" value="$NAT_PORT4_IPADDR"></td>
	      </tr>
	      <tr>
        <td>5</td>
		<td><input name="nat_port5_public" size="8" maxlength="5" value="$NAT_PORT5_PUBLIC"></td>
		<td><input name="nat_port5_private" size="8" maxlength="5" value="$NAT_PORT5_PRIVATE"></td>
        <td><select name="nat_port5_type"><option value="tcp" $PORT5T>TCP<option value="udp" $PORT5U>UDP
            <option value="icmp" $PORT5I>ICMP<option value="tcpudp" $PORT5TU>TCP/UDP</select></td>
		<td><input name="nat_port5_ipaddr" value="$NAT_PORT5_IPADDR"></td>
	      </tr>
	      <tr>
        <td>6</td>
		<td><input name="nat_port6_public" size="8" maxlength="5" value="$NAT_PORT6_PUBLIC"></td>
		<td><input name="nat_port6_private" size="8" maxlength="5" value="$NAT_PORT6_PRIVATE"></td>
        <td><select name="nat_port6_type"><option value="tcp" $PORT6T>TCP<option value="udp" $PORT6U>UDP
            <option value="icmp" $PORT6I>ICMP<option value="tcpudp" $PORT6TU>TCP/UDP</select></td>
		<td><input name="nat_port6_ipaddr" value="$NAT_PORT6_IPADDR"></td>
	      </tr>
	      <tr>
        <td>7</td>
		<td><input name="nat_port7_public" size="8" maxlength="5" value="$NAT_PORT7_PUBLIC"></td>
		<td><input name="nat_port7_private" size="8" maxlength="5" value="$NAT_PORT7_PRIVATE"></td>
        <td><select name="nat_port7_type"><option value="tcp" $PORT7T>TCP<option value="udp" $PORT7U>UDP
            <option value="icmp" $PORT7I>ICMP<option value="tcpudp" $PORT7TU>TCP/UDP</select></td>
		<td><input name="nat_port7_ipaddr" value="$NAT_PORT7_IPADDR"></td>
	      </tr>
	      <tr>
        <td>8</td>
		<td><input name="nat_port8_public" size="8" maxlength="5" value="$NAT_PORT8_PUBLIC"></td>
		<td><input name="nat_port8_private" size="8" maxlength="5" value="$NAT_PORT8_PRIVATE"></td>
        <td><select name="nat_port8_type"><option value="tcp" $PORT8T>TCP<option value="udp" $PORT8U>UDP
            <option value="icmp" $PORT8I>ICMP<option value="tcpudp" $PORT8TU>TCP/UDP</select></td>
		<td><input name="nat_port8_ipaddr" value="$NAT_PORT8_IPADDR"></td>
	      </tr>
          <tr>
        <td>9</td>
        <td><input name="nat_port9_public" size="8" maxlength="5" value="$NAT_PORT9_PUBLIC"></td>
        <td><input name="nat_port9_private" size="8" maxlength="5" value="$NAT_PORT9_PRIVATE"></td>
        <td><select name="nat_port9_type"><option value="tcp" $PORT9T>TCP<option value="udp" $PORT9U>UDP
            <option value="icmp" $PORT9I>ICMP<option value="tcpudp" $PORT9TU>TCP/UDP</select></td>
        <td><input name="nat_port9_ipaddr" value="$NAT_PORT9_IPADDR"></td>
          </tr>
          <tr>
        <td>10</td>
        <td><input name="nat_port10_public" size="8" maxlength="5" value="$NAT_PORT10_PUBLIC"></td>
        <td><input name="nat_port10_private" size="8" maxlength="5" value="$NAT_PORT10_PRIVATE"></td>
        <td><select name="nat_port10_type"><option value="tcp" $PORT10T>TCP<option value="udp" $PORT10U>UDP
            <option value="icmp" $PORT10I>ICMP<option value="tcpudp" $PORT10TU>TCP/UDP</select></td>
        <td><input name="nat_port10_ipaddr" value="$NAT_PORT10_IPADDR"></td>
          </tr>
	    </table>
	  </td>
	</tr>
	<tr>
	  <td>
	    <table>
	      <tr>
		<td nowrap><input type="checkbox" name="nat_default_enabled" $DEFAULT>&nbsp;
		Send all remaining incoming packets to default server</td>
	      </tr>
	      <tr>
		<td nowrap>Default Server IP Address&nbsp;
		<input name="nat_default_ipaddr" value="$NAT_DEFAULT_IPADDR"></td>
	      </tr>
          <tr>
        <td nowrap><input type="checkbox" name="nat_upnp_enabled" $UPNP>&nbsp;
        Enable UPnP/NAT-PMP </td>
          </tr>
	    </table>
	  </td>
	</tr>
	<tr>
		<td>
			<table>
	     <tr>
        <td><input type="checkbox" name="nat_disable_masq" $MASQ></td>
        <td nowrap>Do not masquerade outgoing traffic&nbsp;</td>
        <td>(use with caution)</td>
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
      document.input.nat_port1_public.focus();
      //-->
      </script>
EOF

cat include/end.inc

