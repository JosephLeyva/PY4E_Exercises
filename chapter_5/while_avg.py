'''
EXERCISE 1: Write a program which repeatedly reads numbers until the user enters
"done". Once "done" is entered, print out the total, count, and average
of the numbers. If the user enters anything other than a number, detect their
mistake using try and except and print an error message and skip to the next number
'''

from decimal import Decimal


values = []

while True:

    line = input('Enter a number: ')
    if line == 'done':
        break

    try:
        values.append(Decimal(line))
    except:
        print('Invalid Input')

# Computing the total (sum of values) and count (len of values)
total = 0
count = 0
for value in values:
    total += value
    count += 1

# Calculating the average of of the numbers
avg = total / count
print(total, count, avg)
