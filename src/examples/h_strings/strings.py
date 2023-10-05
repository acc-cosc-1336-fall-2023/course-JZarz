def test_config():
    return True

def loop_string_w_while(str):

    index = 0

    while index < len(str):
        print (str[index])
        index += 1

def loop_string_ww_for(str):
    
    for s in range (0, len(str)):
        #print(s)
        print (str[s])

def loop_string_w_special_for(str):
    for ch in str:
        print(ch)

def concat_strings(str1,str2):
    return str1 + str2

def slice_string(str):
    return str[6:10]

def slice_w_step_value(str):
    return str[0:len(str):2]

def search_str(str1, str2):
    return str1 in str2
#must be sequential

def use_repetition_operator(num):
    for n in range(1, num+1):
        print("*" * n)