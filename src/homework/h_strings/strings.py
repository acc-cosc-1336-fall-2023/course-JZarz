def get_hamming_distance(dna1,dna2):

    distance = 0

    if len(dna1) != len(dna2):
        print("DNA strings aren't equal")
    else:
        for ch in range (0, len(dna1)):
            if dna1[ch] != dna2[ch]:
                distance += 1
        return distance

def get_dna_complement(dna):

    list = dna[::-1]
        #print(list)
        
    ch = 0 
    while ch < (len(list)):
        new_list = list.lower()
        complement = new_list.replace("a", "T").replace("t","A").replace("c","G").replace("g","C")
        ch += 1
        com = complement
                    
        return com
        

def menu_choice():
    choice = input(" 1. Find Hemming Distance \n 2. Find Dna Complement \n 3. Exit \n")
    main_menu(choice)

def main_menu(choice):

    if choice == '1':
        option_1() 
    elif choice == '2':
        option_2()
    elif choice == '3':
        option_3()
        
    else:
        print("invalid input")

def option_1():
    dna1 = input("type first dna str: \n")
    dna2 = input("type second dna str: \n")

    result =get_hamming_distance(dna1, dna2)

    print (f'The hemming distance of {dna1} and {dna2} is: \n {result}')
    cont_1()
        
def option_2():
    dna = input("type Dna string: \n")
    com = get_dna_complement(dna)
    print (f"Complement Dna {dna} is:\n {com}")
    cont_2()
    

def option_3():
    result = input("Are you sure you want to exit? \n Type 'Y' to exit \n Type 'N ' to return to menu: \n")
    while result.upper() != "Y":

        if result.upper() == "N":
            menu_choice()
            break
            
        else:
            while result.upper() != 'Y' and result.upper() != 'N':
                result = input("Please choose 'Y' or 'N': ")
    
    print("Exited")
    exit()

def cont_1():
    result = input("would you like to continue? \n Type 'Y' to repeat \n type 'N' to return to menu: ")
    while result.lower() != "y":
        if result.lower() == 'n':
            menu_choice()
            
        else:
            while result.lower() != 'y' and result.lower() != 'n':
                result = input("Please choose 'Y' or 'N': ")

    option_1()

def cont_2():
    result = input("would you like to continue? \n Type 'Y' to repeat \n type 'N' to return to menu: ")
    while result.lower() != "y":
        if result.lower() == 'n':
            menu_choice()
            
        else:
            while result.lower() != 'y' and result.lower() != 'n':
                result = input("Please choose 'Y' or 'N': ")

    option_2()
    
            