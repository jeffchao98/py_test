"""
Python Self Train Project
Start From 2015.4
References:
1."using-python" - https://code.google.com/p/using-python/wiki/Welcome
2."Welcome to Python.org" - https://www.python.org/
3.Head First Python, O'RELLY
4."Head First Labs" - http://www.headfirstlabs.com/
"""


import customobj
import dataprocess 
import fileprocess
import nester
import webprocess 
## Only runnable BEFORE Python3
#import BasicOutPutP2
import ProcedureControl
import SelfDefineFunction



#Simple output
## Only runnable before Python3
#BasicOutPutP2

##Procedure Control
ProcedureControl

movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, 
                ["Graham Chapman", ["Michael Palin", "John Cleese",
                        "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

#Define Function
SelfDefineFunction.my_function()
print('//================Do self-function with recursive')
SelfDefineFunction.print_list(movies)




print('//================Public-available module')
nester.print_list(movies,0)

#File process
#File open, read and close / try and exception catch and finally
#'with'(context management protocol)/pickle
print('//================File process')
fileprocess.do_file_process()

#Data process
#sort(In-place / Copied), split, set, List Comprehension
print('//================Data process')
dataprocess.do_data_process()

#Custom Data Object
#dictionary, Object class, Inherit class
print('//================Custom Object')
customobj.do_customobj()

#web process
print('//================Web related process')
webprocess.do_web_process()