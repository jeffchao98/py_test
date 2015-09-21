#!/usr/bin/env python
import webprocess
import yate
import glob

import cgitb

cgitb.enable()


data_files = glob.glob("data/*.txt")
ref_datas = webprocess.put_to_store(data_files)

print(yate.start_response())
print(yate.include_header("List of Data"))
print(yate.start_form("generate_timing_data.py"))
print(yate.para("Select an object from below: "))

for each_ref_data in ref_datas:
    print(yate.radio_button("which_athlete", ref_datas[each_ref_data].name))
print(yate.end_form("Select"))

print(yate.include_footer({"Home":"/index.html"}))