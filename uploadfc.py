#!/usr/bin/python3

import cgi
import cgitb; cgitb.enable()
import shutil
import os, sys

print ("Content-Type: text/html")
form = cgi.FieldStorage()
url = "http://192.168.84.137/index.html?status=uploaded"
print ("Location: %s" % url)
print()

filedata = form['file_1']

if filedata.file:
    fn = os.path.basename(filedata.filename)
    # save file
    with open('/home/PDF/InAnalysis/' + fn, 'wb') as f:
            shutil.copyfileobj(filedata.file, f)
