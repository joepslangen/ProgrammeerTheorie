## Jasper Paul
# main file for checking the code

import pandas as pd
from board import Board
from car import Car

#read rushhour6x6_1.csv
Rushhour_df = pd.read_csv("gameboards/Rushhour6x6_1.csv")

game = Board(Rushhour_df)
game.load_cars(Rushhour_df)
game.printBoard()
game.moveCarLeft("C")
game.printBoard()