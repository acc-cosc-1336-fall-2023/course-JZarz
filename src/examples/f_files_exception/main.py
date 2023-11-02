#main program
import files
#files.write_to_file('philsophers.txt')

#ls to check files created
#vi file prints/reads txt

#files.read_from_file('philsophers.txt')

#files.read_each_line_from_file('philsophers.txt')

#files.write_names_to_file('names.txt', 'a')
#files.read_from_file_while('names.txt')
#files.read_from_file_for('names.txt')
#files.write_sales_data('sales.txt','a')
#files.read_sales_data('sales.txt')
line = 'name,dept_id,other'

fields = line.split(',')

print(fields)

#files.write_field_data('field_data.txt','a')
files.read_field_data('field_data.txt')