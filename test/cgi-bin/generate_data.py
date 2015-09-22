#!/usr/bin/env python

import cgi
import json
import webprocess
import yate
import sys
import customobj

import cgitb

cgitb.enable()


m_items = webprocess.get_from_store()
#get request 
m_form_data = cgi.FieldStorage()
#split the specify condition from the request
str_item_name = m_form_data['which_athlete'].value
print(yate.start_response('application/json'))
print(json.dumps(m_items[str_item_name].as_dict()))

#without mobile test environment, please use the address below
#http://localhost:8080/cgi-bin/generate_data.py?which_athlete=Sarah%20Sweeney