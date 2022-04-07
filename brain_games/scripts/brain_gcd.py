#!/usr/bin/env python3
import prompt
from random import randint
import math


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    if name:
        print('Hello, {}!'.format(name))
    print('Find the greatest common divisor of given numbers.')
    i = 0
    while i <= 2:
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        rand_expression = '{} {}'.format(num1, num2)
        print('Question: {}'.format(rand_expression))
        answer = prompt.string('Your answer: ')
        true_result = str(math.gcd(num1, num2))
        if answer == true_result:
            print('Correct!')
        else:
            print(
                "'{}' is wrong answer ;(. "
                "Correct answer was '{}'.".format(answer, true_result)
            )
            print("Let's try again, {}!".format(name))
            break
        i += 1
    print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
