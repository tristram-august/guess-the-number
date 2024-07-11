import pandas as pd
import numpy as np
import random

num_max = 100

CSV_FILE = ('game_data.csv')

def get_data():
    return pd.read_csv(CSV_FILE)
            
df = get_data()

games_played = df.game_number.unique()
last_game = games_played[-1]
current_game = last_game + 1
print(f'Game #{current_game}.')

def guess(x):
    random_number = random.randint(1,x)
    guess = 0

    while guess != random_number:
        new_row = []
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            new_row = {'game_number':current_game, 'guess':guess, 'correct':False, 'too high':False, 'too low':True}
            df.loc[len(df)] = new_row
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            new_row = {'game_number':current_game, 'guess':guess, 'correct':False, 'too high':True, 'too low':False}
            df.loc[len(df)] = new_row
            print('Sorry, guess again. Too high.')

    new_row = {'game_number':current_game, 'guess':guess, 'correct':True, 'too high':False, 'too low':False}
    df.loc[len(df)] = new_row
    print(f'Congratulations! You have guessed the number {random_number} correctly!')
    df.to_csv(CSV_FILE, index=False)
    
    
    
guess(num_max)



