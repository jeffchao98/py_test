'''
Created on 2015/9/7

@author: SCaine
'''
from __future__ import print_function

import os
import pickle

import nester


man = []
other = []

def do_file_process():
    #if os.path.exists('sketch.txt'):#If-else way (with more complexity)
    try:#Try-except way
        the_file = open('sketch.txt')
        print('file opened')
        for each_line in the_file:
            #print(each_line, end="")
            '''
            #Idea 1
            #In case no split identify token in line, we need confirm before process
            if each_line.find(':')>-1:
                (role, line_spoken) = each_line.split(":", 1)
                #In Case mare than one token(:) in the same line
                #So we need restrict the time of split
                print(role, end="")
                print(' said: ', end="")
                print(line_spoken, end="")
            else:
                print(each_line, end="")
            '''
            #Idea 2-With try and exception catch
            try:
                (role, line_spoken) = each_line.split(":", 1)
                
                Storage_file_process(role, line_spoken)
                #In Case mare than one token(:) in the same line
                #So we need restrict the time of split
                print(role, end="")
                print(' said: ', end="")
                print(line_spoken, end="")
            except ValueError:
                #print(each_line, end="")
                pass
        #print(the_file.readline(), end="")#print all file without handle
        
        
        print(man)
        print(other)    #else:#If-else way
    except IOError:#Try-except way
        print('file missing')
    finally:
        #Check the value item exist then proceed close - or the inner exception occurs
        if 'the_file' in locals():
            the_file.close()
            print('file closed')
        
    
    
    creat_file_test()
    #create_file_real()
    
    
    pickle_data_test()
    pickle_data_real()
        
    pickle_data_recover()
    
    
def Storage_file_process(in_role='', in_line=''):
    if(in_role=='Man'):
        man.append(in_line)
    elif in_role == 'Other Man':
        other.append(in_line)
    else:
        pass

def pickle_data_recover():
    try:
        with open('man_data.out', "rb") as man_file, open('other_data.out', "rb") as other_file:
            new_man = pickle.load(man_file)
    except IOError as err:
        print('File established failed : ' + str(err))
    except pickle.PickleError as p_err:
        print('Pickle error : '+str(p_err))
    nester.print_list(new_man)

def pickle_data_test():
    try:
        with open('mydata.plckle', 'wb') as mypickledata:
            pickle.dump([1,2,'three'], mypickledata)
        with open('mydata.plckle', 'rb') as myreaddata:
            p_list = pickle.load(myreaddata)
    
        print(p_list)
    except IOError as err:
        pass
    except pickle.PickleError as p_err:
        print('Pickle error : '+str(p_err))
def pickle_data_real():
    try:
        #deal with the picker
        with open('man_data.out', "wb") as man_file, open('other_data.out', "wb") as other_file:
            pickle.dump(man, man_file)
            pickle.dump(other, other_file)
    except IOError as err:
        print('File established failed : ' + str(err))
    except pickle.PickleError as p_err:
        print('Pickle error : '+str(p_err))
    
    
 
def creat_file_test():
    try:
        out_file = open("data.out", "w")
        '''
        Mode
        w - create, rewrite if duplicate name existed
        a - append
        w+ - read/write when spec file status unknowed
        '''
        print("Ready for establish the file", file=out_file)
    except IOError:
        print('File established failed')
    #no matter exception events occur or not, the file close must proceed
    finally:
        out_file.close()
def create_file_real():
    try:
        #'with' includes data open/close/IOError handle of a file
        with open('man_data.out', "w") as man_file:
            #print(man, file=man_file)
            nester.print_list(man, man_file)#due to format
        with open('other_data.out', "w") as other_file:
            nester.print_list(other,False,0, other_file)
    except IOError as err:
        print('File established failed : ' + str(err))
    '''
    finally:
        man_file.close()
        other_file.close()
    '''
    #By 'with'(context management protocol) operate the I/O file, no need care the file close when final
