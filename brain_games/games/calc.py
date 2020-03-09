from random import randint
from random import choice


RULE = 'What is the result of the expression?'


def calculate(number1, sign, number2):
    if sign == '+':
        return number1 + number2
    elif sign == '-':
        return number1 - number2
    elif sign == '*':
        return number1 * number2


def check():
    string = '+-*'
    random_sign = choice(string)
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    complete_string = (str(random_number1) + ' ' + random_sign
                       + ' ' + str(random_number2))
    result = calculate(random_number1, random_sign, random_number2)
    return (complete_string, str(result))
