#!/usr/bin/env python3
import prompt
from brain_games.games.calc import create_random_expr
from brain_games.games.common import greet


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    if name:
        print('Hello, {}!'.format(name))
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        ran_expression = create_random_expr()
        print(f'Question: {ran_expression}')
        true_answer = str(eval(ran_expression))
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


if __name__ == '__main__':
    main()
