'''
EXERCISE 3: Write a program to prompt for a score between 0.0 and 1.0. If the
score is out of range, print an error message, If the score is between 0.0 and 1.0, 
print a grade using the following table:

 Score     Grade
>= 0.9      A
>= 0.8      B
>= 0.7      C
>= 0.6      D
< 0.6       F

EXAMPLE
-------------------
Enter score: 0.95
A
'''
try:
    score = float(input('Enter score: '))
    result = None

    # Validation between range [0.0 , 1.0]
    if not 0 <= score <= 1.0:
        raise ValueError

    if score >= 0.9:
        result = 'A'
    elif score >= 0.8:
        result = 'B'
    elif score >= 0.7:
        result = 'C'
    elif score >= 0.6:
        result = 'D'
    else:
        result = 'F'

    print(f'{result=}')
except ValueError:
    print('Bad score')
