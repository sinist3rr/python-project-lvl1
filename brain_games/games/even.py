#!/usr/bin/env python3
from random import randint


def even_check():
    random_number = randint(1, 100)
    if (random_number % 2 == 0):
        return (random_number, 'yes')
    elif (random_number % 2 == 1):
        return (random_number, 'no')


def main():
    even_check()


if __name__ == '__main__':
    main()
