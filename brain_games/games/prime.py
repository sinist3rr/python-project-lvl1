from random import randint


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    i = number - 1
    while (i > 1):
        if (number % i == 0):
            return False
        i -= 1
    return True


def check():
    number = randint(1, 100)
    return str(number), 'yes' if is_prime(number) else 'no'
