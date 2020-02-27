#!/usr/bin/env python3
from random import randint
from random import choice


def calc_check():
    string = '+-*'
    random_sign = choice(string)
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    complete_string = (str(random_number1) + ' ' + random_sign
                       + ' ' + str(random_number2))
    result = eval(complete_string)
    return (complete_string, str(result))


def main():
    calc_check()


if __name__ == '__main__':
    main()
