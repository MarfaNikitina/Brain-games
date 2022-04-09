#!/usr/bin/env python3
import prompt


def common_logic_of_games(function):
    (expression, true_answer, RULE_OF_THE_GAME) = function()
    """print greeting"""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    if name:
        print('Hello, {}!'.format(name))
    print(RULE_OF_THE_GAME)
    i = 0
    while i < 3:
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
