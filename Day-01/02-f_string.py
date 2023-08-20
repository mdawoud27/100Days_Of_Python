#!/usr/bin/python3

name = 'dawoud'
age = 21

print(f'My name is {name}, and I am {age}')

print(f'{17.22932:0.2f}')
print(f'{27:03d}')
print(f'{65:c}\t{97:c}')

# grouping digits
print(f'{123456.78436:,.2f}')

text = '''my name is mohamed
and am a software engineer
i am live in cairo'''
# splitted_text = text.split(',')
split_line = text.splitlines()
print(split_line)

text_list = ['chess', 'computer', 'reading', 'handball']
print(', '.join(text_list))

print('367'.isdigit())
print('ada312'.isalnum())
print('12 ds 32'.isalnum())
