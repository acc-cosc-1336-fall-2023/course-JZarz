def write_to_file(file_name):
    out_file = open(file_name, 'w')
    #write to file
    out_file.write('John Locke\n')
    out_file.write('David Hume\n')
    out_file.write('Edmund Burke\n')

    #close the file
    out_file.close()
    
def read_from_file(file_name):
    in_file = open(file_name,'r')

    file_contents = in_file.read()

    #close file
    in_file.close()
    print(file_contents)

def read_each_line_from_file(file_name):
    in_file = open(file_name,'r')
    line1 = in_file.readline()
    line2 = in_file.readline()
    line3 = in_file.readline()

    in_file.close()

    print(line1)
    print(line2)
    print(line3)
    #if you dont want space you have to strip line space .rstrip('\n')
#cant use testcase because we dont want test to create new info
def write_names_to_file(file_name, file_mode):
    out_file = open(file_name,file_mode)

    user_choice = 'y'

    while(user_choice.lower() == 'y'):
        name = input('enter friend: ')
        out_file.write(name +'\n')
        user_choice = input('type y to continue...')

    out_file.close()

def read_from_file_while(file_name):
    in_file = open(file_name)

    line = in_file.readline()

    while (line != ''):
        print(line.rstrip('\n'))
        line = in_file.readline()

        in_file.close()

def read_from_file_for(file_name):
    in_file = open(file_name,'r')

    for line in in_file:
        print(line.rstrip('\n'))

    in_file.close()

def write_sales_data(file_name, file_mode):
    out_file = open(file_name,file_mode)

    user_choice = 'y'
    while(user_choice.upper() == 'Y'):
        amount = input('enter sale data: ')
        out_file.write(amount + '\n')
        user_choice = input('type y to continue..')

    out_file.close()

def read_sales_data(file_name):
    in_file = open(file_name,'r')

    total_sales = 0

    for amount in in_file:
        print(f'{float(amount):.2f}')
        total_sales +=float(amount)
    print('.........')
    print(f'{total_sales:.2f}')
    in_file.close()

def write_field_data(file_name,file_mode):
    out_file = open(file_name, file_mode)

    user_choice = 'y'
    while (user_choice.upper() == 'Y'):

        name = input("enter name: ")
        dept_id = input('enter dept id: ')
        lang = input('enter programming language: ')

        out_file.write(name + ',' + dept_id + ',' + lang + '\n')
        user_choice = input('enter y to continue..')

    out_file.close()

def read_field_data(file_name):
    in_file = open(file_name,'r')
    name = ''
    dept_id = ''
    lang = ''
    for line in in_file:
        fields = line.rstrip('\n').split(',')
        print(fields)
    in_file.close()

def read_field_data(file_name):
    in_file = open(file_name,'r')
    name = ''
    dept_id = ''
    lang = ''
    for line in in_file:
        fields = line.rstrip('\n').split(',')
        name = ''
        dept_id = ''
        print(fields)
    in_file.close()

def write_city_list_to_file(file_name):
    cities = ['new york', 'boston', 'atlanta', 'dallas']

    out_file = open(file_name,'w')
    for city in cities:
        out_file.write(city + '\n')

    out_file.close()

def read_city_list(file_name):
    in_file = open(file_name,'r')
    cities = []
    for line in in_file:
        cities.append(line.rstrip('\n'))
    
    print(cities)