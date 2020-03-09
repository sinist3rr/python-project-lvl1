from random import randint


RULE = 'Answer "yes" if number even otherwise answer "no".'


def is_even(number):
    if (number % 2 == 0):
        return True
    elif (number % 2 == 1):
        return False


def check():
    number = randint(1, 99)
    return str(number), 'yes' if is_even(number) else 'no'
