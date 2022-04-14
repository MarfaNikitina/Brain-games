#!/usr/bin/env python3
import prompt
MAX_COUNT_OF_TRY = 3


def start_the_game(module):
    expression = module.question
    true_answer = module.correct_answer
    rule_of_the_game = module.RULE_OF_THE_GAME
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    if name:
        print('Hello, {}!'.format(name))
    print(rule_of_the_game)
    i = 0
    while i < MAX_COUNT_OF_TRY:
        print(f'Question: {expression}')
        answer = prompt.string('Your answer: ')
        if answer == true_answer:
            i += 1
            print('Correct!')
            if i == 3:
                print(f'Congratulations, {name}!')
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was '{true_answer}'.")
            print(f"Let's try again, {name}!")
            break
