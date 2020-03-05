from random import randint


RULE = 'Answer "yes" if number even otherwise answer "no".\n'


def is_even(number):
    if (number % 2 == 0):
        return True
    elif (number % 2 == 1):
        return False


def check():
    random_number = randint(1, 100)
    if is_even(random_number):
        return (str(random_number), 'yes')
    elif not is_even(random_number):
        return (str(random_number), 'no')
