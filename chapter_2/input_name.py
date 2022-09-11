'''
EXCERCISE 2: Write a program that uses *input* to prompt a user
their name and welocomes them.
'''


name = input('What is your name? ')

if name.strip() == '':
    raise ValueError('You have to enter a name!')

print(f'Hello {name}!')
