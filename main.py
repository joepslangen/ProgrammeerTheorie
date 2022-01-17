## Jasper Paul
# main file for checking the code

import pandas as pd
from board import Board
from car import Car

#read rushhour6x6_1.csv
dimensions = 6
puzzle_number = 1
Rushhour_df = pd.read_csv(f"gameboards/Rushhour{dimensions}x{dimensions}_{puzzle_number}.csv")

game = Board(dimensions)
game.load_cars(Rushhour_df)
game.place_car()
game.printBoard()
game.randomGameLoop()
game.writeOutput()