def test_config():
    return True

def display_numbers(num):
    cnt = 0
    
    while cnt < num:
        print( "cnt " + str( cnt) +" cnt + 1 " + str( cnt + 1 ) + "num " + str(num))
        cnt = cnt + 1   
        print("cnt after adding 1 " + str(cnt))
        #statement that makes the boolean expression false

def sum_of_square(num): # (3) 1*1 + 2*2 + 3*3 = 14
    sum = 0

    while num > 0:
        sum = sum + num * num
        num = num - 1 #eventually makes boolean expression false

    return sum

def prompt_user():
    keep_going = 'y'

    while keep_going == 'y' or keep_going == 'Y':
        keep_going = input("Loop again, type y: ")

def for_intro_loop():
    for num in [1, 2, 3, 4, 5]:
        print (num)

def for_intro_loop_strings():
    for lang in [ "c++", "java", "python"]:
        print (lang)

def sum_of_squares(num):
    sum = 0

    for val in range(1, num +1):
        sum = sum + val *val

    return sum