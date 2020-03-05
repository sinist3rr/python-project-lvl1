from random import randint


def run(game):
    random_number = randint(1, 100)
    if game(random_number):
        return (str(random_number), 'yes')
    elif not game(random_number):
        return (str(random_number), 'no')
