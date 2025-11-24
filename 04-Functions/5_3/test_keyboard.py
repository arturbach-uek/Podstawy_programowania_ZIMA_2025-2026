from keyboard import input_string, input_integer, input_real, input_boolean # type: ignore

first_name = input_string('Enter name: ')
last_name = input_string('Enter last name: ')
age = input_integer('Enter age: ')
salary = input_real('Enter salary: ')
is_salary_hidden = input_boolean('Hide salary? (y/n): ')

print('\nDATA RECORD')
print('===========')
print('Name:', first_name, last_name)
print('Age:', age)

if not is_salary_hidden:
    print('Salary:', salary)
else:
    print('Salary: [HIDDEN]')
