# Only runnable before Python3

print('//================Basic Output(available before Python3)')

#Basic calaulate
print 3+5
print 100-50
print 13*14
print 5/2
print 8**3
print 13 % 2

#Input Reference
x = input('Please input a number:')
print x

#String Handle
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
#Encode
print len(u'Hi,\u0020Eric')
print len('Hi\nEric')

a = [1, 3, 'abc', 7, "xyz"]
print a[3]
print a[-2]
print a[1:4]

#Dictionary
d = {'python': 'Large constricting snakes.', 'ruby': 'A precious stone that is a red corundum.'}
print d['python']
print len(d)
#-Add
d['game'] = 'Activity engaged in for diversion or amusement.'
print d
#-Edit
d['python'] = 'A very powerful scripting language.'
print d
#-Delete
del d['game']
print d
#Print non-menber
#print d['never_seen']
