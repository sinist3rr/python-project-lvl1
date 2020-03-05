from random import randint


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".\n'


def is_prime(number):
    i = number - 1
    while (i > 1):
        if (number % i == 0):
            return False
        i -= 1
    return True


def check():
    random_number = randint(1, 100)
    if is_prime(random_number):
        return (str(random_number), 'yes')
    elif not is_prime(random_number):
        return (str(random_number), 'no')
