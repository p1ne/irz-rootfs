#!/bin/sh
[ -e /etc/version ] && . /etc/version
K_VERSION=`uname -a`
TIME=`echo $TIME | sed -e 's/-/:/g'`
./begin $0

echo "</td><td colspan=\"3\" valign=\"top\">"
cat include/js.inc

[ -x `which micropython` ] && PYTHON_VERSION="<tr><td>MicroPython version:</td><td>`./ver.py 2>&1`</td></tr>"
cat << EOF
      function CheckForm() {
	if (GetValue(document.input.firmware).length == 0) {
	  alert("No input file specified.");
	  Focus(document.input.firmware);
	  return false;
	}
	return true;
      }
      //-->
      </script>
      <form name="input" onsubmit="return CheckForm();" action="admin_update_exec.cgi" method="post" enctype="multipart/form-data">
      <table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
	  <td class="title" align="center">
	    <b>Update Firmware</b>
	  </td>
	</tr>
	<tr>
	  <td>
	    <table>
	      <tr>
		<td nowrap>
		<table width="100%" cellspacing="5">
        <tr><td>Router model:</td><td>$MODEL</td></tr>
        <tr><td>Firmware version:</td><td>$MAJOR.$MINOR.$BUILD.$BRANCH</td></tr>
        <tr><td>Build date:</td><td>$DATE&nbsp;$TIME</td></tr>
        <tr><td>Commit hash:</td><td>$COMMIT</td></tr>
		<tr><td>Kernel version:</td><td>$K_VERSION</td></tr>
        $PYTHON_VERSION    
        </table>
	      </tr>
	    </table>
	  </td>
	</tr>
	<tr>
	  <td>
	    <table>
	      <tr>
		<td nowrap>New Firmware</td>
		<td><input type="file" size="50" name="firmware"></td>
	      </tr>
	    </table>
	  </td>
	</tr>
	<tr>
	  <td><input type="submit" name="update" value="Update"></td>
	</tr>
      </table>
      </form>
      <script language="JavaScript" type="text/javascript">
      <!--
      document.input.firmware.focus();
      //-->
      </script>
EOF

cat include/end.inc

