'''
EXERCISE 1: Write a for loop that starts at the last character in the string 
and works its way backwards to the first character in the string,
printing each letter on a separate line, except backwards
'''
while True:
    try:
        word = input('Give a string: ')
        word = word.strip()
        if word != '':
            break
        else:
            raise ValueError
    except ValueError:
        print('You need to write something...')


for letter in word[::-1]:
    print(letter)
