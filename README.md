# World_of_Games
Wolrd of Games is a python project that enables you run a program containing 3 Games:
- Guess Game
- Memory Game
- Currency Roulette Games

The games total score at the end of the main run, calculates the score and presents it within a flask web site.

Read this README carfeuly to understand how to run the program and what are the games rules.

## Prerequisites

The following python modules should be installed in order to run the program:
 - requests
 - json
 - os
 - currency_converter

## The Games:

### Guess Game

Guess Game is a game where the user enters a difficulty (number).
Then, he will be asked to guess a number from 1 to the number he provided.
The user wins if he guessed the correct number.

### Memory Game

Memory Game is a game where the user enters a difficulty (number).
Then, random amount of numbers will be presented to the screen for 5 seconds and disappear.
The amount of numbers to be presented is according to the difficulty the user provided.
Then, the user will be asked to write down each number according to the order they were presented.
The user wins if he managed to remember all the numbers.

### Curreny Roulette Game

Currency Roulette Game is a game wherr the user enters a difficulty (number).
Then a random amount in USD will be presented to the user.
The user will be asked to guess the amoun ofthe number in ILS.
Difficulty represents the distance between the guess to the actual currency conversion.
The user wins if he managed to guess the right amount within the difficulty range.

## How to Play?

Simple! Just run MainGame.py. 

## How to review the scores?

Run MainScores.py (from the scoring library). Once the program runs, open a browser and browse to http://localhost:50000
