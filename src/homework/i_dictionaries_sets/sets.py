def get_p_distance(list1, list2):
    if len(list1) != len(list2):
        print("length of strings aren't equal")
    else:
        distance = 0
        for i in range (0, len(list1)):
            if list1[i] !=list2[i]:
                distance += 1
        return distance
    
def get_p_distance_matrix(list1):
    matrix = []
    i = 0
    j = 0
    for i in range(0, (len(list1))):
        l1 = []
        for j in range (0,len(list1)):
            distance = get_p_distance(list1[i],list1[j])
            fasta = distance / 10
            l1.append(fasta)
        i += 1
        matrix.append(l1)
    return matrix

def menu():
    choice = input("Select Option \n 1. Get P Distance Matrix:\n 2. Exit: ")
    option(choice)

def option(choice):
    while choice != '2':
        if choice == '1' :
            option1()
        if choice != '2' and choice != '1':
            choice = input("please select 1. or 2.: ")

    print("Program will Exit")
    

def option1():
    list_amt = int(input("how many str would you like to compare\n"))
    list1 = []
    i = 0
    for i in range (0, list_amt):
        inp_list = input("enter dna str: ")
        list1.append(inp_list)
    i += 1


    matrix = get_p_distance_matrix(list1)
    print(matrix)
    cont()

def cont():
    answer = input("Would you like to get another matrix? \n Type 'Y' for Yes\n Type 'N' to Exit: ")
    if answer.upper() != "N":
        while answer.upper() != "N" or answer.upper() != "Y":
            option1()
            while answer.upper() != "N" and answer.upper() != "Y":
                answer = input("Please select 'Y' or 'N': ")
    else:
        print("Program will exit")
        exit()

