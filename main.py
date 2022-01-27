"""
Importing required packages
"""
import pandas as pd
from code.algorithms.semi_random import Semi_random
from code.algorithms.BFS import BFS
from code.algorithms.BFS_plus import BFS_plus
from code.classes.board import Board

"""
Setting the dimensions and puzzle number to load correct configuration file
"""
dimensions = 6
puzzle_number = 1
Rushhour_df = pd.read_csv(f"gameboards/Rushhour{dimensions}x{dimensions}_{puzzle_number}.csv")

"""
Creation of the different elements
"""
game = Board(dimensions)
semi_random = Semi_random(game)
bfs = BFS(game)
bfs_plus = BFS_plus(game)

"""
Setting up the board to run algorithm
"""
game.load_cars(Rushhour_df)
game.place_car(game.cars)
game.printBoard()

"""
Run chosen algorithm
"""
#bfs_plus.bfs_plus()
#bfs.bfs()
#semi_random.semi_random()

"""
Set correct output
"""
game.printBoard()
game.writeOutput()
