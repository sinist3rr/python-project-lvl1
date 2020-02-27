#!/usr/bin/env python3
from random import randint


def progression_check():
    random_step = randint(1, 10)
    random_start = randint(1, 10)
    random_hide = randint(1, 10)
    i = 1
    current = random_start
    complete_string = ''
    while (i <= 10):
        if i == random_hide:
            complete_string += '..' + ' '
            hided_number = current
        else:
            complete_string += str(current) + ' '
        i += 1
        current += random_step
    return (complete_string[:-1], str(hided_number))


def main():
    progression_check()


if __name__ == '__main__':
    main()
