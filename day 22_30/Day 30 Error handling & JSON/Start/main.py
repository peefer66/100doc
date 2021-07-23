# Error catching
try:
    file = open('my_text_file.txt')
    a_dict = {'key':'value'}
    print(a_dict['key'])

except FileNotFoundError:
    file = open('my_text_file.txt','w')
    file.write('Somthing')
except KeyError as error_message:
    print(f'The key {error_message} does not exist')
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print('File was closed')

#### Raise your own exception
height = float(input('Enter height(m): '))
weight = int(input('Enter weight(kg): '))

if height > 3:
    raise ValueError('Human height should not be above 3m')

bmi = weight/height**2
print(bmi)