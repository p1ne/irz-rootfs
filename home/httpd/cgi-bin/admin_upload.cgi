#!/bin/sh

./begin $0
echo "</td><td colspan=\"3\" valign=\"top\">"
cat include/js.inc

[ ! -d /mnt/rwfs/upload/ ] && mkdir /mnt/rwfs/upload/

cat << EOF
      function CheckForm() {
	if (GetValue(document.getElementsByName("filename")[0]).length == 0) {
	  alert("No input file specified.");
	  document.getElementsByName("filename")[0].focus();
	  return false;
	}
	return true;
      }
      -->
      </script>
      <form onsubmit="return CheckForm();" action="admin_upload_exec.cgi" method="post" enctype="multipart/form-data">
      <table width="100%" cellspacing="0" cellpadding="5" border="3">
	<tr>
	  <td class="title" align="center">
	    <b>Uploaded files: /mnt/rwfs/upload/</b>
	  </td>
	</tr>
	<tr>
	  <td>
	    <table>
	      <tr>
		<td nowrap>
EOF

echo "<table><tr><td style=\"color: blue\">Free space: `df -h | awk '/mtdblock6/{print \$4}'`</td></tr></table>"
echo "<table width=\"100%\" cellspacing=\"5\" cellpadding=\"5\">"

./ls.py

cat << EOF		
		</table>
	      </tr>
	    </table>
	  </td>
	</tr>
	<tr>
	  <td>
	    <table>
	      <tr>
		<td nowrap>Select file</td>
		<td><input type="file" size="50" name="filename"></td>
	      </tr>
	    </table>
	  </td>
	</tr>
	<tr>
	  <td><input type="submit" name="upload" value="Upload"></td>
	</tr>
      </table>
      </form>
      <script language="JavaScript" type="text/javascript">
      <!--
      document.getElementsByName("filename")[0].focus();
      function deleteFile(name){
      	f = document.createElement('form');
      	f.style.display = 'none';
      	f.setAttribute('method', 'post');
      	f.setAttribute('action', 'admin_upload_delete_exec.cgi');
      	d = document.createElement('input');
      	d.setAttribute('name', 'delete');
      	d.setAttribute('type', 'hidden');
      	d.setAttribute('value', name);
      	f.appendChild(d);
      	document.body.appendChild(f);
      	f.submit();
      }
      
      function setExecFile(name){
      	f = document.createElement('form');
      	f.style.display = 'none';
      	f.setAttribute('method', 'post');
      	f.setAttribute('action', 'admin_upload_delete_exec.cgi');
      	d = document.createElement('input');
      	d.setAttribute('name', 'exec');
      	d.setAttribute('type', 'hidden');
      	d.setAttribute('value', name);
      	f.appendChild(d);
      	document.body.appendChild(f);
      	f.submit();
      }
      
      function downloadFile(name){
      	f = document.createElement('form');
      	f.style.display = 'none';
      	f.setAttribute('method', 'post');
      	f.setAttribute('action', 'admin_upload_delete_exec.cgi');
      	d = document.createElement('input');
      	d.setAttribute('name', 'load');
      	d.setAttribute('type', 'hidden');
      	d.setAttribute('value', name);
      	f.appendChild(d);
      	document.body.appendChild(f);
      	f.submit();
      }
      //-->
      </script>
EOF

cat include/end.inc

