#!/usr/bin/env python
import webprocess
import yate
#Due to the sqlite solution for storage, no need file handle anymore
#import glob

import cgitb

cgitb.enable()


#data_files = glob.glob("data/*.txt")
#ref_datas = webprocess.put_to_store(data_files)
ref_datas = webprocess.get_namesID_from_store()

print(yate.start_response())
print(yate.include_header("List of Data"))
print(yate.start_form("generate_timing_data.py"))
print(yate.para("Select an object from below: "))

for each_ref_data in ref_datas:
    #print(yate.radio_button("which_athlete", ref_datas[each_ref_data].name))
    print(yate.radio_button_id("which_athlete", each_ref_data[0],each_ref_data[1]))
print(yate.end_form("Select"))

print(yate.include_footer({"Home":"/index.html"}))