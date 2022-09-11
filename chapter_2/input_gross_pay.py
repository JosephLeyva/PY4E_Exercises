'''
EXCERCISE 3: Write a program to prompt the user for hours and rate per hour
to compute gross pay
'''
try:
    hours = int(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))

    # Compute gross pay (rounded to 2 decimals)
    pay = round(hours * rate, 2)
    print(f'{pay=}')
except ValueError:
    print('There was an invalid input. Try Again...')
