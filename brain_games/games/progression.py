#!/usr/bin/env python3
from random import randint, choice
RULE = 'What number is missing in the progression?'
LENGTH_OF_PROGRESSION = 10


def make_progression():
    num = randint(0, 10)
    step = randint(1, 10)
    progression_list = []
    for i in range(LENGTH_OF_PROGRESSION):
        next_step = num + step * i
        progression_list.append(next_step)
    return progression_list


def generate_question_and_answer():
    random_expression = make_progression()
    secret_num = choice(random_expression)
    correct_answer = str(secret_num)
    question = ''
    for numb in random_expression:
        if numb == secret_num:
            question = question + '..' + ' '
        else:
            question = question + str(numb) + ' '
    return question, correct_answer
