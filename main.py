## Jasper Paul
# main file for checking the code

import pandas as pd
from board import Board
from car import Car


Rushhour_df = pd.read_csv("gameboards/Rushhour12x12_7.csv")

game = Board(Rushhour_df)
game.load_cars(Rushhour_df), 
game.place_car()
game.moveCheck()