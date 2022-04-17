#!/usr/bin/env python3
from random import randint, choice
RULE = 'What number is missing in the progression?'
LENGTH_OF_PROGRESSION = 10


def generate_question_and_answer():
    num = randint(0, 10)
    step = randint(1, 10)
    progression = []
    for i in range(LENGTH_OF_PROGRESSION):
        next_step = num + step * i
        progression.append(str(next_step))
    secret_index = choice(range(len(progression) - 1))
    correct_answer = progression[secret_index]
    progression[secret_index] = '..'
    question = " ".join(progression)
    return question, correct_answer
