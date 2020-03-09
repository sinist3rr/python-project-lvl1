from random import randint


RULE = 'Find the greatest common divisor of given numbers.'


def gcd_find(number1, number2):
    while (number1 % number2 > 0):
        remainder = number1 % number2
        number1 = number2
        number2 = remainder
    return number2


def check():
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    complete_string = (str(random_number1) + ' ' + str(random_number2))
    result = gcd_find(random_number1, random_number2)
    return (complete_string, str(result))
