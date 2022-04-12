#!/usr/bin/env python3
from random import randint, choice


RULE_OF_THE_GAME = 'What number is missing in the progression?'


def make_progression():
    num = randint(0, 10)
    step = randint(1, 10)
    progression_list = []
    for i in range(10):
        next_step = num + step * i
        progression_list.append(next_step)
    return progression_list


def game():
    random_expression = make_progression()
    secret_num = choice(random_expression)
    true_result = str(secret_num)
    question = ''
    for numb in random_expression:
        if numb == secret_num:
            question = question + '..' + ' '
        else:
            question = question + str(numb) + ' '
    return question, true_result
