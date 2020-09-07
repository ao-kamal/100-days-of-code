'''Credit Card Validator - Takes in a credit card number from a common credit card vendor (Visa, MasterCard, American Express, Discover) and
validates it to make sure that it is a valid number (look into how credit cards use a checksum).
'''

print('Enter CC number')
cc = input()
if all([cc.isdecimal, len(cc) == 16]) == True:
    checksum = str(cc[-1:])
    rest = cc[:-1]
    print('Validating...')
    numbers = []
    for i in rest:
        numbers.append(int(i))
    to_double = [0, 2, 4, 6, 8, 10, 12, 14]
    for x in to_double:
        numbers[x] *= 2

    i = 0
    while i <= 14:
        if numbers[i] >= 10:
            sum(map(int, str(numbers[i])))
            numbers[i] = int(numbers[i])
            numbers[i] = sum(map(int, str(numbers[i])))
        i += 1
    sum_of = (sum(numbers))
    sum_of = int(sum_of) * 9
    check_digit = str(sum_of)[-1:]
    if checksum == check_digit:
        print("It's valid!")
    else:
        print("It's not valid.")
else:
    print("Invalid!")
