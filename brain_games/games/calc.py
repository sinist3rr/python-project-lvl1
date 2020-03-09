from random import randint
from random import choice
from operator import add, sub, mul


RULE = 'What is the result of the expression?'


def check():
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    signs_and_ops = ((add(random_number1, random_number2), '+'),
                     (sub(random_number1, random_number2), '-'),
                     (mul(random_number1, random_number2), '*'))
    result, random_sign = choice(signs_and_ops)
    complete_string = ('{} {} {}'.format(str(random_number1),
                       random_sign, str(random_number2)))
    return (complete_string, str(result))
