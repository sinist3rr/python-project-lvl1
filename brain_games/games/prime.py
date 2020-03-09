from brain_games.answer_checker import run


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    i = number - 1
    while (i > 1):
        if (number % i == 0):
            return False
        i -= 1
    return True


def check():
    return run(is_prime)
