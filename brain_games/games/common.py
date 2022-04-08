#!/usr/bin/env python3
import prompt


def greet():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    if name:
        print('Hello, {}!'.format(name))
    return name


def congrats(name):
    print('Congratulations, {}!'.format(name))



def make_progression():
    num = randint(0, 10)
    step = randint(0, 10)
    count_of_steps = 10
    progr_list = []
    for i in range(count_of_steps):
        next_step = num + step
        progr_list.append(next_step)
    secret_num = choice(progr_list)
    for numb in progr_list:
        if numb == secret_num:
            print('..')
        else:
            print(numb)


    list_ = []
    for i in range(10):
        list_.append(next_num)
    secret_num = choice(list_)
    for index, item in enumerate(list_):
        if item == secret_num:
            list_[index] = '..'
    print(list_)
    for i in list_:
        rand_progression = '{} {} {} {} {} {} {} {} {} {}'.format(list_(i))
    return rand_progression
#an+1= an + d
#an = a1 + (n-1) * d

