'''
EXERCISE 2: Rewrite your pay computation with time-and-a-half for over-time
and create a function called computepay which takes two parameters (hours and rate)
'''


def computepay(hours, rate):
    if hours > 40:
        extra_hours = hours - 40
        pay = round(40 * rate, 2)
        # Compute extra hours (1.5 rate)
        pay += round(extra_hours * 1.5 * rate, 2)
    else:
        # Compute gross pay (rounded to 2 decimals)
        pay = round(hours * rate, 2)

    return pay


try:
    hours = int(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))

    pay = computepay(hours, rate)

    print(f'{pay=}')
except ValueError:
    print('Error, please enter numeric input')
