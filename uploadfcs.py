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

if 'file_3' in form:
   filefield = form['file_3']
   if not isinstance(filefield, list):
      filefield = [filefield]

   for fileitem in filefield:
       if fileitem.filename:
          fn = os.path.basename(fileitem.filename)
          # save file
          with open('/home/PDF/InEmbed/' + fn, 'wb') as f:
              shutil.copyfileobj(fileitem.file, f)


