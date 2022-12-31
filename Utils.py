import os


def get_difficulty():
    attempt = 0
    while attempt < 3:
        try:
            difficulty = input('Please select difficulty: ')
            return int(difficulty)
        except ValueError:
            print(f'''The difficulty value you provided is not legal
                                 Please make sure to follow these guidelines:
                                 1. Value must be a number
                                 2. Value must be greater than 1
                                 [Attempt no. {attempt + 1} out of 3]''')
            attempt += 1


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


scores_file_name = 'scores.txt'
bad_return_code = 666
