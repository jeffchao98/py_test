#!/usr/bin/env python

import cgi

import webprocess
import yate
import cgitb

cgitb.enable()

#data_items = webprocess.get_from_store()
#print("Get data items:")
#print(data_items)

form_data = cgi.FieldStorage()
id_focus_item = form_data['which_athlete'].value

m_focus_item = webprocess.get_athlete_from_id(id_focus_item)

#focus_item = data_items[id_focus_item]

print(yate.start_response())
print(yate.include_header("Data Detail"))
#print(yate.header("Name:"+focus_item.name+", DOB:"+focus_item.dob+"."))
print(yate.header("Name:"+m_focus_item['Name']+", DOB:"+m_focus_item['DOB']+"."))
print(yate.para("The top 3 records: "))
print(yate.u_list(m_focus_item['top3']))
#Show all data(without duplicate item)
print(yate.para("The entire set of timing data is: " + str(m_focus_item['data']) +" (duplicates removed)."))

print(yate.do_form_with_hide('add_timing_data.py', ['Time'], {'Athlete':id_focus_item} ,text='Submit'))

print(yate.include_footer({"Home":"/index.html", "select another item":"generate_web_list.py"}))