def menu():
    
    option = input("Please select option \n 1. Factorial \n 2. sum of odds \n 3. exit: \n")

    handle_menu_options(option)
    
    

def handle_menu_options(option):
    if option.isnumeric():
        option = int(option) 
        while option != 3:
                if option == 1:
                    option_1()
                elif option == 2:
                    option_2()
                else:
                    print("Invalid option. Please select 1, 2, or 3.")
                    option = int(input("Please select 1, 2, or 3: "))
        
        # Exit the loop when the user selects 3
        cont()
    else:
        print("input must be numeric")
    
    

def option_1():
    num = int(input("please enter a number in range  1 - 100  for a factorial or 0 to exit: "))

    if ( num != 0):
    
        while (num <0 or num > 100):
           num = int(input("number must be in range of 1  - 100: "))
            
        solution = get_factorial(num)
        print('factorial of ' , num , 'is ' ,solution)
    else:
        cont()

def option_2():
    num = int(input("please enter a number in range  1 - 100 for sum of odds or 0 to exit: "))

    if ( num != 0):
    
        while (num <0 or num > 100):
            num = int(input("number must be in range of 1  - 100: "))

        sum = sum_odd_numbers(num)
        print("sum of odds for" , num, " is ", sum)
        
    else:
        cont()
    
    
def get_factorial(num):
    
    solution = 1

    for n in range(num):
        solution *= n + 1
    
    return solution

    

def sum_odd_numbers(num):
    sum = 0
    n = 0
    for n in range (num):

        while (n <= num and (n% 2 == 0)):
            
            sum += n + 1
            n += 1

    return sum

def cont():
    answer = input("Are you sure you want to exit? \n Type 'Y' to exit \n Type 'N' to go back to menu: ")
    
    if (answer.lower() != "y"):
        while((answer.lower() != "n" and answer.lower() != "y")):

            answer = input( "please select Y or N: ")

        menu()
        
    else:
        print('program will exit')
        exit()
    
    
def menu_op(option):        

    while True:
        if option == '1':
            option_1()  
            break   

        elif option == '2':
            option_2()
            break
        
        elif option == '3':
            cont()
            break

        else:
            print("please select 1, 2 or 3")
            break
    
def menu_ops_1(option):
    
    if option.isnumeric(): 
        option = int(option)
        while option != 3 or option != 2 or option != 1:
            if option != 3:               
                while option != 2 or option != 1 :
                    if option != 2:
                        while option != 1 :
                            option =  int(input("please select 1, 2 or 3: "))
                        option_1()
                    else:
                        option_2()    
            else:
                cont()
    else:
        print ("must be numeric ")
