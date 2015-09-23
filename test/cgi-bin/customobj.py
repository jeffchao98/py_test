'''
Created on 2015/9/10

@author: SCaine
'''

def do_customobj():
    
    
    #dictionary way
    d_james = process_files('testdata/james2.txt')
    d_julie = process_files('testdata/julie2.txt')
    d_mikey = process_files('testdata/mikey2.txt')
    d_sarah = process_files('testdata/sarah2.txt')
    
    '''
    d_james = list_to_dic(l_james)
    d_julie = list_to_dic(l_julie)
    d_mikey = list_to_dic(l_mikey)
    d_sarah = list_to_dic(l_sarah)
    '''
    print(d_sarah['Name']+"'s fastest times are: "+str(d_sarah['Times'][0:3]))
    
    
    #custom object way (inherit)
    o_james = process_files_obj('testdata/james2.txt')
    print(o_james.name+"'s fastest times are: "+str(o_james[0:3]))
    
    
    #Test Created Custom Object
    zwei = customobj('TestItem')
    zwei.add_time('1.31')
    print(zwei.top3())
    zwei.add_times(['2.22', "1-21", '2:22'])
    print(zwei.top3())
    
    #Test Created Inherit Object
    zwei_inh = customobj_inh('TestItem')
    zwei_inh.append('1.31')
    print(zwei_inh.top3())
    zwei_inh.extend(['2.22', "1-21", '2:22'])
    print(zwei_inh.top3())
    
    pass

class customobj:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times
        pass
    def top3(self):
        return(sorted(set(sanitize(t) for t in self.times))[0:3])
    def add_time(self, time_val):
        self.times.append(time_val)
    def add_times(self, l_input_list):
        self.times.extend(l_input_list)

class customobj_inh(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        #Inherit Step 1 : initial the class which current object derived
        list.__init__([])
        #Inherit Step 2 : import the input value
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)
        pass
    def top3(self):
        return(sorted(set(sanitize(t) for t in self))[0:3])
    @property
    def clean_data(self):
        return(sorted(set(sanitize(t) for t in self)))
    def as_dict(self):
        return({'Name':self.name, 'DOB':self.dob, 'Top3':self.top3()})
    #Since the json method cannot handle custom items, we need transfer it as dict type 

#In : file, Out : object
def process_files_obj(f_name):
    try:
        with open(f_name) as tFile:
            data = tFile.readline()
            tmp_list = data.strip().split(',')
            return(customobj_inh(tmp_list.pop(0), tmp_list.pop(0), tmp_list))
    except IOError as err:
        print('File error: '+str(err))
        return(None)

#In : file, Out : set
def process_files(f_name):
    try:
        with open(f_name) as tFile:
            data = tFile.readline()
            tmp_list = data.strip().split(',')
            return(list_to_dic(tmp_list))
    except IOError as err:
        print('File error: '+str(err))
        return(None)

def list_to_dic(input_list):
    tmp_dic={}
    
    tmp_dic['Name'] = input_list.pop(0)
    tmp_dic['DOB'] = input_list.pop(0)
    tmp_dic['Times'] = sorted(set(sanitize(t) for t in input_list))
    
    return(tmp_dic)

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
