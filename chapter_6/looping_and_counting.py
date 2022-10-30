'''
The following program counts the number of times the letter "a" 
appears in a string.

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

EXERCISE: Encapsulte this code in a function named count, and
generalize it so that it accepts the string and the letter as arguments
'''


def count(string, letter):
    counter = 0
    for char in string:
        if char == letter:
            counter += 1

    return counter


print(count('banana', 'a'))
print(count('this is very fun', 'i'))
