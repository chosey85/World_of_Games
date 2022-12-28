import random
import GeneralFunctions


def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    return int(secret_number)


def get_guess_from_user(difficulty):
    attempt = 0
    while attempt < 3:
        try:
            options = range(1, difficulty)
            guess = input(f'Please select a number between 1 to {difficulty}: ')
            while int(guess) not in options:
                print(f'{guess} is not a valid number within 1 to {difficulty}, please try again')
                guess = input(f'Please select a number between 1 to {difficulty}: ')
            return int(guess)
        except ValueError:
            print(f'''The value you provided is not legal
                     Please make sure to follow these guidelines:
                     1. Value must be a number
                     [Attempt no. {attempt + 1} out of 3]''')
            attempt += 1


def compare_results(secret_number, guess):
    if secret_number == guess:
        return True
    else:
        return False


def play():
    selected_difficulty = GeneralFunctions.get_difficulty()
    generated_secret_number = generate_number(selected_difficulty)
    user_guess = get_guess_from_user(selected_difficulty)
    results = compare_results(generated_secret_number, user_guess)
    if results:
        print(f'\nYou Won :) The secret number is indeed {generated_secret_number}!')
    else:
        print(f'\nYou lost :( The secret number is {generated_secret_number}, while you selected {user_guess}.')







