#!/usr/bin/env python3
from random import randint


def gcd_check():
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    complete_string = (str(random_number1) + ' ' + str(random_number2))
    while (random_number1 % random_number2 > 0):
        remainder = random_number1 % random_number2
        random_number1 = random_number2
        random_number2 = remainder
    return (complete_string, str(random_number2))


def main():
    gcd_check()


if __name__ == '__main__':
    main()
