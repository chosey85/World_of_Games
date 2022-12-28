import random
import os
import time
import GeneralFunctions


def generate_sequence(difficulty):
    rand_list = []
    for i in range(difficulty):
        rand_list.append(random.randint(1, 101))
    return rand_list


def get_list_from_user(difficulty):
    user_list = []
    game_range = range(1, 101)
    for i in range(difficulty):
        provided_number = input(f'Please provide number {i+1}: ')
        while int(provided_number) not in game_range or not provided_number.isnumeric():
            print(f'{provided_number} is not a number / not in the range between 1 to 101 please try again.')
            provided_number = input(f'Please provide number {i+1}: ')
        user_list.append(int(provided_number))
    return user_list


def is_list_equal(list1, list2):
    if list1 == list2:
        return True
    else:
        return False


def play():
    selected_difficulty = GeneralFunctions.get_difficulty()
    generated_sequence = generate_sequence(selected_difficulty)
    print('\nTry to memorize the following sequence: ')
    print(generated_sequence)
    time.sleep(0.7)
    GeneralFunctions.clear_screen()
    print('\nPlease write now all the numbers you\'ve seen according to their order')
    user_list = get_list_from_user(selected_difficulty)
    result = is_list_equal(generated_sequence, user_list)
    if result:
        print(f'\nYou Won :) The generated sequence was indeed {generated_sequence}')
    else:
        print(f'\nYou Lost :( The generated sequence was {generated_sequence}, while yours was {user_list}')


