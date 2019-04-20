
hello_string = 'Hello, I am a Python String'

for i in range(len(hello_string)):
    print(hello_string[i])

try:
    hello_string[3] = 'f'
except TypeError:
    print('There was an Error')

new_string = hello_string[0:3] + 'f' + hello_string[4:]

print(new_string, '|', hello_string[0:3], '|', hello_string[4:])

# splits into a list of characters
shorter_string = 'split me up'
print(list(shorter_string))

if ' I am a string' == 'I am a string ':
    print('they are the same')

if ' I am a string'.strip() == 'I am a string '.strip():
    print('they are the same now')

print(hello_string.split())

csv_string = 'I am a string, 23, 13, This is what CSV files will give'
print(csv_string.split(','))

list_of_strings = ['this', 'that', 'them', 'those', 'things']

things_to_join = []
joining_string = '..'

joining_string.join(things_to_join)
print("|".join(list_of_strings))
print(" and ".join(list_of_strings))

