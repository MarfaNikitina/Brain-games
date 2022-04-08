#!/usr/bin/env python3
import prompt
from random import randint

def is_prime(num):
    devider = 2
    while num % devider != 0:
        devider += 1
    return devider == num

def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    if name:
        print('Hello, {}!'.format(name))
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i < 3:
        random_number = randint(1, 100)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        if is_prime(random_number):
            true_answer = 'yes'
        else:
            true_answer = 'no'
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
