#!/usr/bin/env python3

import prompt
from random import randint
from brain_games.cli import welcome_user


def greet():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".\n')


def even_check(num):
    if (num % 2 == 0):
        return 'yes'
    elif (num % 2 == 1):
        return 'no'


def even(user_name):
    i = 1
    while (i <= 3):
        random_number = randint(1, 100)
        print("Question: {}".format(random_number))
        user_answer = prompt.string('Your answer: ')

        if ((random_number % 2 == 0 and user_answer == 'yes') or
                (random_number % 2 == 1 and user_answer == 'no')):
            print('Correct!')
            i += 1
        elif ((random_number % 2 == 0 and user_answer != 'yes') or
                (random_number % 2 == 1 and user_answer != 'no')):
            print("'{}' is wrong answer ;(. Correct answer was '{}'."
                  .format(user_answer, even_check(random_number)))
            return
    print("Congratulations, {}!".format(user_name))


def main():
    greet()
    name = welcome_user()
    even(name)


if __name__ == '__main__':
    main()
