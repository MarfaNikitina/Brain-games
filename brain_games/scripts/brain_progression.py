#!/usr/bin/env python3
import prompt
from random import randint, choice


def make_progression():
    num = randint(0, 10)
    step = randint(1, 10)
    progr_list = []
    for i in range(10):
        next_step = num + step * i
        progr_list.append(next_step)
    return progr_list

def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    if name:
        print('Hello, {}!'.format(name))
    print('What number is missing in the progression?')
    i = 0
    while i < 3:
        ran_progr = make_progression()
        secret_num = choice(ran_progr)
        new_progr = ''
        for numb in ran_progr:
            if numb == secret_num:
                new_progr = new_progr + ' ' + '..'
            else:
                new_progr = new_progr + ' ' + str(numb)
        print(f'Question:{new_progr}')
        answer = prompt.string('Your answer: ')
        if answer == str(secret_num):
            i += 1
            print('Correct!')
            if i == 3:
                print('Congratulations, {}!'.format(name))
        else:
            print(
                "'{}' is wrong answer ;(. "
                "Correct answer was '{}'.".format(answer, secret_num)
            )
            print("Let's try again, {}!".format(name))
            break


if __name__ == '__main__':
    main()
