#!/usr/bin/env python

import cgi

import webprocess
import yate
import cgitb

cgitb.enable()

data_items = webprocess.get_from_store()
#print("Get data items:")
#print(data_items)

form_data = cgi.FieldStorage()
id_focus_item = form_data['which_athlete'].value

focus_item = data_items[id_focus_item]

print(yate.start_response())
print(yate.include_header("Data Detail"))
print(yate.header("Name:"+focus_item.name+", DOB:"+focus_item.dob+"."))
print(yate.para("The top 3 records: "))
print(yate.u_list(focus_item.top3()))
print(yate.include_footer({"Home":"/index.html", "select another item":"generate_web_list.py"}))