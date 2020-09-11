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
        pass
    elif prompt == 'Seconds':
        pass
    elif prompt == 'Minutes':
        pass
    elif prompt == 'Hours':
        pass
    elif prompt == 'Days':
        pass
    elif prompt == 'Weeks':
        pass
    else:
        print('You typed {0}'.format(prompt))
        time_from()


def call_time():
    time_from()


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


# 5 units:
# - Length(Inches, Feet, Millimetres, Centimetres, Metres, Kilometers)
# - Temperature(Fahrenheit, Celsius, Kelvin)
# - Time(Milliseconds, Seconds, Minutes, Hours, Days, Weeks)
# - Weight and Mass(Pounds, Kilograms, Ounces, Metric tonnes, grams)
# - Volume(Milliliters, Litres, Gallons(US), Cups(US), Pints(US))
