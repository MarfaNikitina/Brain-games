#!/usr/bin/env python3
from random import randint, choice
RULE = 'What number is missing in the progression?'
LENGTH_OF_PROGRESSION = 10


def generate_question_and_answer():
    num = randint(0, 10)
    step = randint(1, 10)
    progression = ''
    for i in range(LENGTH_OF_PROGRESSION):
        next_step = str(num + step * i)
        progression = progression + next_step
    secret_number = choice(progression)
    correct_answer = secret_number
    new_progression = ''
    for item in progression:
        if item == secret_number:
            new_progression = new_progression + '..'
        else:
            new_progression = new_progression + item
    question = " ".join(new_progression)
    return question, correct_answer
