#!/usr/bin/env python3
import prompt
"""Импортируем функцию и извлекаем из нее 3 переменные через распаковку кортежа"""


def common_logic_of_games(expression, true_answer, rule_of_the_game):
    """print greeting"""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    if name:
        print('Hello, {}!'.format(name))
    print(rule_of_the_game)
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
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{true_answer}'.")
            print(f"Let's try again, {name}!")
            break
