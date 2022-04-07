#!/usr/bin/env python3
import prompt
from random import randint


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    if name:
        print('Hello, {}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i <= 2:
        random_number = randint(1, 100)
        print('Question: {}'.format(random_number))
        answer = prompt.string('Your answer: ')
        if (is_even(random_number) and answer == 'yes') \
                or (not is_even(random_number) and answer == 'no'):
            print('Correct!')
        elif is_even(random_number) and answer != 'yes':
            print(
                "'{}' is wrong answer ;(. "
                "Correct answer was 'yes'.".format(answer)
            )
            print("Let's try again, {}!".format(name))
            break
        elif not is_even(random_number) and answer != 'no':
            print(
                "'{}' is wrong answer ;(. "
                "Correct answer was 'no'.".format(answer)
            )
            print("Let's try again, {}!".format(name))
            break
        i += 1
        print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
