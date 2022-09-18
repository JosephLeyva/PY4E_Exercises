'''
EXERCISE 7: Rewrite the grade program from the previous chapter using
a function called computegrade that takes a score as its parameter and
returns a grade as a string.

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


def computegrade(score):
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
    return result


try:
    score = float(input('Enter score: '))
    result = None

    # Validation between range [0.0 , 1.0]
    if not 0 <= score <= 1.0:
        raise ValueError

    result = computegrade(score)

    print(f'{result=}')

except ValueError:
    print('Bad score')
