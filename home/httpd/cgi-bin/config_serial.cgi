#!/bin/sh

[ -e /mnt/rwfs/settings/settings.serial ] && . /mnt/rwfs/settings/settings.serial
[ -e /etc/version ] && . /etc/version

case "$SER_MODE" in
	server)     mserver=selected ;;
	client) 	mclient=selected ;;
	*)          mnone=selected ;;
esac
case "$SER_MODE_4XX" in
	server)     	mserver_4XX=selected ;;
	client)		mclient_4XX=selected ;;
	*)          	mnone_4XX=selected ;;
esac

case "$SER_IFACE" in
    usb)    ifusb="selected" ;;
    485)    if485="selected" ;;
    422)    if422="selected" ;;
    *)      if232="selected" ;;
esac
case "$SER_IFACE_4XX" in
    usb)    ifusb_4XX="selected" ;;
    485)    if485_4XX="selected" ;;
    422)    if422_4XX="selected" ;;
    *)      if232_4XX="selected" ;;
esac
case "$SER_BAUD" in
	300)    s300=selected ;;
	1200)   s1200=selected ;;
	2400)   s2400=selected ;;
	4800)   s4800=selected ;;
	9600)   s9600=selected ;;
	19200)	s19200=selected	;;
	38400)  s38400=selected	;;
	57600)	s57600=selected	;;
	*)      s115200=selected ;;
esac
case "$SER_BAUD_4XX" in
	300)    s300_4XX=selected ;;
	1200)   s1200_4XX=selected ;;
	2400)   s2400_4XX=selected ;;
	4800)   s4800_4XX=selected ;;
	9600)   s9600_4XX=selected ;;
	19200)	s19200_4XX=selected	;;
	38400)  s38400_4XX=selected	;;
	57600)	s57600_4XX=selected	;;
	*)      s115200_4XX=selected ;;
esac
case "$SER_DATA" in
	7DATABITS)
		d7=selected
		;;
	*)
		d8=selected
		;;
esac
case "$SER_PARITY" in
	EVEN)
		pe=selected
		;;
	ODD)
		po=selected
		;;
	*)
		pn=selected
		;;
esac
case "$SER_STOP" in
	2STOPBITS)
		s2=selected
		;;
	*)
		s1=selected
		;;
esac	

case "$SER_DATA_4XX" in
	7DATABITS)
		d7_4XX=selected
		;;
	*)
		d8_4XX=selected
		;;
esac
case "$SER_PARITY_4XX" in
	EVEN)
		pe_4XX=selected
		;;
	ODD)
		po_4XX=selected
		;;
	*)
		pn_4XX=selected
		;;
esac
case "$SER_STOP_4XX" in
	2STOPBITS)
		s2_4XX=selected
		;;
	*)
		s1_4XX=selected
		;;
esac
SER_BANNER_DEC=`decode $SER_BANNER`
SER_BANNER_4XX_DEC=`decode $SER_BANNER_4XX`
[ -z "$SER_PORT" ] && SER_PORT=2001
[ -z "$SER_PORT_4XX" ] && SER_PORT_4XX=2002

[ -z "$SEC_INTVL" ] && SEC_INTVL="1"
SEC_PHONES_DEC=`decode $SEC_PHONES`
SEC_OPEN_DEC=`decode $SEC_OPEN`
SEC_CLOSE_DEC=`decode $SEC_CLOSE`
case "$SEC_MODE" in
	usbcom)	sec_mode_usb="selected";;
	serial) sec_mode_ser="selected";;
	*)		sec_mode_none="selected";;
esac

SMS_PHONES_DEC=`decode $SMS_PHONES`
SMS_ID_DEC=`decode $SMS_ID`
SMS_INDEX1_DEC=`decode $SMS_INDEX1`
SMS_INDEX2_DEC=`decode $SMS_INDEX2`
SMS_INDEX3_DEC=`decode $SMS_INDEX3`
SMS_INDEX4_DEC=`decode $SMS_INDEX4`
SMS_INDEX5_DEC=`decode $SMS_INDEX5`


case "$MODEL" in
    RCA|RC1)
        HAS232=1
        HAS485=0
        HAS422=0
        HASDCC=0
        ;;
    RUH|RUH2)
        HAS232=1
        HAS485=0
        HAS422=0
        HASDCC=1
        ;;
    RUH2b|RUHm|RUH2m|RUH2-RS485)
        HAS232=1
        HAS485=1
        HAS422=0
        HASDCC=1
        ;;
    RUH3)
        HAS232=1
        HAS485=1
        HAS422=1
        HASDCC=0
        ;;
    *)
        HAS232=1
        HAS485=0
        HAS422=0
        HASDCC=0
        ;;
esac

./begin $0

echo "</td><td colspan=\"3\" valign=\"top\">"
echo "    <script language=\"JavaScript\" type=\"text/javascript\">"
echo "  <!--"
[ "$HASDCC" = "1" ] && cat << EOF
/**
*
*  Base64 encode / decode
*  http://www.webtoolkit.info/
*
**/
 
var Base64 = {
 
    // private property
    _keyStr : "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=",
 
    // public method for encoding
    encode : function (input) {
        var output = "";
        var chr1, chr2, chr3, enc1, enc2, enc3, enc4;
        var i = 0;
 
        input = Base64._utf8_encode(input);
 
        while (i < input.length) {
 
            chr1 = input.charCodeAt(i++);
            chr2 = input.charCodeAt(i++);
            chr3 = input.charCodeAt(i++);
 
            enc1 = chr1 >> 2;
            enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);
            enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);
            enc4 = chr3 & 63;
 
            if (isNaN(chr2)) {
                enc3 = enc4 = 64;
            } else if (isNaN(chr3)) {
                enc4 = 64;
            }
 
            output = output +
            this._keyStr.charAt(enc1) + this._keyStr.charAt(enc2) +
            this._keyStr.charAt(enc3) + this._keyStr.charAt(enc4);
 
        }
 
        return output;
    },
 
    // public method for decoding
    decode : function (input) {
        var output = "";
        var chr1, chr2, chr3;
        var enc1, enc2, enc3, enc4;
        var i = 0;
 
        input = input.replace(/[^A-Za-z0-9\+\/\=]/g, "");
 
        while (i < input.length) {
 
            enc1 = this._keyStr.indexOf(input.charAt(i++));
            enc2 = this._keyStr.indexOf(input.charAt(i++));
            enc3 = this._keyStr.indexOf(input.charAt(i++));
            enc4 = this._keyStr.indexOf(input.charAt(i++));
 
            chr1 = (enc1 << 2) | (enc2 >> 4);
            chr2 = ((enc2 & 15) << 4) | (enc3 >> 2);
            chr3 = ((enc3 & 3) << 6) | enc4;
 
            output = output + String.fromCharCode(chr1);
 
            if (enc3 != 64) {
                output = output + String.fromCharCode(chr2);
            }
            if (enc4 != 64) {
                output = output + String.fromCharCode(chr3);
            }
 
        }
 
        output = Base64._utf8_decode(output);
 
        return output;
 
    },
 
    // private method for UTF-8 encoding
    _utf8_encode : function (string) {
        string = string.replace(/\r\n/g,"\n");
        var utftext = "";
 
        for (var n = 0; n < string.length; n++) {
 
            var c = string.charCodeAt(n);
 
            if (c < 128) {
                utftext += String.fromCharCode(c);
            }
            else if((c > 127) && (c < 2048)) {
                utftext += String.fromCharCode((c >> 6) | 192);
                utftext += String.fromCharCode((c & 63) | 128);
            }
            else {
                utftext += String.fromCharCode((c >> 12) | 224);
                utftext += String.fromCharCode(((c >> 6) & 63) | 128);
                utftext += String.fromCharCode((c & 63) | 128);
            }
 
        }
 
        return utftext;
    },
 
    // private method for UTF-8 decoding
    _utf8_decode : function (utftext) {
        var string = "";
        var i = 0;
        var c = c1 = c2 = 0;
 
        while ( i < utftext.length ) {
 
            c = utftext.charCodeAt(i);
 
            if (c < 128) {
                string += String.fromCharCode(c);
                i++;
            }
            else if((c > 191) && (c < 224)) {
                c2 = utftext.charCodeAt(i+1);
                string += String.fromCharCode(((c & 31) << 6) | (c2 & 63));
                i += 2;
            }
            else {
                c2 = utftext.charCodeAt(i+1);
                c3 = utftext.charCodeAt(i+2);
                string += String.fromCharCode(((c & 15) << 12) | ((c2 & 63) << 6) | (c3 & 63));
                i += 3;
            }
 
        }
 
        return string;
    }
 
}
EOF
cat << EOF

    function Error(msg, obj) {
    	alert(msg); obj.focus(); obj.select(); return false;
     }

    function GetValue(obj) {
    	return obj.value.replace(/\s/g, '');
    }

    function IsValidPort(obj, empty) {
    	var str = GetValue(obj);
    	if (empty && str.length == 0) return true;
    	var value = parseInt(str);
    	return (value > 0) && (value < 65536);
    }
    
    function IsValidIP(obj, empty) {
    var str = GetValue(obj);
    var fields = str.match(/^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$/);
    if (fields != null) {
      var tmp = fields[1] | fields[2] | fields[3] | fields[4];
      return (tmp < 256) && (empty || tmp > 0);
    } else {
      return false;
    }
      }


    function CheckForm() {
		if ( !(document.input.ser_mode.value == "none") && !(IsValidPort(document.input.ser_port))) {
      		return Error("Missing or invalid port for RS-232", document.input.ser_port);
    	}
        if ((document.input.ser_mode.value == "client") && !(IsValidIP(document.input.ser_server, GetValue(document.input.ser_server).length == 0))  ) {
            return Error("Invalid Server IP", document.input.ser_server);
        }
EOF
[ "$HASDCC" = "1" ] && cat << EOF
        if ( (document.input.sec_mode.value == "serial") && (document.input.ser_mode.value != "none") ) {
            alert("Serial port is already in use!");
            document.input.sec_mode.focus();
            return false;
        }
EOF
[ "$HAS485" = "1" ] && cat << EOF
    	if ( !(document.input.ser_mode_4XX.value == "none") && !(IsValidPort(document.input.ser_port_4XX))) {
      		return Error("Missing or invalid port for RS-485", document.input.ser_port_4XX);
    	}
        if ((document.input.ser_mode_4XX.value == "client") && !(IsValidIP(document.input.ser_server_4XX, GetValue(document.input.ser_server_4XX).length == 0))  ) {
            return Error("Invalid Server IP for RS-485", document.input.ser_server_4XX);
        }
		if ( document.input.ser_mode.value == "server" && document.input.ser_mode_4XX.value == "server") {
		    if ( document.input.ser_port.value == document.input.ser_port_4XX.value ) {
    			alert("RS-232 and RS-485 server ports must be different");
	    		document.input.ser_mode.focus();
		    	return false;
		    }
		}
EOF
cat << EOF	
	return true;
    }

      function ModeChanged() {
    var m_none  = document.input.ser_mode.value == "none";
    var m_client  = document.input.ser_mode.value == "client";
    var m_server  = document.input.ser_mode.value == "server";
    document.input.ser_server.style.color = m_client ? "" : "gray";
    document.input.ser_recon_delay.style.color = m_client ? "" : "gray";
    document.input.ser_server.readOnly = !m_client;
    document.input.ser_recon_delay.readOnly = !m_client;
    document.getElementById('server').style.color = m_client ? "" : "gray";
    document.getElementById('recon_delay').style.color = m_client ? "" : "gray";
EOF
[ "$HASDCC" = "1" ] && cat << EOF
/*
    document.input.sms_id.style.color = m_sms ? "" : "gray";
    document.input.sms_id.readOnly = !m_sms;
    document.input.sms_phones.style.color = m_sms ? "" : "gray";
    document.input.sms_phones.readOnly = !m_sms;
    document.input.sms_index1.style.color = m_sms ? "" : "gray";
    document.input.sms_index1.readOnly = !m_sms;
    document.input.sms_index2.style.color = m_sms ? "" : "gray";
    document.input.sms_index2.readOnly = !m_sms;
    document.input.sms_index3.style.color = m_sms ? "" : "gray";
    document.input.sms_index3.readOnly = !m_sms;
    document.input.sms_index4.style.color = m_sms ? "" : "gray";
    document.input.sms_index4.readOnly = !m_sms;
    document.input.sms_index5.style.color = m_sms ? "" : "gray";
    document.input.sms_index5.readOnly = !m_sms;
*/
EOF
echo "      }"
[ "$HAS485" = "1" ] && cat << EOF      
      function ModeChanged_4XX() {
    var m_none  = document.input.ser_mode_4XX.value == "none";
    var m_client  = document.input.ser_mode_4XX.value == "client";
    var m_server  = document.input.ser_mode_4XX.value == "server";
    document.input.ser_server_4XX.style.color = m_client ? "" : "gray";
    document.input.ser_recon_delay_4XX.style.color = m_client ? "" : "gray";
    document.input.ser_server_4XX.readOnly = !m_client;
    document.input.ser_recon_delay_4XX.readOnly = !m_client;
    document.getElementById('server_4XX').style.color = m_client ? "" : "gray";
    document.getElementById('recon_delay_4XX').style.color = m_client ? "" : "gray";
      }
EOF
cat << EOF

    //-->
    </script>
      <form name="input" onsubmit="return CheckForm();" action="config_serial_set.cgi" method="post">
      <table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
	  <td class="title" align="center">
	    <b>Serial Port Configuration</b>
	  </td>
	</tr>
	<tr>
EOF

[ "$HAS232" = "1" ] && cat << EOF
	    <td>
	    <table width="100%">
	    <tr>
		<td valign="top">
		    <table><tr>
			<th colspan="2">RS-232 Port</th>
		    </tr><tr>
		
		    <td nowrap>Serial Port Mode</td>
		    <td><select name="ser_mode" class="input" onChange="ModeChanged()">
        		<option value="none" $mnone >None</option>
        		<option value="server" $mserver >Tunnel Server</option>
        		<option value="client" $mclient >Tunnel Client</option>
                </select>
    		    </td>
    		</tr>
    		<tr>
    		    <td nowrap>Interface</td>
    		    <td><select name="ser_iface" class="input">
        		<option value="232" $if232 >RS-232</option>
		        <option value="usb" $ifusb >USB-COM</option>
                </select>
    		    </td>
		</tr>
		<tr>
			<td nowrap>TCP Port</td>
			<td><input class="input" name="ser_port" value="$SER_PORT"></td>
		</tr>
		<tr>
        	    <td id="server" nowrap>Server IP</td>
        	    <td id="server"><input class="input" name="ser_server" value="$SER_SERVER"></td>
    		</tr>
    		<tr>
			<td nowrap>Baudrate</td>
			<td><select name="ser_baud" class="input">
				<option value="300" $s300 >300</option>
				<option value="1200" $s1200 >1 200</option>
      			<option value="2400" $s2400 >2 400</option>
               	<option value="4800" $s4800 >4 800</option>
       			<option value="9600" $s9600 >9 600</option>
	          	<option value="19200" $s19200 >19 200</option>
       			<option value="38400" $s38400 >38 400</option>
       			<option value="57600" $s57600 >57 600</option>
	          	<option value="115200" $s115200 >115 200</option>
			</select></td>
		</tr>
		<tr>
			<td nowrap>Data Bits</td>
			<td><select class="input" name="ser_data">
            			<option value="7DATABITS" $d7 >7 bits</option>
				<option value="8DATABITS" $d8 >8 bits</option>
			</select></td>
		</tr>
		<tr>
			<td nowrap>Parity Check</td>
			<td><select class="input" name="ser_parity">
            			<option value="NONE" $pn >None</option>
		            	<option value="EVEN" $pe >Even</option>
            			<option value="ODD" $po >Odd</option>
		            </select>
		        </td>
		</tr>
		<tr>
			<td nowrap>Stop Bits</td>
			<td><select class="input" name="ser_stop">
            			<option value="1STOPBIT" $s1 >1 bit</option>
		            	<option value="2STOPBITS" $s2 >2 bits</option>
		            </select>
		    	</td>
		</tr>
		<tr>
        	    <td nowrap id="timeout">Timeout</td>
        	    <td id="timeout"><input class="input" name="ser_tout" value="$SER_TOUT"> sec</td>
		</tr>
		<tr>
        	    <td nowrap id="accum_intvl">Accumulator interval</td>
        	    <td id="accum_intvl"><input class="input" name="ser_accum_intvl" value="$SER_ACCUM_INTVL"> ms</td>
    		</tr>
    		<tr>
        	    <td nowrap id="accum_attempts">Accumulator attempts</td>
        	    <td id="accum_atts"><input class="input" name="ser_accum_atts" value="$SER_ACCUM_ATTS"></td>
    		</tr>
    		<tr>
        	    <td nowrap id="recon_delay">Reconnect delay</td>
        	    <td id="recon_delay"><input class="input" name="ser_recon_delay" value="$SER_RECON_DELAY"> sec</td>
    		</tr><tr>
            <td nowrap id="banner">Banner</td>
            <td id="banner"><input class="input" name="ser_banner" value="$SER_BANNER_DEC"></td>
        </tr>
	</table>
    </td>
EOF

[ "$HAS485" = "1" ] && cat << EOF
    <td valign="top">
	<table>
	    <tr>
		<th colspan="2">RS-485 Port</th>
	    </tr>
	    <tr>
		<td nowrap>Serial Port Mode</td>
		<td><select name="ser_mode_4XX" class="input" onChange="ModeChanged_4XX()">
	            <option value="none" $mnone_4XX >None</option>
        	    <option value="server" $mserver_4XX >Tunnel Server</option>
        	    <option value="client" $mclient_4XX >Tunnel Client</option>
            </select>
    		</td>
    	    </tr>
    	    <tr>
    		<td nowrap>Interface</td>
    		<td><select name="ser_iface_4XX" class="input">
    	    <option value="485" $if485_4XX >RS-485</option>
EOF

if [ "$HAS422" = "1" ]; then 
    echo "          <option value=\"422\" $if422_4XX >RS-422</option>"
fi

[ "$HAS485" = "1" ] && cat << EOF        
    		</select></td>
	    </tr>
	    <tr>
		<td nowrap>TCP Port</td>
		<td><input class="input" name="ser_port_4XX" value="$SER_PORT_4XX"></td>
	    </tr><tr>
        	<td id="server_4XX" nowrap>Server IP</td>
        	<td id="server_4XX"><input class="input" name="ser_server_4XX" value="$SER_SERVER_4XX"></td>
    	    </tr><tr>
		<td nowrap>Baudrate</td>
		<td><select name="ser_baud_4XX" class="input">
			<option value="300" $s300_4XX >300</option>
			<option value="1200" $s1200_4XX >1 200</option>
    	    <option value="2400" $s2400_4XX >2 400</option>
            <option value="4800" $s4800_4XX >4 800</option>
            <option value="9600" $s9600_4XX >9 600</option>
	        <option value="19200" $s19200_4XX >19 200</option>
    	    <option value="38400" $s38400_4XX >38 400</option>
            <option value="57600" $s57600_4XX >57 600</option>
          	<option value="115200" $s115200_4XX >115 200</option>
		    </select>
		</td>
	    </tr>
	    <tr>
			<td nowrap>Data Bits</td>
			<td><select class="input" name="ser_data_4XX">
            	<option value="7DATABITS" $d7_4XX >7 bits</option>
				<option value="8DATABITS" $d8_4XX >8 bits</option>
			</select></td>
	    </tr><tr>
			<td nowrap>Parity Check</td>
			<td><select class="input" name="ser_parity_4XX">
            	<option value="NONE" $pn_4XX >None</option>
            	<option value="EVEN" $pe_4XX >Even</option>
            	<option value="ODD" $po_4XX >Odd</option>
            </select></td>
	    </tr><tr>
			<td nowrap>Stop Bits</td>
			<td><select class="input" name="ser_stop_4XX">
            	<option value="1STOPBIT" $s1_4XX >1 bit</option>
            	<option value="2STOPBITS" $s2_4XX >2 bits</option>
            </select></td>
		</tr><tr>
        	<td nowrap id="timeout_4XX">Timeout</td>
        	<td id="timeout_4XX"><input class="input" name="ser_tout_4XX" value="$SER_TOUT_4XX"> sec</td>
		</tr><tr>
            <td nowrap id="accum_intvl">Accumulator interval</td>
            <td id="accum_intvl"><input class="input" name="ser_accum_intvl_4XX" value="$SER_ACCUM_INTVL_4XX"> ms</td>
        </tr><tr>
            <td nowrap id="accum_attempts">Accumulator attempts</td>
            <td id="accum_atts"><input class="input" name="ser_accum_atts_4XX" value="$SER_ACCUM_ATTS_4XX"></td>
        </tr><tr>
            <td nowrap id="recon_delay_4XX">Reconnect delay</td>
            <td id="recon_delay_4XX"><input class="input" name="ser_recon_delay_4XX" value="$SER_RECON_DELAY_4XX"> sec</td>
        </tr><tr>
            <td nowrap id="banner">Banner</td>
            <td id="banner"><input class="input" name="ser_banner_4XX" value="$SER_BANNER_4XX_DEC"></td>
        </tr>
</table></td>
EOF


echo "        </tr>"
[ "$HASDCC" = "1" ] && cat << EOF
	    <tr>
		<td width="50%" valign="top">
		    <table>
			<tbody>
			    <tr>
				<th colspan="2">Dry Contact Check</th>
			    </tr>
			    <tr>
				<td>Dry Contact Check</td>
				<td>
				    <select class="input" name="sec_mode">
					<option value="none" $sec_mode_none >Disabled</option>
					<option value="usbcom" $sec_mode_usb >USB-COM</option>
					<option value="serial" $sec_mode_ser >RS-232</option>
				    </select>
				</td>
			    </tr>
			    <tr>
				<td>Polling interval (sec)</td>
				<td><input class="input" name="sec_intvl" maxlength="3" value="$SEC_INTVL"></td>
			    </tr>
			    <tr>
				<td>Phone numbers</td>
				<td>
				    <input class="input" name="sec_phones" maxlength="120" value="$SEC_PHONES_DEC">
				</td>
			    </tr>
			    <tr>
				<td>Open message *</td>
				<td>
				    <input class="input" name="sec_open" maxlength="140" value="$SEC_OPEN_DEC">
				</td>
			    </tr>
			    <tr>
				<td>Close message *</td>
				<td>
				    <input class="input" name="sec_close" maxlength="140" value="$SEC_CLOSE_DEC">
				</td>
			    </tr>
			</tbody>
		    </table>
		</td>
	    </tr>
EOF
cat << EOF
	    </table></td></tr><tr>
		<td><input type="submit" name="apply" value="Apply"></td>
	    </tr>
      </table>
      </form>
      <script language="JavaScript" type="text/javascript">
      <!--
        document.input.ser_mode.focus();
        ModeChanged();
EOF
[ "$HAS485" = "1" ] && echo "        ModeChanged_4XX();"
cat << EOF
      //-->
      </script>
EOF

cat include/end.inc

