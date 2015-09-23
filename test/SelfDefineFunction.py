#Define Function
def my_function():
    print('//================Do self-function')
    print('Hi, my_function')


#Define Function-recursive
def print_list(input_list):
    for each_element in input_list:
        if isinstance(each_element, list):
            print_list(each_element)
        else:
            print(each_element)
