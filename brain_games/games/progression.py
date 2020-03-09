from random import randint


RULE = 'What number is missing in the progression?'


def progression_find(step, start, hide):
    i = 1
    current = start
    complete_string = ''
    while (i <= 10):
        if i == hide:
            complete_string += '..' + ' '
            hided_number = current
        else:
            complete_string += str(current) + ' '
        i += 1
        current += step
    return (complete_string[:-1], str(hided_number))


def check():
    random_step = randint(1, 10)
    random_start = randint(1, 10)
    random_hide = randint(1, 10)
    result = progression_find(random_step, random_start, random_hide)
    return result
