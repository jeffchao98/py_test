from string import Template

def start_response(resp="text/html"):
    return('Content-type: ' + resp + '\n\n')

#Generate HTML title
def include_header(the_title):
    with open('templates/header.html') as headf:
        head_text = headf.read()
    header = Template(head_text)
    return(header.substitute(title=the_title))
#Generate HTML tail part
def include_footer(the_links):
    with open('templates/footer.html') as footf:
        foot_text = footf.read()
    link_string = ''
    for key in the_links:
        link_string += '<a href="' + the_links[key] + '">' + key + '</a>&nbsp;&nbsp;&nbsp;&nbsp;'
    footer = Template(foot_text)
    return(footer.substitute(links=link_string))

#Generate the HTML form start
def start_form(the_url, form_type="POST"):
    return('<form action="' + the_url + '" method="' + form_type + '">')

#Generate the HTML form end
def end_form(submit_msg="Submit"):
    return('<p></p><input type=submit value="' + submit_msg + '"></form>')


#Generate the HTML radio button
def radio_button(rb_name, rb_value):
    return('<input type="radio" name="' + rb_name +
                             '" value="' + rb_value + '"> ' + rb_value + '<br />')
def radio_button_id(rb_name, rb_value, rb_id):
    return('<input type="radio" name="' + rb_name +
                             '" value="' + str(rb_id) + '"> ' + rb_value + '<br />')
#Generate the HTML list
def u_list(items):
    u_string = '<ul>'
    for item in items:
        u_string += '<li>' + item + '</li>'
    u_string += '</ul>'
    return(u_string)


#Generate HTML header
def header(header_text, header_level=2):
    return('<h' + str(header_level) + '>' + header_text +
           '</h' + str(header_level) + '>')

def para(para_text):
    return('<p>' + para_text + '</p>') 
def create_inputs(input_list):
    html_inputs=''
    for each_input in input_list:
        html_inputs = html_inputs+'<input type="text" name="'+\
        each_input+'"size=40>'
    return(html_inputs)

def do_form(name, the_inputs, method="POST", text="Submit"):
    with open('templates/form.html') as formf:
        form_text = formf.read()
    inputs=create_inputs(the_inputs)
    form=Template(form_text)
    
    return(form.substitute(cgi_name=name, http_method=method, list_of_inputs=inputs, submit_text=text))
def do_form_with_hide(name, the_inputs,the_inputs_hide, method="POST", text="Submit"):
    with open('templates/form.html') as formf:
        form_text = formf.read()
    inputs=create_inputs(the_inputs)
    for hide_key in the_inputs_hide.keys():
        inputs = inputs+'<input type="hidden" name="'+\
        hide_key+'" value="'+the_inputs_hide[hide_key]+'">'
    form=Template(form_text)
    
    return(form.substitute(cgi_name=name, http_method=method, list_of_inputs=inputs, submit_text=text))