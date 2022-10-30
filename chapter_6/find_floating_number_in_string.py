'''
EXERCISE 5: Take the following Python code that stores a string:

str_ = 'X-DSPAM-Confidence:0.8475'

Use find and string slicing to extract the portion of the string after
the colon character and then use the float function to convert the 
extracted string into a floating point number.
'''

str_ = 'X-DSPAM-Confidence:0.8475'

index = str_.find(':')
number = float(str_[index+1:])

print(number)
print(type(number))
