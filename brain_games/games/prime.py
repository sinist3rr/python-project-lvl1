#!/usr/bin/env python3
from random import randint


def prime_check():
    random_number = randint(1, 100)
    i = random_number - 1
    while (i > 1):
        if (random_number % i == 0):
            return (str(random_number), 'no')
        i -= 1
    return (str(random_number), 'yes')


def main():
    prime_check()


if __name__ == '__main__':
    main()
