#!/usr/bin/env python

from __future__ import print_function

import cgi
import os
import time
import sys
import yate

print(yate.start_response('text/plain'))
addr = os.environ['REMOTE_ADDR']
host = os.environ['REMOTE_HOST']
method = os.environ['REQUEST_METHOD']
cut_time = time.asctime(time.localtime())

print("HOST = "+host+", ADDR = "+addr+", CUT_TIME = "+cut_time+": METHOD = "+method+": ", end='', file=sys.stderr)

form=cgi.FieldStorage()
for each_form_item in form.keys():print(each_form_item+'->'+form[each_form_item].value, end='', file=sys.stderr)
#return line when error occur
print(file=sys.stderr)
print('OK.')
