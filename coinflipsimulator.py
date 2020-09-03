"""Coin Flip Simulation - Write some code that simulates flipping a single coin however many times the user decides. The code should record the outcomes and count the number of tails and heads.
"""

import random
import sys

print('Coin Flip Simulator')
print('-----------------------')


def flip_again():
    prompt = input('Flip again? Y/N:\n')
    if prompt == 'Y':
        num_of_flips()
    elif prompt == 'N':
        print('Bye!')
        sys.exit()
    else:
        print('You typed {0}'.format(prompt))
        flip_again()


def coin_flip(n):
    heads = 0
    tails = 0
    for i in range(n):
        outcome = random.randint(0, 1)
        if outcome == 0:
            heads += 1
        if outcome == 1:
            tails += 1
    print('{0} flips of the coin returned {1} Heads and {2} Tails.'.format(
        n, heads, tails))
    print('\n')
    flip_again()


def num_of_flips():
    prompt = input('How many times do you want to flip the coin?:\n')
    if prompt.isdecimal() == True:
        n = int(prompt)
        coin_flip(n)
    else:
        print('You typed {0}'.format(prompt))
        num_of_flips()


num_of_flips()
