"""Binary to Decimal and Back Converter - Develop a converter to convert a decimal number
to binary or a binary number to its decimal equivalent.
"""
import sys

print(
    'This program converts a number from Binary to Decimal or from Decimal to Binary.')


def binary_to_decimal(n):
    print(int(str(n), 2), '\n')


def decimal_to_binary(n):
    print(format(int(n), 'b'), '\n')


def convert_again():
    prompt = input('Run the program again? (Y/N)\n')
    if prompt == 'Y':
        converter()
    elif prompt == 'N':
        print('Bye!')
        sys.exit()
    else:
        print("You typed '{0}'.'.format{0}\n")
        convert_again()


def converter():
    print('-------------------------------------------\n')
    choice = input(
        "To convert from Binary to Decimal, type 'b'.\nTo convert from Decimal to Binary, type 'd'.\n")
    if choice == 'b':
        print('---------------------------------------')
        print('Converting from Binary to Decimal...\n')
        number = input('Enter the number you want to convert: \n')
        binary_to_decimal(number)
        convert_again()

    elif choice == 'd':
        print('---------------------------------------')
        print('Converting from Binary to Decimal...\n')
        number = input('Enter the number you want to convert: \n')
        decimal_to_binary(number)
        convert_again()

    else:
        print("You typed '{0}'.".format(choice))
        converter()
        print('\n')


converter()
