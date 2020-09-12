"""Unit Converter (temp, currency, volume, mass and more) - Converts various units between one another.The user enters the type of unit being
entered, the type of unit they want to convert to and then the value. The program will then make the conversion.
"""
import math
import sys
import time

print('Unit Converter')
print('---------------------------')


def time_from():
    prompt = input(
        'Converting from?: (Milliseconds, Seconds, Minutes, Hours, Days, Weeks)\n')
    if prompt == 'Milliseconds':
        print('Converting from Milliseconds...\n')
        return 0
    elif prompt == 'Seconds':
        print('Converting from Seconds...\n')
        return 1
    elif prompt == 'Minutes':
        print('Converting from Minutes...\n')
        return 2
    elif prompt == 'Hours':
        print('Converting from Hours...\n')
        return 3
    elif prompt == 'Days':
        print('Converting from Days...\n')
        return 4
    elif prompt == 'Weeks':
        print('Converting from Weeks...\n')
        return 5
    else:
        print('You typed {0}'.format(prompt))
        time_from()


def time_to():
    prompt = input(
        'Converting to?: (Milliseconds, Seconds, Minutes, Hours, Days, Weeks)\n')
    if prompt == 'Milliseconds':
        print('Converting to Milliseconds...\n')
        return 0
    elif prompt == 'Seconds':
        print('Converting to Seconds...\n')
        return 1
    elif prompt == 'Minutes':
        print('Converting to Minutes...\n')
        return 2
    elif prompt == 'Hours':
        print('Converting to Hours...\n')
        return 3
    elif prompt == 'Days':
        print('Converting to Days...\n')
        return 4
    elif prompt == 'Weeks':
        print('Converting to Weeks...\n')
        return 5
    else:
        print('You typed {0}'.format(prompt))
        time_to()


def call_time():
    conv = [1, 10, 60, 60, 24, 7]
    i = time_from()
    j = time_to()


def convert_again():
    prompt = input('Convert again? Y/N:\n')
    if prompt == 'Y':
        unit_type()
    elif prompt == 'N':
        print('Bye!')
        sys.exit()
    else:
        print('You typed {0}'.format(prompt))
        convert_again()


def unit_type():
    prompt = input('Enter unit type do you want to convert. (Time):\n')
    if prompt == 'Time':
        call_time()
    else:
        print('You typed {0}'.format(prompt))
        unit_type()


unit_type()

# 5 units:
# - Length(Inches, Feet, Millimetres, Centimetres, Metres, Kilometers)
# - Temperature(Fahrenheit, Celsius, Kelvin)
# - Time(Milliseconds, Seconds, Minutes, Hours, Days, Weeks)
# - Weight and Mass(Pounds, Kilograms, Ounces, Metric tonnes, grams)
# - Volume(Milliliters, Litres, Gallons(US), Cups(US), Pints(US))
