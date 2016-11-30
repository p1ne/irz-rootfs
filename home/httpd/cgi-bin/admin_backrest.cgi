#!/bin/sh
./begin $0

echo "</td><td colspan=\"3\" valign=\"top\">"
cat include/js.inc

cat << EOF
      function CheckForm() {
    if (GetValue(document.input.config).length == 0) {
      alert("No input file specified.");
      Focus(document.input.config);
      return false;
    }
    return true;
      }
      //-->
      </script>
      <table width="100%" cellspacing="0" cellpadding="5" border="3">
    <tr>
      <td class="title" align="center"><b>Backup/Restore configuration</b></td>
    </tr>
    <tr>
      <td>
        <form name="input2" action="admin_backrest_backup.cgi" method="post" enctype="multipart/form-data">
        <table>
          <tr>
            <td nowrap>Backup configuration:</td>
            <td><input type="submit" name="backup" value="Backup"></td>
          </tr>
        </table>
        </form>
      </td>
    </tr>
    <tr>
      <td>
       <form name="input" onsubmit="return CheckForm();" action="admin_backrest_restore.cgi" method="post" enctype="multipart/form-data">
        <table>
          <tr>
            <td nowrap>Restore configuration:</td>
            <td><input type="file" size="50" name="config"></td>
            <td><input type="submit" name="restore" value="Restore"></td>
          </tr>
        </table>
        </form>
      </td>
    </tr>
    <tr>
      <td>
       <form name="input" onsubmit="return CheckForm();" action="admin_backrest_restusb.cgi" method="post" enctype="multipart/form-data">
        <table>
          <tr>
            <td nowrap>Load configuration from USB-flash:</td>
            <td><input type="submit" name="restore" value="Load"></td>
          </tr>
        </table>
        </form>
      </td>
    </tr>
  </table>
      <script language="JavaScript" type="text/javascript">
      <!--
      document.input.firmware.focus();
      //-->
      </script>
EOF

cat include/end.inc

