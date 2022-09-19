'''
EXERCISE 2: Write another program that prompts for a list of numbers as
above and at the end prints out both the maximum and minimum of the numbers
instead of the average
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


# Compute the min and max
minimum = None
maximum = None
for value in values:
    if minimum is None or value < minimum:
        minimum = value
    if maximum is None or value > maximum:
        maximum = value

print('minimum = {}, maximum = {}'.format(str(minimum), str(maximum)))
