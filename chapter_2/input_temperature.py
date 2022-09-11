'''
EXCERCISE 5: Write a program which prompts the user for a Celsius temperature, convert
the temperature to Fahrenheit, and print put the converted temperature
'''

try:
    celsius = int(input('Please give me the temperature in °C: '))

    # conversion celsius to fahrenheit  => https://www.cuemath.com/c-to-f-formula/
    fahrenheit = celsius * 9 / 5 + 32
    print(f'{celsius} °C is equal to {fahrenheit} °F')
except:
    print('Something went wrong... Try again.')
