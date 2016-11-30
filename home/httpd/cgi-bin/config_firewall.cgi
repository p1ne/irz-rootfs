#!/bin/sh

[ -e /mnt/rwfs/settings/settings.fw ] && . /mnt/rwfs/settings/settings.fw

NONE="selected"
[ "$FW_MODE" = "allow" ] && ALLOW="selected" && NONE=""
[ "$FW_MODE" = "disable" ] && DISABLE="selected" && NONE=""


[ "$FW_RULE1_TYPE" = "single" ] && fw_rule1_type_single="selected"
[ "$FW_RULE1_TYPE" = "any" ] && fw_rule1_type_any="selected"
[ "$FW_RULE1_TYPE" = "subnet" ] && fw_rule1_type_subnet="selected"
[ "$FW_RULE1_PROTO" = "all" ] && fw_rule1_proto_all="selected"
[ "$FW_RULE1_PROTO" = "tcp" ] && fw_rule1_proto_tcp="selected"
[ "$FW_RULE1_PROTO" = "udp" ] && fw_rule1_proto_udp="selected"
[ "$FW_RULE1_PROTO" = "icmp" ] && fw_rule1_proto_icmp="selected"

[ "$FW_RULE2_TYPE" = "single" ] && fw_rule2_type_single="selected"
[ "$FW_RULE2_TYPE" = "any" ] && fw_rule2_type_any="selected"
[ "$FW_RULE2_TYPE" = "subnet" ] && fw_rule2_type_subnet="selected"
[ "$FW_RULE2_PROTO" = "all" ] && fw_rule2_proto_all="selected"
[ "$FW_RULE2_PROTO" = "tcp" ] && fw_rule2_proto_tcp="selected"
[ "$FW_RULE2_PROTO" = "udp" ] && fw_rule2_proto_udp="selected"
[ "$FW_RULE2_PROTO" = "icmp" ] && fw_rule2_proto_icmp="selected"

[ "$FW_RULE3_TYPE" = "single" ] && fw_rule3_type_single="selected"
[ "$FW_RULE3_TYPE" = "any" ] && fw_rule3_type_any="selected"
[ "$FW_RULE3_TYPE" = "subnet" ] && fw_rule3_type_subnet="selected"
[ "$FW_RULE3_PROTO" = "all" ] && fw_rule3_proto_all="selected"
[ "$FW_RULE3_PROTO" = "tcp" ] && fw_rule3_proto_tcp="selected"
[ "$FW_RULE3_PROTO" = "udp" ] && fw_rule3_proto_udp="selected"
[ "$FW_RULE3_PROTO" = "icmp" ] && fw_rule3_proto_icmp="selected"

[ "$FW_RULE4_TYPE" = "single" ] && fw_rule4_type_single="selected"
[ "$FW_RULE4_TYPE" = "any" ] && fw_rule4_type_any="selected"
[ "$FW_RULE4_TYPE" = "subnet" ] && fw_rule4_type_subnet="selected"
[ "$FW_RULE4_PROTO" = "all" ] && fw_rule4_proto_all="selected"
[ "$FW_RULE4_PROTO" = "tcp" ] && fw_rule4_proto_tcp="selected"
[ "$FW_RULE4_PROTO" = "udp" ] && fw_rule4_proto_udp="selected"
[ "$FW_RULE4_PROTO" = "icmp" ] && fw_rule4_proto_icmp="selected"

[ "$FW_RULE5_TYPE" = "single" ] && fw_rule5_type_single="selected"
[ "$FW_RULE5_TYPE" = "any" ] && fw_rule5_type_any="selected"
[ "$FW_RULE5_TYPE" = "subnet" ] && fw_rule5_type_subnet="selected"
[ "$FW_RULE5_PROTO" = "all" ] && fw_rule5_proto_all="selected"
[ "$FW_RULE5_PROTO" = "tcp" ] && fw_rule5_proto_tcp="selected"
[ "$FW_RULE5_PROTO" = "udp" ] && fw_rule5_proto_udp="selected"
[ "$FW_RULE5_PROTO" = "icmp" ] && fw_rule5_proto_icmp="selected"

[ "$FW_RULE6_TYPE" = "single" ] && fw_rule6_type_single="selected"
[ "$FW_RULE6_TYPE" = "any" ] && fw_rule6_type_any="selected"
[ "$FW_RULE6_TYPE" = "subnet" ] && fw_rule6_type_subnet="selected"
[ "$FW_RULE6_PROTO" = "all" ] && fw_rule6_proto_all="selected"
[ "$FW_RULE6_PROTO" = "tcp" ] && fw_rule6_proto_tcp="selected"
[ "$FW_RULE6_PROTO" = "udp" ] && fw_rule6_proto_udp="selected"
[ "$FW_RULE6_PROTO" = "icmp" ] && fw_rule6_proto_icmp="selected"

[ "$FW_RULE7_TYPE" = "single" ] && fw_rule7_type_single="selected"
[ "$FW_RULE7_TYPE" = "any" ] && fw_rule7_type_any="selected"
[ "$FW_RULE7_TYPE" = "subnet" ] && fw_rule7_type_subnet="selected"
[ "$FW_RULE7_PROTO" = "all" ] && fw_rule7_proto_all="selected"
[ "$FW_RULE7_PROTO" = "tcp" ] && fw_rule7_proto_tcp="selected"
[ "$FW_RULE7_PROTO" = "udp" ] && fw_rule7_proto_udp="selected"
[ "$FW_RULE7_PROTO" = "icmp" ] && fw_rule7_proto_icmp="selected"

[ "$FW_RULE8_TYPE" = "single" ] && fw_rule8_type_single="selected"
[ "$FW_RULE8_TYPE" = "any" ] && fw_rule8_type_any="selected"
[ "$FW_RULE8_TYPE" = "subnet" ] && fw_rule8_type_subnet="selected"
[ "$FW_RULE8_PROTO" = "all" ] && fw_rule8_proto_all="selected"
[ "$FW_RULE8_PROTO" = "tcp" ] && fw_rule8_proto_tcp="selected"
[ "$FW_RULE8_PROTO" = "udp" ] && fw_rule8_proto_udp="selected"
[ "$FW_RULE8_PROTO" = "icmp" ] && fw_rule8_proto_icmp="selected"

[ "$FW_RULE9_TYPE" = "single" ] && fw_rule9_type_single="selected"
[ "$FW_RULE9_TYPE" = "any" ] && fw_rule9_type_any="selected"
[ "$FW_RULE9_TYPE" = "subnet" ] && fw_rule9_type_subnet="selected"
[ "$FW_RULE9_PROTO" = "all" ] && fw_rule9_proto_all="selected"
[ "$FW_RULE9_PROTO" = "tcp" ] && fw_rule9_proto_tcp="selected"
[ "$FW_RULE9_PROTO" = "udp" ] && fw_rule9_proto_udp="selected"
[ "$FW_RULE9_PROTO" = "icmp" ] && fw_rule9_proto_icmp="selected"

[ "$FW_RULE10_TYPE" = "single" ] && fw_rule10_type_single="selected"
[ "$FW_RULE10_TYPE" = "any" ] && fw_rule10_type_any="selected"
[ "$FW_RULE10_TYPE" = "subnet" ] && fw_rule10_type_subnet="selected"
[ "$FW_RULE10_PROTO" = "all" ] && fw_rule10_proto_all="selected"
[ "$FW_RULE10_PROTO" = "tcp" ] && fw_rule10_proto_tcp="selected"
[ "$FW_RULE10_PROTO" = "udp" ] && fw_rule10_proto_udp="selected"
[ "$FW_RULE10_PROTO" = "icmp" ] && fw_rule10_proto_icmp="selected"

./begin $0

echo "</td><td colspan=\"3\" valign=\"top\">"

cat << EOF
      <script language="JavaScript" type="text/javascript">
      <!--
      function Error(msg, obj) {
	alert(msg); obj.focus(); obj.select(); return false;
      }
      function GetValue(obj) {
	return obj.value.replace(/\s/g, '');
      }
      function IsEmpty(obj) {
	return GetValue(obj).length == 0;
      }
      function IsInRange(obj, low, high, empty) {
	var str = GetValue(obj);
	if (empty && str.length == 0) return true;
	return (parseInt(str) >= low) && (parseInt(str) <= high);
      }
      function IsValidMAC(obj, empty) {
	var str = GetValue(obj);
	if (empty && str.length == 0) return true;
	return str.search(/^[0-9a-fA-F]{1,2}(:[0-9a-fA-F]{1,2}){5}$/) >= 0;
      }
      function IsValidIP(obj, empty) {
	var str = GetValue(obj);
	if (empty && str.length == 0) return true;
	var fields = str.match(/^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$/);
	if (fields != null) {
	  var tmp = fields[1] | fields[2] | fields[3] | fields[4];
	  return (tmp < 256) && (empty || tmp > 0);
	} else {
	  return false;
	}
      }
      function IsValidPort(obj, empty) {
	var str = GetValue(obj);
	if (empty && str.length == 0) return true;
	var value = parseInt(str);
	return (value > 0) && (value < 65536);
      }
      function CheckForm() {
	if (!IsValidIP(document.input.fw_rule1_ipaddr, true)) {
	  return Error("Invalid 1. IP address.", document.input.fw_rule1_ipaddr);
	}
	if (!IsValidIP(document.input.fw_rule2_ipaddr, true)) {
	  return Error("Invalid 2. IP address.", document.input.fw_rule2_ipaddr);
	}
	if (!IsValidIP(document.input.fw_rule3_ipaddr, true)) {
	  return Error("Invalid 3. IP address.", document.input.fw_rule3_ipaddr);
	}
	if (!IsValidIP(document.input.fw_rule4_ipaddr, true)) {
	  return Error("Invalid 4. IP address.", document.input.fw_rule4_ipaddr);
	}
	if (!IsValidIP(document.input.fw_rule5_ipaddr, true)) {
	  return Error("Invalid 5. IP address.", document.input.fw_rule5_ipaddr);
	}
	if (!IsValidIP(document.input.fw_rule6_ipaddr, true)) {
	  return Error("Invalid 6. IP address.", document.input.fw_rule6_ipaddr);
	}
	if (!IsValidIP(document.input.fw_rule7_ipaddr, true)) {
	  return Error("Invalid 7. IP address.", document.input.fw_rule7_ipaddr);
	}
	if (!IsValidIP(document.input.fw_rule8_ipaddr, true)) {
	  return Error("Invalid 8. IP address.", document.input.fw_rule8_ipaddr);
	}
    if (!IsValidIP(document.input.fw_rule9_ipaddr, true)) {
      return Error("Invalid 9. IP address.", document.input.fw_rule9_ipaddr);
    }
    if (!IsValidIP(document.input.fw_rule10_ipaddr, true)) {
      return Error("Invalid 10. IP address.", document.input.fw_rule10_ipaddr);
    }

	return true;
      }
      function SourceChanged(index, clear) {
	var obj = document.input["fw_rule"+index+"_ipaddr"];
	var obj2 = document.input["fw_rule"+index+"_subnet"];
	if (document.input["fw_rule"+index+"_type"].value == "any") {
	  obj.disabled = true; obj.value = "0.0.0.0";
	} else {
	  obj.disabled = false; if (clear) obj.value = "";
	}
	if (document.input["fw_rule"+index+"_type"].value == "subnet") {
		obj2.disabled = false;
	} else {
		obj2.disabled = true;
	}
      }
      function ProtoChanged(index) {
	var obj = document.input["fw_rule"+index+"_port"];
	if (document.input["fw_rule"+index+"_proto"].value == "all") {
	  obj.disabled = true; obj.value = "";
	} else {
	  obj.disabled = false;
	}
      }
      //-->
      </script>
      <form name="input" onsubmit="return CheckForm();" action="config_firewall_set.cgi" method="post">
      <table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
	  <td class="title" align="center">
	    <b>Firewall Configuration</b>
	  </td>
	</tr>
	<tr>
	  <td>
	    <table><tr><td>
			<select name="fw_mode">
				<option value="none" $NONE>Disable firewall</option>
				<option value="allow" $ALLOW>Allow specified, disable others</option>
				<option value="disable" $DISABLE>Disable specified, allow others</option>
			</select>
		</td></tr></table>
	    <table>
	      <tr>
		<th>#</th><th>Type</th><th>IP Address *</th><th>Net Mask *</th><th>Protocol</th><th>Port *</th>
	      </tr>
	      <tr>
			<td align="right">1.</td>
			<td><select name="fw_rule1_type" onChange="SourceChanged(1, true)"><option value="single" $fw_rule1_type_single>single address<option value="any" $fw_rule1_type_any>any address<option value="subnet" $fw_rule1_type_subnet>subnet</select></td>
			<td><input name="fw_rule1_ipaddr" value="$FW_RULE1_IPADDR"></td>
			<td><input name="fw_rule1_subnet" value="$FW_RULE1_SUBNET"></td>
			<td><select name="fw_rule1_proto" onChange="ProtoChanged(1)"><option value="all" $fw_rule1_proto_all>all<option value="tcp" $fw_rule1_proto_tcp>TCP<option value="udp" $fw_rule1_proto_udp>UDP<option value="icmp" $fw_rule1_proto_icmp>ICMP</select></td>
			<td><input name="fw_rule1_port" size="8" maxlength="5" value="$FW_RULE1_PORT"></td>
	      </tr>
          <tr>
			<td align="right">2.</td>
            <td><select name="fw_rule2_type" onChange="SourceChanged(2, true)"><option value="single" $fw_rule2_type_single>single address<option value="any" $fw_rule2_type_any>any address<option value="subnet" $fw_rule2_type_subnet>subnet</select></td>
            <td><input name="fw_rule2_ipaddr" value="$FW_RULE2_IPADDR"></td>
			<td><input name="fw_rule2_subnet" value="$FW_RULE2_SUBNET"></td>
            <td><select name="fw_rule2_proto" onChange="ProtoChanged(2)"><option value="all" $fw_rule2_proto_all>all<option value="tcp" $fw_rule2_proto_tcp>TCP<option value="udp" $fw_rule2_proto_udp>UDP<option value="icmp" $fw_rule2_proto_icmp>ICMP</select></td>
            <td><input name="fw_rule2_port" size="8" maxlength="5" value="$FW_RULE2_PORT"></td>
          </tr>
          <tr>
            <td align="right">3.</td>
            <td><select name="fw_rule3_type" onChange="SourceChanged(3, true)"><option value="single" $fw_rule3_type_single>single address<option value="any" $fw_rule3_type_any>any address<option value="subnet" $fw_rule3_type_subnet>subnet</select></td>
            <td><input name="fw_rule3_ipaddr" value="$FW_RULE3_IPADDR"></td>
            <td><input name="fw_rule3_subnet" value="$FW_RULE3_SUBNET"></td>
            <td><select name="fw_rule3_proto" onChange="ProtoChanged(3)"><option value="all" $fw_rule3_proto_all>all<option value="tcp" $fw_rule3_proto_tcp>TCP<option value="udp" $fw_rule3_proto_udp>UDP<option value="icmp" $fw_rule3_proto_icmp>ICMP</select></td>
            <td><input name="fw_rule3_port" size="8" maxlength="5" value="$FW_RULE3_PORT"></td>
          </tr>
          <tr>
            <td align="right">4.</td>
            <td><select name="fw_rule4_type" onChange="SourceChanged(4, true)"><option value="single" $fw_rule4_type_single>single address<option value="any" $fw_rule4_type_any>any address<option value="subnet" $fw_rule4_type_subnet>subnet</select></td>
            <td><input name="fw_rule4_ipaddr" value="$FW_RULE4_IPADDR"></td>
            <td><input name="fw_rule4_subnet" value="$FW_RULE4_SUBNET"></td>
            <td><select name="fw_rule4_proto" onChange="ProtoChanged(4)"><option value="all" $fw_rule4_proto_all>all<option value="tcp" $fw_rule4_proto_tcp>TCP<option value="udp" $fw_rule4_proto_udp>UDP<option value="icmp" $fw_rule4_proto_icmp>ICMP</select></td>
            <td><input name="fw_rule4_port" size="8" maxlength="5" value="$FW_RULE4_PORT"></td>
          </tr>
          <tr>
            <td align="right">5.</td>
            <td><select name="fw_rule5_type" onChange="SourceChanged(5, true)"><option value="single" $fw_rule5_type_single>single address<option value="any" $fw_rule5_type_any>any address<option value="subnet" $fw_rule5_type_subnet>subnet</select></td>
            <td><input name="fw_rule5_ipaddr" value="$FW_RULE5_IPADDR"></td>
            <td><input name="fw_rule5_subnet" value="$FW_RULE5_SUBNET"></td>
            <td><select name="fw_rule5_proto" onChange="ProtoChanged(5)"><option value="all" $fw_rule5_proto_all>all<option value="tcp" $fw_rule5_proto_tcp>TCP<option value="udp" $fw_rule5_proto_udp>UDP<option value="icmp" $fw_rule5_proto_icmp>ICMP</select></td>
            <td><input name="fw_rule5_port" size="8" maxlength="5" value="$FW_RULE5_PORT"></td>
          </tr>
          <tr>
            <td align="right">6.</td>
            <td><select name="fw_rule6_type" onChange="SourceChanged(6, true)"><option value="single" $fw_rule6_type_single>single address<option value="any" $fw_rule6_type_any>any address<option value="subnet" $fw_rule6_type_subnet>subnet</select></td>
            <td><input name="fw_rule6_ipaddr" value="$FW_RULE6_IPADDR"></td>
            <td><input name="fw_rule6_subnet" value="$FW_RULE6_SUBNET"></td>
            <td><select name="fw_rule6_proto" onChange="ProtoChanged(6)"><option value="all" $fw_rule6_proto_all>all<option value="tcp" $fw_rule6_proto_tcp>TCP<option value="udp" $fw_rule6_proto_udp>UDP<option value="icmp" $fw_rule6_proto_icmp>ICMP</select></td>
            <td><input name="fw_rule6_port" size="8" maxlength="5" value="$FW_RULE6_PORT"></td>
          </tr>
          <tr>
            <td align="right">7.</td>
            <td><select name="fw_rule7_type" onChange="SourceChanged(7, true)"><option value="single" $fw_rule7_type_single>single address<option value="any" $fw_rule7_type_any>any address<option value="subnet" $fw_rule7_type_subnet>subnet</select></td>
            <td><input name="fw_rule7_ipaddr" value="$FW_RULE7_IPADDR"></td>
            <td><input name="fw_rule7_subnet" value="$FW_RULE7_SUBNET"></td>
            <td><select name="fw_rule7_proto" onChange="ProtoChanged(7)"><option value="all" $fw_rule7_proto_all>all<option value="tcp" $fw_rule7_proto_tcp>TCP<option value="udp" $fw_rule7_proto_udp>UDP<option value="icmp" $fw_rule7_proto_icmp>ICMP</select></td>
            <td><input name="fw_rule7_port" size="8" maxlength="5" value="$FW_RULE7_PORT"></td>
          </tr>
          <tr>
            <td align="right">8.</td>
            <td><select name="fw_rule8_type" onChange="SourceChanged(8, true)"><option value="single" $fw_rule8_type_single>single address<option value="any" $fw_rule8_type_any>any address<option value="subnet" $fw_rule8_type_subnet>subnet</select></td>
            <td><input name="fw_rule8_ipaddr" value="$FW_RULE8_IPADDR"></td>
            <td><input name="fw_rule8_subnet" value="$FW_RULE8_SUBNET"></td>
            <td><select name="fw_rule8_proto" onChange="ProtoChanged(8)"><option value="all" $fw_rule8_proto_all>all<option value="tcp" $fw_rule8_proto_tcp>TCP<option value="udp" $fw_rule8_proto_udp>UDP<option value="icmp" $fw_rule8_proto_icmp>ICMP</select></td>
            <td><input name="fw_rule8_port" size="8" maxlength="5" value="$FW_RULE8_PORT"></td>
          </tr>
          <tr>
            <td align="right">9.</td>
            <td><select name="fw_rule9_type" onChange="SourceChanged(9, true)"><option value="single" $fw_rule9_type_single>single address<option value="any" $fw_rule9_type_any>any address<option value="subnet" $fw_rule9_type_subnet>subnet</select></td>
            <td><input name="fw_rule9_ipaddr" value="$FW_RULE9_IPADDR"></td>
            <td><input name="fw_rule9_subnet" value="$FW_RULE9_SUBNET"></td>
            <td><select name="fw_rule9_proto" onChange="ProtoChanged(9)"><option value="all" $fw_rule9_proto_all>all<option value="tcp" $fw_rule9_proto_tcp>TCP<option value="udp" $fw_rule9_proto_udp>UDP<option value="icmp" $fw_rule9_proto_icmp>ICMP</select></td>
            <td><input name="fw_rule9_port" size="8" maxlength="5" value="$FW_RULE9_PORT"></td>
          </tr>
          <tr>
            <td align="right">10.</td>
            <td><select name="fw_rule10_type" onChange="SourceChanged(10, true)"><option value="single" $fw_rule10_type_single>single address<option value="any" $fw_rule10_type_any>any address<option value="subnet" $fw_rule10_type_subnet>subnet</select></td>
            <td><input name="fw_rule10_ipaddr" value="$FW_RULE10_IPADDR"></td>
            <td><input name="fw_rule10_subnet" value="$FW_RULE10_SUBNET"></td>
            <td><select name="fw_rule10_proto" onChange="ProtoChanged(10)"><option value="all" $fw_rule10_proto_all>all<option value="tcp" $fw_rule10_proto_tcp>TCP<option value="udp" $fw_rule10_proto_udp>UDP<option value="icmp" $fw_rule10_proto_icmp>ICMP</select></td>
            <td><input name="fw_rule10_port" size="8" maxlength="5" value="$FW_RULE10_PORT"></td>
          </tr>

		  <tr><td colspan="6"><i>* can be blank</i></td></tr>
	    </table>
	  </td>
	</tr>
	<tr>
	  <td><input type="submit" name="apply" value="Apply"></td>
	</tr>
      </table>
      </form>
      <script language="JavaScript" type="text/javascript">
      document.input.fw_mode.focus();
      for (index = 1; index <= 10; index++) {
	SourceChanged(index, false);
	ProtoChanged(index);
      }
      </script>
EOF

cat include/end.inc

