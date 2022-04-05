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
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    third_number = randint(1, 100)
    random_numbers = (first_number, second_number, third_number)
    for i in random_numbers:
        print('Question: {}'.format(i))
        answer = prompt.string('Your answer: ')
        if (is_even(i) and answer == 'yes') \
                or (not is_even(i) and answer == 'no'):
            print('Correct!')
        elif is_even(i) and answer != 'yes':
            print(
                "'{}' is wrong answer ;(. "
                "Correct answer was 'yes'.".format(answer)
            )
            print("Let's try again, {}!".format(name))
            break
        elif not is_even(i) and answer != 'no':
            print(
                "'{}' is wrong answer ;(. "
                "Correct answer was 'no'.".format(answer)
            )
            print("Let's try again, {}!".format(name))
            break
        print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
