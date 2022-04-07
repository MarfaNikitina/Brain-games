#!/usr/bin/env python3
import prompt
from random import randint, choice
import operator


def create_random_expr():
    numb1 = randint(1, 100)
    numb2 = randint(1, 100)
    ops = {'+': operator.add,
           '-': operator.sub,
           '*': operator.mul}
    random_ops = choice(list(ops.keys()))
    ran_expression = str(numb1) + random_ops + str(numb2)
    return ran_expression


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    if name:
        print('Hello, {}!'.format(name))
    print('What is the result of the expression?')
    ran_expr1 = create_random_expr()
    ran_expr2 = create_random_expr()
    ran_expr3 = create_random_expr()
    ran_examples = (ran_expr1, ran_expr2, ran_expr3)
    for i in ran_examples:
        print('Question: {}'.format(i))
        true_answer = str(eval(i))
        answer = prompt.string('Your answer: ')
        if answer == true_answer:
            print('Correct!')
        else:
            print(
                "'{}' is wrong answer ;(. "
                "Correct answer was '{}'.".format(answer, true_answer)
            )
            print("Let's try again, {}!".format(name))
            break
        print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
