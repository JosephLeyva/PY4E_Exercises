'''
EXERCISE 1: Rewrite your pay computation to give the employee 1.5 times the hourly 
rate for hours worked abovee 40 hours
'''

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
