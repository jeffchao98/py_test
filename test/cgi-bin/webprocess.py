import pickle
#test
from customobj import customobj_inh
import urllib
from http.server import HTTPServer, CGIHTTPRequestHandler
import yate

import sqlite3

db_name = 'cgi-bin/coachdata.sqlite'

def do_web_process():
    #test functions for yate.py
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

def get_namesID_from_store():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    results = cursor.execute("""SELECT name, id FROM athletes""")
    response = results.fetchall()
    connection.close()
    return(response)
def get_athlete_from_id(athlete_id):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    results = cursor.execute("""SELECT name, dob FROM athletes WHERE id=?""",(athlete_id,))
    (name, dob) = results.fetchone()
    results = cursor.execute("""SELECT value FROM timing_data WHERE athlete_id=?""",(athlete_id,))
    data = [row[0] for row in results.fetchall()]
    
    #Due to unknown order inside database, so we need sorted the data via customobj_inh class before display
    m_tmp_item = customobj_inh(name, dob, data)
    response = {'Name':   m_tmp_item.name,
                'DOB':    m_tmp_item.dob,
                'data':   m_tmp_item.clean_data,
                'top3':   m_tmp_item.top3()}
    connection.close()
    return(response)
def get_name_from_store():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    results = cursor.execute("""SELECT name FROM athletes""")
    response = [row[0] for row in results.fetchall()]
    connection.close()
    return(response)
'''
    m_item = get_from_store()
    list_trsult = [m_item[each_item].name for each_item in m_item]
    return(list_trsult)
'''
    