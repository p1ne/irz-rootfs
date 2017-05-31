#!/usr/bin/micropython

import uos
DIR = '/mnt/rwfs/upload/'

result = ''

ll = uos.ilistdir(DIR)
for l in ll:
        name=l[0]
        if l[1] != 4:
		result += '<tr>'
		result += '<td>%s</td>' % name
		result += '<td><u onclick="downloadFile(\'%s\')" style="cursor: pointer">%s</u></td>' % ( name, name )
		result += '<td><u onclick="deleteFile(\'%s\')" style="cursor: pointer">delete</u></td>' % name
		result += '<td><u onclick="setExecFile(\'%s\')" style="cursor: pointer">change exec</u></td>' % name
		result += '</tr>'
print(result)
