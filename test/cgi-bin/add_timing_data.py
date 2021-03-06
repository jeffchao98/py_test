#!/usr/bin/env python

from __future__ import print_function

import cgi
import os
import time
import sys
import yate

import sqlite3


print(yate.start_response('text/plain'))

###Information Code Start###
addr = os.environ['REMOTE_ADDR']
host = os.environ['REMOTE_HOST']
method = os.environ['REQUEST_METHOD']
cut_time = time.asctime(time.localtime())

print("HOST = "+host+", ADDR = "+addr+", CUT_TIME = "+cut_time+": METHOD = "+method+": ", end='', file=sys.stderr)
###Information Code End###

form=cgi.FieldStorage()
for each_form_item in form.keys():
    print(each_form_item+'->'+form[each_form_item].value, end='', file=sys.stderr)

the_id = form['Athlete'].value
the_time = form['Time'].value

connection = sqlite3.connect('cgi-bin/coachdata.sqlite')
cursor = connection.cursor()
cursor.execute("INSERT INTO timing_data (athlete_id, value) VALUES (?, ?)",
                       (the_id, the_time))
connection.commit()
connection.close()



#return line when error occur
print(file=sys.stderr)

#Print OK when complete
print('OK.')
