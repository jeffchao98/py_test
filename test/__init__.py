"""
Python Self Train Project
Start From 2015.4
References:
1."using-python" - https://code.google.com/p/using-python/wiki/Welcome
2."Welcome to Python.org" - https://www.python.org/
3.Head First Python, O'RELLY
4."Head First Labs" - http://www.headfirstlabs.com/
"""

#Simple output
print 3+5
print 100-50
print 13*14
print 5/2
print 8**3
print 13 % 2
x = input('Please input a number:')
print x
x = 'Hello, world'
print x
x = 'I\'m Eric.'
print x
x = "I'm Eric."
print x
file_path = 'C:\\Documents and Settings\\ericsk\\test.dat'
print file_path
file_path = r'C:\Documents and Settings\ericsk\test.dat'
print file_path
x = 'Hello, '
y = 'World'
z = x+y
print x+y
print z
x = 'Cat'
print x * 3
x = 'Hello, World.'
print x[7]
print 'hello'[0:2]
x = 'Hello, World.'
print x[-2]
print x[4:-3]# From Left 5 to Right 3
x = 'Hello, World.'
print len(x)
x = u'Hi,\u0020Er\tic'
print x

print len(u'Hi,\u0020Eric')
print len('Hi\nEric')

a = [1, 3, 'abc', 7, "xyz"]
print a[3]
print a[-2]
print a[1:4]

d = {'python': 'Large constricting snakes.', 'ruby': 'A precious stone that is a red corundum.'}
print d['python']
print len(d)
#Add
d['game'] = 'Activity engaged in for diversion or amusement.'
print d
#Edit
d['python'] = 'A very powerful scripting language.'
print d
#Delete
del d['game']
print d
#Print non-menber
#print d['never_seen']


# if - else procedure
#x = input('Please enter a integer: ')

import customobj
import dataprocess 
import fileprocess
import nester
import webprocess 


x = 0
if x > 0:
    print ('******Case input great than 0*******')
    print ('You have entered a positive integer.')
    print ('************************************') 
elif x == 0:
    print ('*******Case input equal as 0********')
    print ('You have entered zero.')
    print ('************************************') 
else:
    print ('******Case input less than 0********')
    print ('You have entered a negative integer.')
    print ('************************************') 

# For - Loop usage
d = {'python': 'Large constricting snakes.', 'ruby': 'A precious stone that is a red corundum.'}
a = [1, 3, 'abc', 7, "xyz"]

for each_element in a:
    print(each_element)
for each_element in d:
    print(each_element)
for each_element in d:
    print(d[each_element])
for num in range(5):
    print(num)
for num in range(5):
    print(a[num])
    
# while -loop usage
count = 0
while count<3:
    print(d)
    count = count+1

print(isinstance(a, list))
print(isinstance(d, list))
print(isinstance(x, list))

#Define Function
def my_function():
    print('Hi, my_function')
print('Do self-function')
my_function()

#Define Function-recursive
movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, 
                ["Graham Chapman", ["Michael Palin", "John Cleese",
                        "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
'''
def print_list(input_list):
    for each_element in input_list:
        if isinstance(each_element, list):
            print_list(each_element)
        else:
            print(each_element)
'''

nester.print_list(movies,0)

#File process
#File open, read and close / try and exception catch and finally
#'with'(context management protocol)/pickle
fileprocess.do_file_process()

#Data process
#sort(In-place / Copied), split, set, List Comprehension
dataprocess.do_data_process()

#Custom Data Object
#dictionary, Object class, Inherit class
customobj.do_customobj()

#web process
webprocess.do_web_process()