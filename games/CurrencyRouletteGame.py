import requests
import json
import random
from currency_converter import CurrencyConverter
from etc import Utils
from scoring import Score


def generate_number():
    random_number = random.randint(1, 100)
    return random_number


def get_usd_to_ils_curr(total_amount):
    converter = CurrencyConverter()
    ils_amount = converter.convert(total_amount, 'USD', 'ILS')
    return ils_amount


# another option to do the currency conversion using API
#
# def get_usd_to_ils_curr(total_amount):
#     response = requests.get(
#         f'https://api.apilayer.com/exchangerates_data/convert?', params={
#             'to': 'ILS',
#             'from': 'USD',
#             'amount': total_amount
#         },
#         headers={
#             'apikey': 'bXAdeMFnc1fT0TNADmnnvkgYOmuudxtN'
#         }
#     )
#
#     data = json.loads(response.text)
#     return data["result"]


def get_guess_from_user(usd):
    guess = input(f'Please provide your guess of the current currency of {usd} USD in ILS ')
    while not guess.isnumeric():
        guess = input(f'Please enter a numeric value: ')
    return guess


def compare_guess_to_act(guessed_usd, act_usd, difficulty):
    if act_usd + difficulty >= guessed_usd >= act_usd - difficulty:
        return True
    else:
        return False


def play():
    difficulty = Utils.get_difficulty()
    amount_in_usd = generate_number()
    amount_in_ils = get_usd_to_ils_curr(amount_in_usd)
    guessed_amount = get_guess_from_user(amount_in_usd)
    print(f'actual amount is: {amount_in_ils} ILS')
    print(f'guessed amount it: {guessed_amount}')
    result = compare_guess_to_act(int(guessed_amount), int(amount_in_ils), int(difficulty))
    if result:
        print('You won')
        Score.add_score(difficulty)
    else:
        print('You lost')




