def test_config():
    return True
def display_list():
    list1 = [5,10,20]
    print (list1)

def display_list_w_while_loop():
    list = [5,10,20]

    index = 0

    while index < len(list):
        print (list[index])
        index += 1

def display_rev_list_w_while_loops():
    list = [5,10,20]
    
    list_index = len(list)-1

    while list_index >= 0:
        print (list[list_index])
        list_index -= 1

def display_list_w_for_range():
    list = [5,10,20]
    for i in range(0, len(list)):
        print (list[i])

def display_list_w_for_range_w_skip():
    list = [5,10,20,3,7,1,50]
    for i in range(0, len(list),2):
        print (list[i])    

def display_rev_list_w_for_range():
    list = [5,10,20]
    for i in range(len(list), 0, -1):
        print (list[i-1])
        
def get_list_total_while(list):
    index = 0
    sum = 0

    while(index < len(list)):
        sum += list[index]
        index += 1
    return sum

def get_list_total_for(list):

    sum = 0 
    for i in range (0, len(list)):
        sum += list[i]

    return sum

def list_ref_param(list):
    list[0] = 0

def get_list_return_value(list):
    print(list)
    list[0] = 0

    return list
