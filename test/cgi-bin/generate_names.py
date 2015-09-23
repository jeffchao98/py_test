#!/usr/bin/env python


import json
import webprocess
import yate

#names = webprocess.get_name_from_store()
names = webprocess.get_namesID_from_store()

print(yate.start_response('application/json'))
print(json.dumps(sorted(names)))