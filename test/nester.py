'''
Created on 2015/9/6
 
author: SCaine
'''
from __future__ import print_function

import sys


#sys.stdout - may allow output the content to screen or file if specified
def print_list(input_list, bEnable=False, level=0, fh=sys.stdout):
    for each_element in input_list:
        if isinstance(each_element, list):
            print_list(each_element,bEnable,level+1,fh)
        else:
            if bEnable == True:
                for num in range(level):
                    print("\t", end="", file=fh)
            print(each_element, file=fh)
    