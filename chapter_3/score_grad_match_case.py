'''
EXERCISE 3: (MATCH-CASE VERSION) Write a program to prompt for a score between 0.0 and 1.0. 
If the score is out of range, print an error message, If the score is between 0.0 and 1.0, 
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

    match score:
        case n if n >= 0.9:
            result = 'A'
        case n if n >= 0.8:
            result = 'B'
        case n if n >= 0.7:
            result = 'C'
        case n if n >= 0.6:
            result = 'D'
        case n if n < 0.6:
            result = 'F'
        case _:
            raise ValueError

    print(f'{result=}')

except ValueError:
    print('Bad score')
