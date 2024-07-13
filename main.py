import pandas as pd
import numpy as np
import random
from nicegui import ui

num_max = 100

CSV_FILE = ('game_data.csv')

def get_data():
    return pd.read_csv(CSV_FILE)
            



# def guess(x):
#     random_number = random.randint(1,x)
#     guess = 0

#     while guess != random_number:
#         new_row = []
#         guess = int(input(f'Guess a number between 1 and {x}: '))
#         if guess < random_number:
#             new_row = {'game_number':current_game, 'guess':guess, 'correct':False, 'too high':False, 'too low':True}
#             df.loc[len(df)] = new_row
#             print('Sorry, guess again. Too low.')
#         elif guess > random_number:
#             new_row = {'game_number':current_game, 'guess':guess, 'correct':False, 'too high':True, 'too low':False}
#             df.loc[len(df)] = new_row
#             print('Sorry, guess again. Too high.')

#     new_row = {'game_number':current_game, 'guess':guess, 'correct':True, 'too high':False, 'too low':False}
#     df.loc[len(df)] = new_row
#     print(f'Congratulations! You have guessed the number {random_number} correctly!')
#     df.to_csv(CSV_FILE, index=False)

# guess(num_max)

result = ui.label() 
   
@ui.refreshable
def guess_entered(guess):
    df = get_data()
    
    games_played = df.game_number.unique()
    last_game = games_played[-1]
    current_game = last_game + 1
    random_number = random.randint(1,num_max)

    if guess < random_number:
        new_row = {'game_number':current_game, 'guess':guess, 'correct':False, 'too high':False, 'too low':True}
        df.loc[len(df)] = new_row
        result.set_text('Sorry, guess again. Too low.')
    elif guess > random_number:
        new_row = {'game_number':current_game, 'guess':guess, 'correct':False, 'too high':True, 'too low':False}
        df.loc[len(df)] = new_row
        result.set_text('Sorry, guess again. Too high.')
    else:
        new_row = {'game_number':current_game, 'guess':guess, 'correct':True, 'too high':False, 'too low':False}
        df.loc[len(df)] = new_row
        result.set_text(f'Congratulations! You have guessed the number {random_number} correctly!')
        df.to_csv(CSV_FILE, index=False)
        reset_button.visible=True
        reset_button.enabled=True
    

num = ui.number(label=f'Guess a number between 1 and {num_max}', value=0, 
                #validation={'Too small!': lambda value: value < 1, 'Too large': lambda value: value > 100 },
         precision=0, #on_change=lambda e: guess_entered(e.value)
         ) 
submit_button = ui.button("Submit", on_click=lambda: guess_entered(num.value))
reset_button = ui.button("Reset Game", on_click=lambda: reset_game())
reset_button.visible=False
reset_button.enabled=False

def reset_game():
    random_number = random.randint(1,num_max)
    num.value = 0
    result.set_text(f'Guess a number between 1 and {num_max}')
    reset_button.visible=False
    reset_button.enabled=False 

ui.run()



