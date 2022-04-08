#!/usr/bin/env python3
from random import randint, choice


def progression():
    rule_of_the_game = 'What number is missing in the progression?'
    num = randint(0, 10)
    step = randint(1, 10)
    progression_list = []
    for i in range(10):
        next_step = num + step * i
        progression_list.append(next_step)

    secret_num = choice(progression_list)
    true_answer = str(secret_num)
    expression = ''
    for numb in progression_list:
        if numb == secret_num:
            expression = expression + ' ' + '..'
        else:
            expression = expression + ' ' + str(numb)
    return (expression, true_answer, rule_of_the_game)
