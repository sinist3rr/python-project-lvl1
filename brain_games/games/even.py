from brain_games.answer_checker import run


RULE = 'Answer "yes" if number even otherwise answer "no".'


def is_even(number):
    if (number % 2 == 0):
        return True
    elif (number % 2 == 1):
        return False


def check():
    return run(is_even)
