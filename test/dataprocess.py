'''
Created on 2015/9/9

@author: SCaine
'''
def do_data_process():
    print('//==================do_data_process(Value Only)')
    d_james = process_files('testdata/james_o.txt')
    d_julie = process_files('testdata/julie_o.txt')
    d_mikey = process_files('testdata/mikey_o.txt')
    d_sarah = process_files('testdata/sarah_o.txt')
    
    d_james_s = []
    d_julie_s = []
    d_mikey_s = []
    d_sarah_s = []
    
    d_james_s = data_sync_transfer(d_james)
    d_julie_s = data_sync_transfer(d_julie)
    d_mikey_s = data_sync_transfer(d_mikey)
    d_sarah_s = data_sync_transfer(d_sarah)
    
    #Print sorted(copy sort) list
    #print(sorted(d_james_s))
    #print(sorted(d_julie_s))
    #print(sorted(d_mikey_s))
    #print(sorted(d_sarah_s))
    
    d_james_s.sort()
    d_julie_s.sort()
    d_mikey_s.sort()
    d_sarah_s.sort()
    
    d_james_s_u = filter_duplicate(d_james_s)
    d_julie_s_u = filter_duplicate(d_julie_s)
    d_mikey_s_u = filter_duplicate(d_mikey_s)
    d_sarah_s_u = filter_duplicate(d_sarah_s)
    
    print(d_james_s_u[0:3])
    print(d_julie_s_u[0:3])
    print(d_mikey_s_u[0:3])
    print(d_sarah_s_u[0:3])
    
    
    
    pass

def filter_duplicate(input_list):
    out_list = []
    #filter the duplicate items idea 01 : check before append to the new list
    '''
    for each_t in input_list:
        if each_t not in out_list:
            out_list.append(each_t)
    '''
    #filter the duplicate items idea 02 : use the "set" characteristic - no duplicate allow left
    #However, you must transfer the 'set' type back to 'list' by list(_set_) and reorder it again
    #Sort MUST proceed after transfer to list COMPLETE, or out_list will remain nothing
    out_list = list(set(input_list))
    out_list.sort()
    return(out_list)


def data_sync_transfer(input_list):
    #Standard Way
    '''
    synced_list=[]
    
    for each_t in input_list:
        synced_list.append(sanitize(each_t))
    return(synced_list)
    '''
    
    #Shorter Way
    return([sanitize(each_t) for each_t in input_list])

def process_files(f_name):
    try:
        with open(f_name) as tFile:
            data = tFile.readline()
            return(data.strip().split(','))
    except IOError as err:
        print('File error: '+str(err))
        return(None)

def sanitize(input_time):#sync the splitter
    outRes = input_time
    if '-' in input_time:
        spiltter  = '-'
    elif ':' in input_time:
        spiltter = ':'
    else:
        return(outRes)
    
    (m_tmp, s_tmp) = input_time.split(spiltter)
    outRes = (m_tmp + '.' + s_tmp)
    return(outRes)
