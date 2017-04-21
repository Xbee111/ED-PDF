#!/usr/bin/python3.5

import cgi
import cgitb; cgitb.enable()
import shutil
import os, sys

print ("Content-Type: text/html")
form = cgi.FieldStorage()
url = "http://192.168.84.137/msf.html?status=uploaded"
print ("Location: %s" % url)
print()

with open('filetheft.rc','w') as fileOutput:
      fileOutput.write(form.getvalue("exploit"))
      fileOutput.write("\n")
      fileOutput.write(form.getvalue("srvhost"))
      fileOutput.write("\n")
      fileOutput.write(form.getvalue("uripath"))
      fileOutput.write("\n")
      fileOutput.write(form.getvalue("run"))


