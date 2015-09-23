
x = 0

d = {'python': 'Large constricting snakes.', 'ruby': 'A precious stone that is a red corundum.'}
a = [1, 3, 'abc', 7, "xyz"]

## if - else procedure
def testIfElse():
    #x = input('Please enter a integer: ')
    
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
   
## For - Loop usage
def testForLoop():
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
    
## while -loop usage
def testWhileLoop():
    count = 0
    while count<3:
        print(d)
        count = count+1
    
    print(isinstance(a, list))
    print(isinstance(d, list))
    print(isinstance(x, list))

print ('//================= If - Else Procedure Control')
testIfElse()
print ('//================= For Loop Output')
testForLoop()
print ('//================= While Loop Output')
testWhileLoop()

