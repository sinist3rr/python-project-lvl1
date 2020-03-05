import prompt
from brain_games.cli import welcome_user


def greet():
    print('Welcome to the Brain Games!')


def show_question(random):
    print("Question: {}".format(random))
    return


def game_finish(user_name):
    print("Congratulations, {}!".format(user_name))
    return


def run(game_module):
    greet()
    print(game_module.RULE)
    user_name = welcome_user()
    game_round = 1
    while (game_round <= 3):
        random_entity, correct_answer = game_module.check()
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
