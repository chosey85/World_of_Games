import GuessGame
import MemoryGame
import CurrencyRouletteGame


def welcome(name):
    print(f""" Hello {name} and welcome to the World of Games (WoG)
 Here you can find many cool games to play\n """)


def load_game():
    play_another = 'yes'
    while play_another in ('yes', 'Yes'):
        chosen_game = input(""" Please choose a game to play:
        1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
        2. Guess Game - guess a number and see if you chose like the computer
        3. Currency Roulette - try and guess the value of a random amount of USD in ILS
        >>""")
        while not chosen_game.isdigit() or (int(chosen_game) > 3 or int(chosen_game) == 0):
            chosen_game = input(""" Please select a valid option:
        1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
        2. Guess Game - guess a number and see if you chose like the computer
        3. Currency Roulette - try and guess the value of a random amount of USD in ILS
        >>""")
        int_chosen_game = int(chosen_game)
        if int_chosen_game == 1:
            MemoryGame.play()
        elif int_chosen_game == 2:
            GuessGame.play()
        elif int_chosen_game == 3:
            CurrencyRouletteGame.play()
        play_another = input('Would you like to play another game? [Yes/No]: ')
        while play_another not in ('Yes', 'yes', 'No', 'no'):
            print('Invalid option')
            play_another = input('Would you like to play another game? [Yes/No]: ')
        if play_another in ('No', 'no'):
            print('Thank you for playing with us!')






