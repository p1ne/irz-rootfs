#!/bin/sh

[ -e /mnt/rwfs/settings/settings.dyndns ] && . /mnt/rwfs/settings/settings.dyndns

[ "$DYNDNS_ENABLED" = "1" ] && CHECKED="checked"
[ "$DYNDNS_FORCE_UPDATE" = "1" ]  && FORCE_CHECKED="checked"
[ -z "$DYNDNS_SYSTEM" ] && DYNDNS_SYSTEM=dyndns
DYNDNS_PASSWORD=`echo $DYNDNS_PASSWORD | base64 -d`
DYNDNS_NAME=`echo $DYNDNS_NAME | base64 -d`
DYNDNS_URL=`echo $DYNDNS_URL | base64 -d`
case $DYNDNS_SYSTEM in
    noip)   NOIP="selected" ;;
    free)   FREE="selected" ;;
    zone)   ZONE="selected" ;;
    cust)   CUST="selected" ;;
    *)      DYND="selected" ;;
esac
./begin $0

echo "</td><td colspan=\"3\" valign=\"top\">"
cat include/js.inc

cat << EOF
    function change_sys() {
        var cust  = document.input.dyndns_system.value == "cust";
        document.input.dyndns_name.disabled = !cust;
        document.input.dyndns_url.disabled = !cust;
        document.getElementById('dyndns_name').style.color = cust ? "" : "gray";
        document.getElementById('dyndns_url').style.color = cust ? "" : "gray";
    }

function CheckForm() {
	    var dyndns_enabled = document.input.dyndns_enabled.checked;
        var dyndns_updates_enabled = document.input.dyndns_force_updates.checked;
        var intvl = parseInt(GetValue(document.input.dyndns_update_interval));

    if (cust && GetValue(document.input.dyndns_name).length < 1) {
        alert("Invalid or missing custom server.");
        Focus(document.input.dyndns_name);
        return false;
    }
    if (cust && GetValue(document.input.dyndns_url).length < 1) {
        alert("Invalid or missing custom URL.");
        Focus(document.input.dyndns_url);
        return false;
    }
        
	if (dyndns_enabled && GetValue(document.input.dyndns_hostname).length < 6) {
	  alert("Invalid or missing hostname.");
	  Focus(document.input.dyndns_hostname);
	  return false;
	}
	if (dyndns_enabled && GetValue(document.input.dyndns_username).length < 1) {
	  alert("Missing username.");
	  Focus(document.input.dyndns_username);
	  return false;
	}
	if (dyndns_enabled && GetValue(document.input.dyndns_password).length < 1) {
	  alert("Missing password.");
	  Focus(document.input.dyndns_password);
	  return false;
	}
        
        /*if (dyndns_enabled && intvl < 1) {
	  alert("Update interval not set");
	  Focus(document.input.dyndns_update_interval);
	  return false;
    }*/
        
	return true;
}
      //-->
      </script>
      <form name="input" onsubmit="return CheckForm();" action="config_dyndns_set.cgi" method="post">
      <table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
	  <td class="title" align="center">
	    <b>DynDNS Configuration</b>
	  </td>
	</tr>
	<tr>
	  <td>
	    <table>
	      <tr>
		<td><input type="checkbox" name="dyndns_enabled" $CHECKED></td>
		<td nowrap>Enable DynDNS client</td>
	      </tr>
	    </table>
	    <table>
          <tr>
        <td nowrap>Service Provider</td>
        <td><select class="input" name="dyndns_system" onClick="change_sys()">
            <option value="dynd" $DYND>dyndns.com</option>
            <option value="noip" $NOIP>no-ip.com</option>
            <option value="free" $FREE>freedns.afraid.org</option>
            <option value="zone" $ZONE>zoneedit.com</option>
            <option value="cust" $CUST>Custom</option>
        </select></td>
          </tr>
	      <tr>
		<td nowrap>Hostname</td>
		<td><input class="input" name="dyndns_hostname" value="$DYNDNS_HOSTNAME"></td>
	      </tr>
	      <tr>
		<td nowrap>Username</td>
		<td><input class="input" name="dyndns_username" value="$DYNDNS_USERNAME"></td>
	      </tr>
	      <tr>
		<td nowrap>Password</td>
		<td><input class="input" type="password" name="dyndns_password" value="$DYNDNS_PASSWORD"></td>
	      </tr>
          <tr>
        <td nowrap>Custom Server</td>
        <td><input class="input" name="dyndns_name" value="$DYNDNS_NAME"></td>
          </tr>
          <tr>
        <td nowrap>Custom URL</td>
        <td><input class="input" name="dyndns_url" value="$DYNDNS_URL"></td>
          </tr>
          <tr>
		<td nowrap>Update interval</td>
		<td><input name="dyndns_update_interval" maxlength="6" size="6" value="$DYNDNS_UPDATE_INTERVAL"> seconds</td>
	      </tr>
		</table>
		<table>
         <tr>
          <td><input type="checkbox" name="dyndns_force_updates" $FORCE_CHECKED></td>
          <td nowrap>Force updates (Use carefully, or your account may be blocked!)</td>
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
      document.input.dyndns_enabled.focus();
      change_sys();
      </script>
EOF

cat include/end.inc

