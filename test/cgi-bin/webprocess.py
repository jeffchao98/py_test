import pickle
#test
from customobj import customobj_inh
import urllib
from http.server import HTTPServer, CGIHTTPRequestHandler
import yate




def do_web_process():
    #test functions of yate.py
    print(yate.start_response())
    print(yate.start_response("text/plain"))
    print(yate.start_response("application/json"))
    print(yate.include_header("Test title for my web application in python test"))
    print(yate.include_footer({'Home':'/index.html', 'Select':'/cgi-bin/select.py'}))
    print(yate.start_form("/cgi-bin/process-athlete.py"))
    #print(urllib.request.urlopen('http://192.168.0.1/test.py', urllib.parse.urlencode({'a':'c'})))
    print(urllib.parse.urlencode({'a':'c'}))
    
    the_files = ['sarah2.txt', 'james2.txt', 'mikey2.txt']
    data = put_to_store(the_files)
    for each_data in data:
        print(data[each_data].name+' '+data[each_data].dob)
    data_copy = get_from_store()
    for each_data in data_copy:
        print(data_copy[each_data].name+' '+data_copy[each_data].dob)
    #start simple http server for test
    simple_http_server_test()
    pass

def simple_http_server_test():
    port = 8080

    httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
    print("Starting simple_httpd on port: " + str(httpd.server_port))
    httpd.serve_forever()

def process_files_obj(f_name):
    try:
        with open(f_name) as tFile:
            data = tFile.readline()
            tmp_list = data.strip().split(',')
            return(customobj_inh(tmp_list.pop(0), tmp_list.pop(0), tmp_list))
    except IOError as err:
        print('File error: '+str(err))
        return(None)

def put_to_store(files_list):
    all_referenses = {}
    
    for each_file in files_list:
        a_file = process_files_obj(each_file)
        all_referenses[a_file.name]=a_file
    try:
        with open('athletes.pickle', 'wb') as a_file_p:
            pickle.dump(all_referenses, a_file_p)
    except IOError as ioerr:
        print('File error(put_to_store): '+str(ioerr))
    
    return (all_referenses)
    pass
def get_from_store():
    all_referenses = {}
    try:
        with open('athletes.pickle', 'rb') as a_file_p:
            all_referenses = pickle.load(a_file_p)
    except IOError as ioerr:
        print('File error(get_from_store): '+str(ioerr))

    return (all_referenses)
def get_name_from_store():
    m_item = get_from_store()
    list_trsult = [m_item[each_item].name for each_item in m_item]
    return(list_trsult)
    