#!/usr/bin/python

import os
DIR = '/mnt/rwfs/upload/'

result = ''
ll = os.popen('ls -1lh %s' % DIR).readlines()
for l in ll:
	l = l.split()
	l.remove(l[1])
	result += '<tr>'
	result += '<td>%s</td><td>%s</td><td>%s</td>' % (l[0], l[1], ' '.join(l[2:5]))
	result += '<td><u onclick="downloadFile(\'%(name)s\')" style="cursor: pointer">%(name)s</u></td>' % {'name': os.path.basename(l[-1:][0])}
	result += '<td><u onclick="deleteFile(\'%(name)s\')" style="cursor: pointer">delete</u></td>' % {'name': os.path.basename(l[-1:][0])}
	result += '<td><u onclick="setExecFile(\'%(name)s\')" style="cursor: pointer">change exec</u></td>' % {'name': os.path.basename(l[-1:][0])}
	result += '</tr>'
print result
