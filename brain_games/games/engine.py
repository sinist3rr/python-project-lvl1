#!/usr/bin/env python3
import prompt
from brain_games.games.even import even_check
from brain_games.games.calc import calc_check
from brain_games.games.gcd import gcd_check
from brain_games.games.progression import progression_check
from brain_games.cli import welcome_user


def greet():
    print('Welcome to the Brain Games!')


def game_banner(game):
    if game == 'even':
        print('Answer "yes" if number even otherwise answer "no".\n')
    elif game == 'calc':
        print('What is the result of the expression?\n')
    elif game == 'gcd':
        print('Find the greatest common divisor of given numbers.\n')
    elif game == 'progression':
        print('What number is missing in the progression?\n')


def show_question(random):
    print("Question: {}".format(random))
    return


def game_finish(user_name):
    print("Congratulations, {}!".format(user_name))
    return


def game_engine(game_name):
    greet()
    game_banner(game_name)
    user_name = welcome_user()
    game_round = 1
    while (game_round <= 3):
        if game_name == 'even':
            (random_entity, correct_answer) = even_check()
        elif game_name == 'calc':
            (random_entity, correct_answer) = calc_check()
        elif game_name == 'gcd':
            (random_entity, correct_answer) = gcd_check()
        elif game_name == 'progression':
            (random_entity, correct_answer) = progression_check()
        show_question(random_entity)
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            game_round += 1
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'."
                  .format(user_answer, correct_answer))
            return
    game_finish(user_name)


def main():
    game_engine()


if __name__ == '__main__':
    main()
