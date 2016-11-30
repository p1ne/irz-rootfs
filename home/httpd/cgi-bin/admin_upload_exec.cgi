#!/usr/bin/python
# -*- coding: utf8 -*-

import cgi, os, time

DIR = '/mnt/rwfs/upload/'

form = cgi.FieldStorage()

if not 'filename' in form:
	message = 'No file uploaded'
else:
	fn, ext = os.path.splitext(form['filename'].filename.replace(' ','_'))
	try:
		fn = fn.encode('utf8')
		message = '"%s%s" - saved' % (fn, ext)
	except:
		nfn = str(int(time.time()))
		message = 'File "%s" renamed to "%s"- saved' % (fn+ext, nfn+ext)
		fn = nfn
	f = form['filename'].file.read()
	st = os.statvfs('/mnt/rwfs/upload')
	free = st.f_bavail * st.f_frsize
	if free > len(f):
		try:
			if '\0' in f:
				print open(DIR + fn + ext, 'wb').write(f)
			else:
				print open(DIR + fn + ext, 'w').write(f.replace('\r\n', '\n'))
		except Exception as err:
			message = 'ERR: %s' % err
	else:
		message = "Not enough space!"

print """\
Content-Type: text/html\n
<html><body>
Please wait...<hr>
<pre>%s</pre>
<meta http-equiv="refresh" content="20;url=admin_upload.cgi"/>
<hr><a href="admin_upload.cgi">Return</a>
</body></html>
""" % message
