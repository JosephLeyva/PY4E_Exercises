'''
EXERCISE 2: Rewrite your pay program using try and except so that your
program handles non-numeric input gracefully by printing a message and
exiting the program.
'''

try:
    hours = int(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))

    if hours > 40:
        extra_hours = hours - 40
        pay = round(40 * rate, 2)

        # Compute extra hours (1.5 rate)
        pay += round(extra_hours * 1.5 * rate, 2)
    else:
        # Compute gross pay (rounded to 2 decimals)
        pay = round(hours * rate, 2)

    print(f'{pay=}')
except ValueError:
    print('Error, please enter numeric input')
