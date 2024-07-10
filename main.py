import pandas as pd
import numpy as np

import random



num_max = 100

CSV_FILE = ('game_data.csv')

def get_data():
    return pd.read_csv(CSV_FILE)

def write_data(df):
    pd.DataFrame.to_csv(df)
df = get_data()

games_played = df.game_number.unique()
last_game = games_played[-1]
current_game = last_game + 1
print(current_game)


def guess(x):
    random_number = random.randint(1,x)
    guess = 0

    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            df.loc[len(df.index)] = [current_game, guess, False, False, True]
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            df.loc[len(df.index)] = [current_game, guess, False, True, False]
            print('Sorry, guess again. Too high.')

    df.loc[len(df.index)] = [current_game, guess, True, False, False]
    print(f'Congratulations! You have guessed the number {random_number} correctly!')
    df.to_csv ('game_data.csv')
    
guess(num_max)

