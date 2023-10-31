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