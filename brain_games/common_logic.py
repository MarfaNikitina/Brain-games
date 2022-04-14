#!/usr/bin/env python3
import prompt
MAX_COUNT_OF_TRY = 3


def start_the_game(module):
    expression, true_answer = module.generate_question_and_answer()
    rule_of_the_game = module.RULE_OF_THE_GAME
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    if name:
        print('Hello, {}!'.format(name))
    print(rule_of_the_game)
    for i in range(MAX_COUNT_OF_TRY):
        print(f'Question: {expression}')
        answer = prompt.string('Your answer: ')
        if answer == true_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was '{true_answer}'.")
            print(f"Let's try again, {name}!")
            break
        print(f'Congratulations, {name}!')
