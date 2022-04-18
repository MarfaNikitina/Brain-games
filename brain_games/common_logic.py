#!/usr/bin/env python3
import prompt
MAX_COUNT_OF_TRY = 3


def start(game):
    rule_of_the_game = game.RULE
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    if name:
        print('Hello, {}!'.format(name))
    print(rule_of_the_game)
    for _ in range(MAX_COUNT_OF_TRY):
        (expression, true_answer) = (game.generate_question_and_answer())
        print(f'Question: {expression}')
        answer = prompt.string('Your answer: ')
        if answer == true_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was '{true_answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
