#!/bin/sh

./begin $0
. /etc/version

echo "</td><td colspan=\"3\" valign=\"top\">"

cat << EOF
      <table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
	  <td class="title" align="center">
	    <b>Report a problem</b>
	  </td>
	</tr>
	<tr>
	  <td>
		<center>
<script language="javascript">
    function OnSubmitSet(frm){
        frm.action="admin_report_set.cgi"
        frm.submit();
    }
    function OnSubmitSave(frm){
        frm.action="admin_report_save.cgi"
        frm.submit();
    }
    function OnSubmitRemove(frm){
        frm.action="admin_report_remove.cgi"
        frm.submit();
    }
</script>
		<table width="100%" border="0"><tr><td>
		<p><textarea rows="30" cols="110" name="report" readonly>
EOF
en="disabled"
if [ -f /tmp/report ]; then
    cat /tmp/report
    en=""
else
    echo Click \"Generate Report\" button to create report.
    echo NOTE: Report includes all your secrets, keys and passwords!
    echo You must remove them manually in order to keep your privacy!
fi
cat << EOF
</textarea></p>
EOF
if [ -z "$en" ]; then
    echo "<p><b><a href=\"mailto:support@radiofid.ru?Subject=${MODEL}_REPORT&Body=Do%20not%20forget%20to%20attach%20generated%20report.\">Click here to send e-mail to support</a></b></p>"
fi
cat << EOF
		</center>
		</td></tr></table>
	  </td>
	</tr>
	<tr>
	  <td>
      <form name="input" action="admin_report_set.cgi" method="POST">
	  <input type="submit" name="genreport" value="Generate Report" onclick="OnSubmitSet(this.form);">
      <input type="submit" name="savereport" value="Save Report" $en onclick="OnSubmitSave(this.form);">
      <input type="submit" name="removereport" value="Remove Report" $en onclick="OnSubmitRemove(this.form);">
	  </form></td>
	</tr>
    </table>
    <script language="JavaScript" type="text/javascript">
       <!--
       document.input.report.focus();
       //-->
    </script>
EOF

cat include/end.inc

