## Jasper Paul
# main file for checking the code

import pandas as pd
from code.classes.board import Board
import numpy as np

#read rushhour6x6_1.csv
dimensions = 6
puzzle_number = 1
Rushhour_df = pd.read_csv(f"gameboards/Rushhour{dimensions}x{dimensions}_{puzzle_number}.csv")

"""
output = {}
output["moves"] = "time"
moves = []
times = []
for i in range(0, 100):

    game = Board(dimensions)
    game.load_cars(Rushhour_df)
    game.place_car(game.cars)
    game.printBoard()
    values = game.randomGameLoop()
    moves.append(values[0])
    times.append(values[1])
    game.printBoard()
    game.writeOutput()

print(f"Mean moves: {np.mean(moves)}")
print(f"Mean time: {np.mean(times)}")
"""

game = Board(dimensions)
game.load_cars(Rushhour_df)
game.place_car(game.cars)
game.printBoard()
#game.breadthFirst(heuristic = True)
game.randomGameLoop()
game.printBoard()
game.writeOutput()
