#!/bin/sh

[ -e /mnt/rwfs/settings/settings.snmp ] && . /mnt/rwfs/settings/settings.snmp

for arg in `awk -F= '/^SNMP_*/{print($1)}' /etc/defaults/settings.snmp`
do
    
    if eval "[ \"\" = \"\$$arg\"  ]"; then        
        val=`grep $arg /etc/defaults/settings.snmp`
        eval "$val"                
    fi
done


./begin $0

echo "</td><td colspan=\"3\" valign=\"top\">"
cat include/js.inc

if [ "$SNMP_REQUIRE_AUTH" = "yes" ]; then
    CHECKED="checked";
else
    CHECKED="";
fi

if [ "$SNMP_ENABLED" = "yes" ]; then
    ENABLED="checked";
else
    ENABLED="";
fi

SNMP_DESCRIPTION=`decode "$SNMP_DESCRIPTION"`
SNMP_CONTACT=`decode "$SNMP_CONTACT"`
SNMP_LOCATION=`decode "$SNMP_LOCATION"`

cat << EOF
function CheckForm() {
            
    var community = document.input.community_string.value;
    var contact = document.input.contact.value;
    var location = document.input.location.value;
    var description = document.input.description.value;
    var timeout = parseInt(GetValue(document.input.timeout));

    if( community.indexOf(" ") != -1 ){
        alert("Community string field must not contain whitespaces");
        Focus(document.input.community_string);
        return false;
    }

    if( isNaN(timeout)) {
        alert("Invalid timeout!");
        document.input.timeout.value="";
        Focus(document.input.timeout);
        return false;
    }
    
    return true;    
}
-->
</script>

<form name="input" onsubmit="return CheckForm();" action="config_snmp_set.cgi" method="post">
    <table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
	  <td class="title" align="center" colspan="2"><b>SNMP Configuration</b></td>
	</tr>
        <tr>
            <td>
                <table>
                    <tr>            
                        <td nowrap colspan="2">
                            <input name="enabled" $ENABLED type="checkbox"/>&nbsp;Enable SNMP
                        </td>
                    </tr>
                    <tr>
                       <td colspan="2"><input name="auth" $CHECKED type="checkbox">&nbsp;Require authentication</td>                       
                    </tr>
                   <tr>
                        <td nowrap>Community</td>
                        <td><input name="community_string" value="$SNMP_COMMUNITY_STRING"></td>
                    </tr>
                    <tr>
                        <td nowrap>Description</td>
                        <td><input name="description" value="$SNMP_DESCRIPTION"></td>
                    </tr>        
                    <tr>
                       <td nowrap>Contact</td>
                       <td><input name="contact" value="$SNMP_CONTACT"></td>
                    </tr>
                    <tr>
                       <td nowrap>Location</td>
                       <td><input name="location" value="$SNMP_LOCATION"></td>
                    </tr>
                    <tr>
                       <td nowrap>Timeout</td>
                       <td><input name="timeout" value="$SNMP_TIMEOUT"></td>
                    </tr>
                    
                </table>
            </td>
        </tr>
        <tr>
           <td nowrap colspan="2"><input name="submit" value="Apply" type="submit"></td>	    
        </tr>
    </table>
</form>
EOF

cat include/end.inc
