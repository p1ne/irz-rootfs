#!/bin/sh

CONF=/mnt/rwfs/settings/settings.static
[ -f $CONF ] && . $CONF

for i in `seq 10`; do
	eval val="$"STATIC_DEVICE${i}
	case $val in
	eth0)
		eval var=ETH0_${i}
		eval $var="selected"	
	;;
	ppp0)
        eval var=PPP0_${i}
        eval $var="selected" 
	;;
	eth00)
        eval var=ETH00_${i}
        eval $var="selected" 
	;;
    eth1)
        eval var=ETH1_${i}
        eval $var="selected"
        ;;
    gre0)
        eval var=GRE0_${i}
        eval $var="selected"
    ;;
    gre1)
        eval var=GRE1_${i}
        eval $var="selected"
    ;;
    gre2)
        eval var=GRE2_${i}
        eval $var="selected"
    ;;
    gre3)
        eval var=GRE3_${i}
        eval $var="selected"
    ;;
    gre4)
        eval var=GRE4_${i}
        eval $var="selected"
        ;;
    gre5)
        eval var=GRE5_${i}
        eval $var="selected"
    ;;
    gre6)
        eval var=GRE6_${i}
        eval $var="selected"
    ;;
    gre7)
        eval var=GRE7_${i}
        eval $var="selected"
    ;;
    
    gre8)
        eval var=GRE8_${i}
        eval $var="selected"
    ;;
    
    gre9)
        eval var=GRE9_${i}
        eval $var="selected"
    ;;
    gre10)
        eval var=GRE10_${i}
        eval $var="selected"
    ;;
	*)
        eval var=ANY_${i}
        eval $var="selected" 
	;;
	esac
done

./begin $0

echo "</td><td colspan=\"3\" valign=\"top\">"
cat include/js.inc
cat << EOF
      function CheckForm() {
    for (i=1;i<=5;i++){
        network = eval("document.input.static_network"+i);
        if (!IsValidIP(network, true)) {
	        alert("Invalid Network "+i);
        	  Focus(network);
        	  return false;
    	}
        netmask = eval("document.input.static_netmask"+i);
    	if (!IsValidIP(netmask, true)) {
        	  alert("Invalid Netmask "+i);
        	  Focus(netmask);
        	  return false;
    	}
        gateway = eval("document.input.static_gateway"+i);
    	if (!IsValidIP(gateway, true)) {
        	  alert("Invalid Gateway "+i);
        	  Focus(gateway);
        	  return false;
    	}
    }
	return true;
      }
      //-->
      </script>
      <form name="input" onsubmit="return CheckForm();" action="config_static_set.cgi" method="post">
      <table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
	  <td class="title" align="center">
	    <b>Static Routes</b>
	  </td>
	</tr>
		<tr>
	  <td>
	    <table>
	      <tr>
		<th>#</th>
		<th>Network</th>
		<th>Netmask</th>
        <th>Gateway</th>
		<th>Interface</th>
	      </tr>

EOF
for i in `seq 5`; do
    eval "static_network=\$STATIC_NETWORK${i}"
    eval "static_netmask=\$STATIC_NETMASK${i}"
    eval "static_gateway=\$STATIC_GATEWAY${i}"
    eval "any=\$ANY_$i"
    eval "eth0=\$ETH0_$i"
    eval "eth00=\$ETH00_$i"
    eval "ppp0=\$PPP0_$i"
    eval "eth1=\$ETH1_$i"
    echo "<tr>"
    echo "	<td>$i</td>"
    echo "	<td><input name=\"static_network${i}\" size=\"15\" maxlength=\"15\" value=\"$static_network\"></td>"
    echo "	<td><input name=\"static_netmask${i}\" size=\"15\" maxlength=\"15\" value=\"$static_netmask\"></td>"
    echo "	<td><input name=\"static_gateway${i}\" value=\"$static_gateway\"></td>"
    echo "	<td><select name=\"static_device${i}\">"
    echo "		<option value=\"\" $any>"
    echo "		<option value=\"eth0\" $eth0>ETH0"
    echo "		<option value=\"ppp0\" $ppp0>PPP0"
    echo "		<option value=\"eth00\" $eth00>ETH0:0"
    echo "		<option value=\"eth1\" $eth1>ETH1"
    for j in `seq 10`; do
    eval "gre=\$GRE${j}_$i"
    echo "		<option value=\"gre${j}\" $gre >GRE${j}"
    done;
    echo "	</select></td>"
    echo "</tr>"
done;
EOF
cat << EOF 
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
      document.input.static_network1.focus();
      //-->
      </script>
EOF

cat include/end.inc

