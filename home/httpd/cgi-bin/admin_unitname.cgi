#!/bin/sh
NAMEFILE=/mnt/rwfs/settings/unitname
[ -f $NAMEFILE ] && UNITNAME=`cat $NAMEFILE`
HOSTFILE=/mnt/rwfs/settings/hostname
[ -f $HOSTFILE ] && HOSTNAME=`cat $HOSTFILE`

[ -e /mnt/rwfs/settings/settings.etc ] && . /mnt/rwfs/settings/settings.etc

[ "$ETC_UNITNAME_OPENVPN" = "1" ] && ovpn="selected"
[ "$ETC_UNITNAME" = "none" ] && none="selected"
[ "$ETC_UNITNAME" = "ovpn" ] && ovpn="selected"
[ "$ETC_UNITNAME" = "snmp" ] && snmp="selected"
[ "$ETC_UNITNAME" = "user" ] && user="selected"
[ "$ETC_HOSTNAME" = "none" ] && hostnone="selected"
[ "$ETC_HOSTNAME" = "ovpn" ] && hostovpn="selected"
[ "$ETC_HOSTNAME" = "snmp" ] && hostsnmp="selected"
[ "$ETC_HOSTNAME" = "user" ] && hostuser="selected"



./begin $0

echo "</td><td colspan=\"3\" valign=\"top\">"

cat << EOF
      <table width="100%" cellspacing="0" cellpadding="5" border="3">

<script language="JavaScript" type="text/javascript">
function update() {
    mode = document.getElementById("unitnamemode").value;
    if (mode == "user") {
        document.getElementById("unitname").disabled=false;
        document.getElementById("unitname").readonly=false;
    } else {
        document.getElementById("unitname").disabled=true;
        document.getElementById("unitname").readonly=true;
    }
}
function updatehost() {
    mode = document.getElementById("hostnamemode").value;
    if (mode == "user") {
        document.getElementById("hostname").disabled=false;
        document.getElementById("hostname").readonly=false;
    } else {
        document.getElementById("hostname").disabled=true;
        document.getElementById("hostname").readonly=true;
    }
}

</script>
	<tr>
	  <td class="title" align="center">
	    <b>Unit name</b>
	  </td>
	</tr>
	<tr>
	  <td>
		<form name="input" action="admin_unitname_set.cgi" method="POST">
		<table width="100%" border="0">
        <tr>
            <td>
            <select name="unitnamemode" id="unitnamemode" onChange="update();">
                <option value="none" $none >Unit name disabled</option>
                <option value="ovpn" $ovpn >Take unit name from OpenVPN certificate</option>
                <option value="snmp" $snmp >Take unit name from SNMP description</option>
                <option value="user" $user >Enter unit name below</option>
            </select>
            </td>
        </tr>
		<tr>
		    <td>
			<input name="unitname" id="unitname" maxlength="100" value="$UNITNAME">
		    </td>
		</tr>
        <tr>
            <td>
            <select name="hostnamemode" id="hostnamemode" onChange="updatehost();">
                <option value="none" $hostnone >Default host name</option>
                <option value="ovpn" $hostovpn >Take host name from OpenVPN certificate</option>
                <option value="snmp" $hostsnmp >Take host name from SNMP description</option>
                <option value="user" $hostuser >Enter host name below</option>
            </select>
            </td>
        </tr>
        <tr>
            <td>
            <input name="hostname" id="hostname" maxlength="100" value="$HOSTNAME">
            </td>
        </tr>
		</table>
	  </td>
	</tr>
	<tr>
	  <td>
	  <input type="submit" name="save" value="Set Unit name">
	  </form></td>
	</tr>
    </table>
    <script language="JavaScript" type="text/javascript">
        update();
        updatehost();
        document.input.unitnamemode.focus();
    </script>
EOF

cat include/end.inc

