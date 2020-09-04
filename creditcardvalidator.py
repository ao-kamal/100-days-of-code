

print('Credit Card Validator')
print('-----------------------\n')


def validate():
    number = input('Enter Credit Card Number\n')
    if all([number.isdecimal, len(number) == 16]) == True:
        for i in range(16):
    else:
        print('Invalid!\n')
        validate()
