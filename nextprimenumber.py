import math

print('Prime Number Finder: This Program will find a prime number until the user chooses to stop asking for the next one.')
choice = input('First number? (Type Y or N)\n')
current = 1


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False

    max_div = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_div, 2):
        if n % i == 0:
            return False
    return True


while choice.lower().startswith('y'):
    current += 1

    while is_prime(current) == False:
        current += 1

    print("Next prime is " + str(current))
    choice = input("Continue finding prime numbers (y/n)? ")
