#!/bin/sh

FILE=/mnt/rwfs/settings/settings.ipsec
tun=`echo "$QUERY_STRING" | sed -n 's/^.*tun=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`

IPSEC_ENABLED=`cat $FILE | grep "IPSEC${tun}_ENABLED" | sed -e 's/^.*ENABLED=//'`
IPSEC_DESC=`cat $FILE | grep "IPSEC${tun}_DESC" | sed -e 's/^.*DESC=//'`
IPSEC_NAT_TRAVERSAL=`cat $FILE | grep "IPSEC${tun}_NAT_TRAVERSAL" | sed -e 's/^.*NAT_TRAVERSAL=//'`
IPSEC_AGGRESSIVE=`cat $FILE | grep "IPSEC${tun}_AGGRESSIVE" | sed -e 's/^.*AGGRESSIVE=//'`
IPSEC_VERIFY_CERT=`cat $FILE | grep "IPSEC${tun}_VERIFY_CERT" | sed -e 's/^.*VERIFY_CERT=//'`
IPSEC_AUTHBY=`cat $FILE | grep "IPSEC${tun}_AUTHBY" | sed -e 's/^.*AUTHBY=//'`
IPSEC_PFS=`cat $FILE | grep "IPSEC${tun}_PFS" | sed -e 's/^.*PFS=//'`
IPSEC_REMOTE_IPADDR=`cat $FILE | grep "IPSEC${tun}_REMOTE_IPADDR" | sed -e 's/^.*REMOTE_IPADDR=//'`
IPSEC_REMOTE_NETWORK=`cat $FILE | grep "IPSEC${tun}_REMOTE_NETWORK" | sed -e 's/^.*REMOTE_NETWORK=//'`
IPSEC_REMOTE_NETMASK=`cat $FILE | grep "IPSEC${tun}_REMOTE_NETMASK" | sed -e 's/^.*REMOTE_NETMASK=//'`
IPSEC_LOCAL_NETWORK=`cat $FILE | grep "IPSEC${tun}_LOCAL_NETWORK" | sed -e 's/^.*LOCAL_NETWORK=//'`
IPSEC_LOCAL_NETMASK=`cat $FILE | grep "IPSEC${tun}_LOCAL_NETMASK" | sed -e 's/^.*LOCAL_NETMASK=//'`
IPSEC_PSK=`cat $FILE | grep "IPSEC${tun}_PSK" | sed -e 's/^.*PSK=//'`
IPSEC_KEY_LIFE=`cat $FILE | grep "IPSEC${tun}_KEY_LIFE" | sed -e 's/^.*KEY_LIFE=//'`
IPSEC_IKE_LIFE=`cat $FILE | grep "IPSEC${tun}_IKE_LIFE" | sed -e 's/^.*IKE_LIFE=//'`
IPSEC_CA_CERT=`cat $FILE | grep "IPSEC${tun}_CA_CERT" | sed -e 's/^.*CA_CERT=//'`
IPSEC_REMOTE_CERT=`cat $FILE | grep "IPSEC${tun}_REMOTE_CERT" | sed -e 's/^.*REMOTE_CERT=//'`
IPSEC_LOCAL_CERT=`cat $FILE | grep "IPSEC${tun}_LOCAL_CERT" | sed -e 's/^.*LOCAL_CERT=//'`
IPSEC_REMOTE_ID=`cat $FILE | grep "IPSEC${tun}_REMOTE_ID" | sed -e 's/^.*REMOTE_ID=//'`
IPSEC_LOCAL_KEY=`cat $FILE | grep "IPSEC${tun}_LOCAL_KEY" | sed -e 's/^.*LOCAL_KEY=//'`
IPSEC_LOCAL_ID=`cat $FILE | grep "IPSEC${tun}_LOCAL_ID" | sed -e 's/^.*LOCAL_ID=//'`
IPSEC_REKEY_FUZZ=`cat $FILE | grep "IPSEC${tun}_REKEY_FUZZ" | sed -e 's/^.*REKEY_FUZZ=//'`
IPSEC_REKEY_MARGIN=`cat $FILE | grep "IPSEC${tun}_REKEY_MARGIN" | sed -e 's/^.*REKEY_MARGIN=//'`
IPSEC_P1ENCALG=`cat $FILE | grep "IPSEC${tun}_P1ENCALG" | sed -e 's/^.*P1ENCALG=//'`
IPSEC_P1HASHALG=`cat $FILE | grep "IPSEC${tun}_P1HASHALG" | sed -e 's/^.*P1HASHALG=//'`
IPSEC_P1DHGROUP=`cat $FILE | grep "IPSEC${tun}_P1DHGROUP" | sed -e 's/^.*P1DHGROUP=//'`
IPSEC_P2ENCALG=`cat $FILE | grep "IPSEC${tun}_P2ENCALG" | sed -e 's/^.*P2ENCALG=//'`
IPSEC_P2AUTHALG=`cat $FILE | grep "IPSEC${tun}_P2AUTHALG" | sed -e 's/^.*P2AUTHALG=//'`
IPSEC_P2PFSGROUP=`cat $FILE | grep "IPSEC${tun}_P2PFSGROUP" | sed -e 's/^.*P2PFSGROUP=//'`
IPSEC_MY_TYPE=`cat $FILE | grep "IPSEC${tun}_MY_TYPE" | sed -e 's/^.*MY_TYPE=//'`
IPSEC_MY_IDENTIFIER=`cat $FILE | grep "IPSEC${tun}_MY_IDENTIFIER" | sed -e 's/^.*MY_IDENTIFIER=//'`
IPSEC_PEERS_TYPE=`cat $FILE | grep "IPSEC${tun}_PEERS_TYPE" | sed -e 's/^.*PEERS_TYPE=//'`
IPSEC_PEERS_IDENTIFIER=`cat $FILE | grep "IPSEC${tun}_PEERS_IDENTIFIER" | sed -e 's/^.*PEERS_IDENTIFIER=//'`
IPSEC_VERIFY_IDENTIFIER=`cat $FILE | grep "IPSEC${tun}_VERIFY_IDENTIFIER" | sed -e 's/^.*VERIFY_IDENTIFIER=//'`
IPSEC_PINGTEST_IP=`cat $FILE | grep "IPSEC${tun}_PINGTEST_IP" | sed -e 's/^.*PINGTEST_IP=//'`
IPSEC_PINGTEST_INT=`cat $FILE | grep "IPSEC${tun}_PINGTEST_INT" | sed -e 's/^.*PINGTEST_INT=//'`
IPSEC_LEVEL=`cat $FILE | grep "IPSEC${tun}_LEVEL" | sed -e 's/^.*LEVEL=//'`

[ -z "$IPSEC_P1ENCALG" ]            && IPSEC_P1ENCALG=3des
[ -z "$IPSEC_P1HASHALG" ]           && IPSEC_P1HASHALG=sha1
[ -z "$IPSEC_P1DHGROUP" ]           && IPSEC_P1DHGROUP=2
[ -z "$IPSEC_P2ENCALG" ]            && IPSEC_P2ENCALG=3des
[ -z "$IPSEC_P2AUTHALG" ]           && IPSEC_P2AUTHALG=hmac_sha1
[ -z "$IPSEC_P2PFSGROUP" ]          && IPSEC_P2PFSGROUP=0
[ -z "$IPSEC_MY_TYPE" ]             && IPSEC_MY_TYPE=none
[ -z "$IPSEC_PEERS_TYPE" ]          && IPSEC_PEERS_TYPE=none
[ -z "$IPSEC_VERIFY_IDENTIFIER" ]   && IPSEC_VERIFY_IDENTIFIER=0

case "$IPSEC_P1ENCALG" in
    des)        P1ENCALG_DES="selected";;
    blowfish)   P1ENCALG_BLOWFISH="selected";;
    aes)        P1ENCALG_AES="selected";;
    *)          P1ENCALG_3DES="selected";;
esac
case "$IPSEC_P1HASHALG" in
    sha256) P1HASHALG_SHA256="selected";;
    sha384) P1HASHALG_SHA384="selected";;
    md5)    P1HASHALG_MD5="selected";;
    *)      P1HASHALG_SHA1="selected";;
esac
case "$IPSEC_P1DHGROUP" in
    1)  P1DHGROUP_1="selected";;
    5)  P1DHGROUP_5="selected";;
    14) P1DHGROUP_14="selected";;
    15) P1DHGROUP_15="selected";;
    16) P1DHGROUP_16="selected";;
    17) P1DHGROUP_17="selected";;
    18) P1DHGROUP_18="selected";;
    *)  P1DHGROUP_2="selected";;
esac
case "$IPSEC_P2ENCALG" in
    des)        P2ENCALG_DES="selected";;
    blowfish)   P2ENCALG_BLOWFISH="selected";;
    rc5)        P2ENCALG_RC5="selected";;
    aes)        P2ENCALG_AES="selected";;
    *)          P2ENCALG_3DES="selected";;
esac
case "$IPSEC_P2AUTHALG" in
    hmac_sha256)    P2AUTHALG_HMACSHA256="selected";;
    hmac_sha384)    P2AUTHALG_HMACSHA384="selected";;
    hmac_md5)       P2AUTHALG_HMACMD5="selected";;
    3des)           P2AUTHALG_3DES="selected";;
    des)            P2AUTHALG_DES="selected";;
    *)              P2AUTHALG_HMACSHA1="selected";;
esac
case "$IPSEC_P2PFSGROUP" in
    1)  P2PFSGROUP_1="selected";;
    2)  P2PFSGROUP_2="selected";;
    5)  P2PFSGROUP_5="selected";;
    14) P2PFSGROUP_14="selected";;
    15) P2PFSGROUP_15="selected";;
    16) P2PFSGROUP_16="selected";;
    17) P2PFSGROUP_17="selected";;
    18) P2PFSGROUP_18="selected";;
    *)  P2PFSGROUP_0="selected";;
esac
case "$IPSEC_MY_TYPE" in
		address)	MY_TYPE_ADDRESS="selected";;
		user_fqdn)  MY_TYPE_USER_FQDN="selected";;
		fqdn)		MY_TYPE_FQDN="selected";;
		asn1dn)		MY_TYPE_ASN1DN="selected";;
		*)			MY_TYPE_NONE="selected";;
esac
case "$IPSEC_PEERS_TYPE" in
		address)	PEERS_TYPE_ADDRESS="selected";;
		user_fqdn)  PEERS_TYPE_USER_FQDN="selected";;
		fqdn)		PEERS_TYPE_FQDN="selected";;
		asn1dn)		PEERS_TYPE_ASN1DN="selected";;
		*)			PEERS_TYPE_NONE="selected";;
esac

case "$IPSEC_LEVEL" in
    default)    LEV_DEF="selected" ;;
    use)        LEV_USE="selected" ;;
    unique)     LEV_UNI="selected" ;;
    *)          LEV_REQ="selected" ;;
esac
    
[ -z "$IPSEC_KEY_LIFE" ] && IPSEC_KEY_LIFE=3600
[ -z "$IPSEC_IKE_LIFE" ] && IPSEC_IKE_LIFE=3600
[ -z "$IPSEC_REKEY_FUZZ" ] && IPSEC_REKEY_FUZZ=100
[ -z "$IPSEC_REKEY_MARGIN" ] && IPSEC_REKEY_MARGIN=540

[ "$IPSEC_ENABLED" = "1" ] && ENABLED="checked"
[ "$IPSEC_NAT_TRAVERSAL" = "1" ] && TRAVERSAL="selected"
[ "$IPSEC_AGGRESSIVE" = "1" ] && AGGRESSIVE="selected"
[ "$IPSEC_VERIFY_CERT" = "0" ] && VERIFY="selected"
[ "$IPSEC_AUTHBY" = "rsa" ] && RSA="selected"
[ "$IPSEC_PFS" = "1" ] && PFS="selected"

if [ "$IPSEC_VERIFY_IDENTIFIER" != "0" ]; then 
    VERIFY_IDENTIFIER_ON="selected"
else
    VERIFY_IDENTIFIER_OFF="selected"
fi


IPSEC_DESC=`echo -n "$IPSEC_DESC" | base64 -d`
IPSEC_PSK=`echo -n "$IPSEC_PSK" | base64 -d`
IPSEC_LOCAL_PASS=`echo -n "$IPSEC_LOCAL_PASS" | base64 -d`
IPSEC_MY_IDENTIFIER=`echo -n "$IPSEC_MY_IDENTIFIER" | base64 -d`
IPSEC_PEERS_IDENTIFIER=`echo -n "$IPSEC_PEERS_IDENTIFIER" | base64 -d`


./begin $0

echo "</td><td colspan=\"3\" valign=\"top\">"
cat include/js.inc
cat << EOF
   	//document.input.ipsec_my_identifier.disabled = !(document.input.ipsec_my_type.value != "none");
   	//document.input.ipsec_peers_identifier.disabled = !(document.input.ipsec_peers_type.value != "none");
      function CheckForm() {
	var keylife = parseInt(GetValue(document.input.ipsec_key_life));
	var ikelife = parseInt(GetValue(document.input.ipsec_ike_life));
	var margin = parseInt(GetValue(document.input.ipsec_rekey_margin));
	var fuzz = parseInt(GetValue(document.input.ipsec_rekey_fuzz));
    if (!IsValidIP(document.input.ipsec_remote_ipaddr, false)) {
      return Error("Invalid remote IP address.", document.input.ipsec_remote_ipaddr);
    }
	if (!IsValidIP(document.input.ipsec_remote_network, true)) {
	  return Error("Invalid remote subnet.", document.input.ipsec_remote_network);
	}
	if (!IsValidIP(document.input.ipsec_remote_netmask, true)) {
	  return Error("Invalid remote subnet mask.", document.input.ipsec_remote_netmask);
	}
	if (!IsValidIP(document.input.ipsec_local_network, false)) {
	  return Error("Invalid local subnet.", document.input.ipsec_local_network);
	}
	if (!IsValidIP(document.input.ipsec_local_netmask, false)) {
	  return Error("Invalid local subnet mask.", document.input.ipsec_local_netmask);
	}
	if (!IsInRange(document.input.ipsec_key_life, 1, 86400, false)) {
	  return Error("Missing or invalid key lifetime.", document.input.ipsec_key_life);
	}
	if (!IsInRange(document.input.ipsec_ike_life, 1, 86400, false)) {
	  return Error("Missing or invalid IKE lifetime.", document.input.ipsec_ike_life);
	}
	if (!IsInRange(document.input.ipsec_rekey_margin, 1, 3600, false)) {
	  return Error("Missing or invalid rekey margin.", document.input.ipsec_rekey_margin);
	}
	if (!IsInRange(document.input.ipsec_rekey_fuzz, 0, 200, false)) {
	  return Error("Missing or invalid rekey fuzz.", document.input.ipsec_rekey_fuzz);
	}
	if (keylife <= margin * (1 + fuzz/100)) {
	  return Error("Key lifetime must be greater than " + (1 + fuzz/100) + "x rekey margin.", document.input.ipsec_key_life);
	}
	if (ikelife <= margin * (1 + fuzz/100)) {
	  return Error("IKE lifetime must be greater than " + (1 + fuzz/100) + "x rekey margin.", document.input.ipsec_ike_life);
	}
    if (!IsValidIP(document.input.ipsec_pingtest_ip, true)) {
      return Error("Invalid ping test IP.", document.input.ipsec_pingtest_ip);
    }
    if (document.input.ipsec_pingtest_ip.value != '') {
        if (!IsInRange(document.input.ipsec_pingtest_int, 1, 1440, false)) {
            return Error("Missing or invalid ping test interval.", document.input.ipsec_pingtest_int);
        }
    }
	if ( document.input.ipsec_my_type.value != "none" ){
	    if ( document.input.ipsec_my_identifier.value == ""  ) {
		    return Error("My Identifier must be specified", document.input.ipsec_my_identifier);
	    }
	}
	if ( document.input.ipsec_peers_type.value != "none") {
        if ( document.input.ipsec_peers_identifier.value == "" ) {
	        return Error("Peers Identifier must be specified", document.input.ipsec_peers_identifier);
        }
	}
	if (document.input.ipsec_enabled.checked) {
	  if (document.input.ipsec_authby.value == 'rsa') {
	    if (IsEmpty(document.input.ipsec_ca_cert) || document.input.ipsec_ca_cert.value.length > 6000) {
	      return Error("Missing or invalid CA certificate.", document.input.ipsec_ca_cert);
	    }
	    if (IsEmpty(document.input.ipsec_remote_cert) || document.input.ipsec_remote_cert.value.length > 6000) {
	      return Error("Missing or invalid remote certificate.", document.input.ipsec_remote_cert);
	    }
	    if (IsEmpty(document.input.ipsec_local_cert) || document.input.ipsec_local_cert.value.length > 6000) {
	      return Error("Missing or invalid local certificate.", document.input.ipsec_local_cert);
	    }
	    if (IsEmpty(document.input.ipsec_local_key) || document.input.ipsec_local_key.value.length > 6000) {
	      return Error("Missing or invalid local private key.", document.input.ipsec_local_key);
	    }
	  } else {
	    if (IsEmpty(document.input.ipsec_psk)) {
	      return Error("Missing pre-shared key.", document.input.ipsec_psk);
	    }
	  }
	}
	return true;
      }
      function AuthByChanged() {
	var rsa = document.input.ipsec_authby.value == "rsa";
	document.input.ipsec_psk.disabled = rsa;
	document.input.ipsec_ca_cert.disabled = !rsa;
	document.input.ipsec_remote_cert.disabled = !rsa;
	document.input.ipsec_local_cert.disabled = !rsa;
	document.input.ipsec_local_key.disabled = !rsa;
	document.input.ipsec_local_pass.disabled = !rsa;
    document.input.ipsec_verify_cert.disabled = !rsa;
	document.getElementById('psk').style.color = rsa ? "gray" : "";
	document.getElementById('ca_cert').style.color = rsa ? "" : "gray";
	document.getElementById('remote_cert').style.color = rsa ? "" : "gray";
	document.getElementById('local_cert').style.color = rsa ? "" : "gray";
	document.getElementById('local_key').style.color = rsa ? "" : "gray";
	document.getElementById('local_pass').style.color = rsa ? "" : "gray";
      }
      function PeerTypeChanged(){
      	var peer_none = document.input.ipsec_peers_type.value == "none";
      	document.input.ipsec_peers_identifier.disabled = peer_none;
      }
      function MyTypeChanged(){
      	var my_none = document.input.ipsec_my_type.value == "none";
      	document.input.ipsec_my_identifier.disabled = my_none;
      }
      //-->
      </script>
      <form name="input" onload="OnLoad()" onsubmit="return CheckForm();" action="config_ipsecn_set.cgi?tun=$tun" method="post">
      <table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
	  <td class="title" align="center"><b>IPsec Tunnel #$tun Configuration</b></td>
	</tr>
	<tr>
	  <td>
	    <table> <!-- enable -->
	      <tr>
		<td><input type="checkbox" name="ipsec_enabled" $ENABLED></td>
		<td nowrap>Create IPsec tunnel #$tun</td>
	      </tr>
	    </table>
	    <table> <!-- narrow params -->
		  <tr>
         <td nowrap>Description *</td>
         <td><input class="input" name="ipsec_desc" maxlength="30" value="$IPSEC_DESC"></td>
         <td width="30">&nbsp;</td>
         <td class="menu" colspan="2" align="center"><b>Phase 1</b></td>
		  </tr>
	      <tr>
		<td nowrap>Remote IP Address</td>
		<td><input class="input" name="ipsec_remote_ipaddr" value="$IPSEC_REMOTE_IPADDR"></td>
         <td>&nbsp;</td>
         <td nowrap>Encryption Algorythm</td>
         <td><select class="input" name="ipsec_p1encalg">
                <option value="3des" $P1ENCALG_3DES>3DES
                <option value="des" $P1ENCALG_DES>DES
                <option value="blowfish" $P1ENCALG_BLOWFISH>BLOWFISH
                <option value="aes" $P1ENCALG_AES>AES
         </select></td>
	      </tr>
	      <tr>
		<td nowrap>Remote ID *</td>
		<td><input class="input" name="ipsec_remote_id" value="$IPSEC_REMOTE_ID"></td>
        <td>&nbsp;</td>
        <td nowrap>Hash Algorythm</td>
        <td><select class="input" name="ipsec_p1hashalg">
            <option value="sha1" $P1HASHALG_SHA1>SHA1
            <option value="sha256" $P1HASHALG_SHA256>SHA256
            <option value="sha384" $P1HASHALG_SHA384>SHA384
            <option value="md5" $P1HASHALG_MD5>MD5
        </select></td>
	      </tr>
	      <tr>
		<td nowrap>Remote Subnet</td>
		<td><input class="input" name="ipsec_remote_network" value="$IPSEC_REMOTE_NETWORK"></td>
        <td>&nbsp;</td>
        <td nowrap>DH Group</td>
        <td><select class="input" name="ipsec_p1dhgroup">
            <option value="1" $P1DHGROUP_1>DH Group 1 (768 bits)
            <option value="2" $P1DHGROUP_2>DH Group 2 (1024 bits)
            <option value="5" $P1DHGROUP_5>DH Group 5 (1536 bits)
            <option value="14" $P1DHGROUP_14>DH Group 14 (2048 bits)
            <option value="15" $P1DHGROUP_15>DH Group 15 (3072 bits)
            <option value="16" $P1DHGROUP_16>DH Group 16 (4096 bits)
            <option value="17" $P1DHGROUP_17>DH Group 17 (6144 bits)
            <option value="18" $P1DHGROUP_18>DH Group 18 (8192 bits)
         </select></td>
	      </tr>
	      <tr>
		<td nowrap>Remote Subnet Mask</td>
		<td><input class="input" name="ipsec_remote_netmask" value="$IPSEC_REMOTE_NETMASK"></td>
        <td colspan="3">&nbsp;</td>
	      </tr>
	      <tr>
		<td nowrap>Local ID *</td>
		<td><input class="input" name="ipsec_local_id" value="$IPSEC_LOCAL_ID"></td>
        <td>&nbsp;</td>
        <td class="menu" colspan="2" align="center"><b>Phase 2</b></td>
	      </tr>
	      <tr>
		<td nowrap>Local Subnet</td>
		<td><input class="input" name="ipsec_local_network" value="$IPSEC_LOCAL_NETWORK"></td>
        <td>&nbsp;</td>
        <td nowrap>Encryption Algorythm</td>
        <td><select class="input" name="ipsec_p2encalg">
            <option value="3des"$P2ENCAGL_3DES>3DES
            <option value="des" $P2ENCALG_DES>DES
            <option value="blowfish" $P2ENCALG_BLOWFISH>BLOWFISH
            <option value="rc5" $P2ENCALG_RC5>RC5
            <option value="aes" $P2ENCALG_AES>AES
        </select></td>
	      </tr>
	      <tr>
		<td nowrap>Local Subnet Mask</td>
		<td><input class="input" name="ipsec_local_netmask" value="$IPSEC_LOCAL_NETMASK"></td>
        <td>&nbsp;</td>
        <td nowrap>Authentication Algorythm</td>
        <td><select class="input" name="ipsec_p2authalg">
            <option value="hmac_sha1" $P2AUTHALG_HMACSHA1>HMAC-SHA1
            <option value="hmac_sha256" $P2AUTHALG_HMACSHA256>HMAC-SHA256
            <option value="hmac_sha384" $P2AUTHALG_HMACSHA384>HMAC-SHA384
            <option value="des" $P2AUTHALG_DES>DES
            <option value="3des" $P2AUTHALG_3DES>3DES
            <option value="hmac_md5" $P2AUTHALG_HMACMD5>HMAC-MD5
        </select></td>
	      </tr>
	      <tr>
		<td nowrap>Key Lifetime (sec)</td>
		<td nowrap><input class="input" name="ipsec_key_life" value="$IPSEC_KEY_LIFE"></td>
        <td>&nbsp;</td>
        <td nowrap>PFS Group</td>
        <td><select class="input" name="ipsec_p2pfsgroup">
            <option value="0" $P2PFSGROUP_0>None
            <option value="1" $P2PFSGROUP_1>PFS Group 1 (768 bits)
            <option value="2" $P2PFSGROUP_2>PFS Group 2 (1024 bits)
            <option value="5" $P2PFSGROUP_5>PFS Group 5 (1536 bits)
            <option value="14" $P2PFSGROUP_14>PFS Group 14 (2048 bits)
            <option value="15" $P2PFSGROUP_15>PFS Group 15 (3072 bits)
            <option value="16" $P2PFSGROUP_16>PFS Group 16 (4096 bits)
            <option value="17" $P2PFSGROUP_17>PFS Group 17 (6144 bits)
            <option value="18" $P2PFSGROUP_18>PFS Group 18 (8192 bits)
        </select></td>
	      </tr>
	      <tr>
		<td nowrap>IKE Lifetime (sec)</td>
		<td nowrap><input class="input" name="ipsec_ike_life" value="$IPSEC_IKE_LIFE"></td>
        <td colspan="3">&nbsp;</td>
	      </tr>
	      <tr>
		<td nowrap>Rekey Margin (sec)</td>
		<td nowrap><input class="input" name="ipsec_rekey_margin" value="$IPSEC_REKEY_MARGIN"></td>
        <td>&nbsp;</td>
            <td nowrap>My Identifier Type</td>
            <td>
                <select class="input" name="ipsec_my_type" onChange="MyTypeChanged()">
                    <option value="none" $MY_TYPE_NONE>None
                    <option value="address" $MY_TYPE_ADDRESS>Address
                    <option value="user_fqdn" $MY_TYPE_USER_FQDN>User FQDN
                    <option value="asn1dn" $MY_TYPE_ASN1DN>ASN1DN
                    <option value="fqdn" $MY_TYPE_FQDN>FQDN
                </select>
            </td>
	      </tr>
	      <tr>
		<td nowrap>Rekey Fuzz (%)</td>
		<td nowrap><input class="input" name="ipsec_rekey_fuzz" value="$IPSEC_REKEY_FUZZ"></td>
        <td>&nbsp;</td>
        <td nowrap>My Identifier</td>
        <td nowrap><input class="input" name="ipsec_my_identifier" value="$IPSEC_MY_IDENTIFIER"> </td>
		</tr>
		<tr>
		<td nowrap>NAT Traversal</td>
		<td><select class="input" name="ipsec_nat_traversal"><option value="0">disabled<option value="1" $TRAVERSAL>enabled</select></td>
        <td>&nbsp;</td>
            <td nowrap>Peers Identifier Type</td>
            <td>
                <select class="input" name="ipsec_peers_type" onChange="PeerTypeChanged()">
                    <option value="none" $PEERS_TYPE_NONE>None
                    <option value="address" $PEERS_TYPE_ADDRESS>Address
                    <option value="user_fqdn" $PEERS_TYPE_USER_FQDN>User FQDN
                    <option value="asn1dn" $PEERS_TYPE_ASN1DN>ASN1DN
                    <option value="fqdn" $PEERS_TYPE_FQDN>FQDN
                </select>
            </td>
	      </tr>
	      <tr>
		<td nowrap>Aggressive Mode</td>
		<td><select class="input" name="ipsec_aggressive"><option value="0">disabled<option value="1" $AGGRESSIVE>enabled</select></td>
         <td>&nbsp;</td>
         <td nowrap>Peers Identifier</td>
         <td nowrap><input class="input" name="ipsec_peers_identifier" value="$IPSEC_PEERS_IDENTIFIER"> </td>
	      </tr>
	      <tr>
		<td nowrap>Authenticate Mode</td>
		<td><select class="input" name="ipsec_authby" onChange="AuthByChanged()"><option value="secret">pre-shared key<option value="rsa" $RSA>X.509 certificate</select></td>
        <td>&nbsp;</td>
        <td nowrap>Verify Identifier</td>
        <td><select class="input" name="ipsec_verify_identifier">
            <option value="on" $VERIFY_IDENTIFIER_ON>On
            <option value="off" $VERIFY_IDENTIFIER_OFF>Off
            </select>
        </td>
	      </tr>
          <tr>
        <td nowrap>Verify Certificate</td>
        <td><select class="input" name="ipsec_verify_cert">
                <option value="1">enabled
                <option value="0" $VERIFY>disabled
        </select></td>
        <td>&nbsp;</td>
        <td nowrap>Ping Test IP</td>
        <td><input class="input" name="ipsec_pingtest_ip" value="$IPSEC_PINGTEST_IP"></td>
          </tr>
          <tr>
		<td nowrap id="psk">Pre-shared Key</td>
		<td><input class="input" name="ipsec_psk" value="$IPSEC_PSK"></td>
        <td>&nbsp;</td>
        <td nowrap id="psk">Ping Test Interval (min)</td>
        <td><input class="input" name="ipsec_pingtest_int" value="$IPSEC_PINGTEST_INT"></td>
	      </tr>
          <tr>
        <td nowrap id="level">Policy level</td>
        <td><select class="input" name="ipsec_level">
                <option value="default" $LEV_DEF>default</option>
                <option value="use" $LEV_USE>use</option>
                <option value="require" $LEV_REQ>require</option>
                <option value="unique" $LEV_UNI>unique</option>
        </select></td>
        <td colspan="3">&nbsp;</td>
          </tr>
<!-- wide params -->
	      <tr>
		<td nowrap id="ca_cert">CA Certificate</td>
		<td nowrap colspan="4">
<textarea cols="78" rows="3" name="ipsec_ca_cert">
EOF
echo -n "$IPSEC_CA_CERT" | base64 -d
cat << EOF
</textarea>
		</td>
	      </tr>
	      <tr>
		<td nowrap id="remote_cert">Remote Certificate</td>
		<td nowrap colspan="4">
<textarea cols="78" rows="3" name="ipsec_remote_cert">
EOF
echo -n "$IPSEC_REMOTE_CERT" | base64 -d
cat << EOF
</textarea>
		</td>
	      </tr>
	      <tr>
		<td nowrap id="local_cert">Local Certificate</td>
		<td nowrap colspan="4">
<textarea cols="78" rows="3" name="ipsec_local_cert">
EOF
echo -n "$IPSEC_LOCAL_CERT" | base64 -d
cat << EOF
</textarea>
		</td>
	      </tr>
	      <tr>
		<td nowrap id="local_key">Local Private Key</td>
		<td nowrap colspan="4">
<textarea cols="78" rows="3" name="ipsec_local_key">
EOF
echo -n "$IPSEC_LOCAL_KEY" | base64 -d
cat << EOF
</textarea>
		</td>
	      </tr>
	      <tr>
		<td nowrap id="local_pass">Local Passphrase *</td>
		<td nowrap colspan="4"><input class="input" name="ipsec_local_pass" value="$IPSEC_LOCAL_PASS"></td>
	      </tr>
	      <tr>
		<td nowrap colspan="5">* <i>can be blank</i></td>
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
      document.input.ipsec_enabled.focus();
    AuthByChanged();
    PeerTypeChanged();
    MyTypeChanged();
      //-->
      </script>
EOF

cat include/end.inc

