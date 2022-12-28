import GuessGame
import MemoryGame
import CurrencyRouletteGame

def welcome(name):
    print(f""" Hello {name} and welcome to the World of Games (WoG)
 Here you can find many cool games to play\n """)


def load_game():
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
    return int(chosen_game)


user_chosen_game = load_game()
if user_chosen_game == 1:
    MemoryGame.play()
elif user_chosen_game == 2:
    GuessGame.play()
else:
    CurrencyRouletteGame.play()

